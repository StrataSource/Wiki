# A script to gather all the available engine dumps to update the ones on the Wiki.
# Requires for you to input the installation path for the Strata Source title to dump from.
#! This was created with Portal 2: Community Edition in mind even if this supports Momentum Mod. Everything might not work correctly!
#! Portal: Revolution is not supported as overall as there will be no new changes to the game in terms of reference, the wiki should have everything on it already, and Linux support was dropped overall.

import os, sys, argparse, subprocess

# "Enums" used to give names to the array positions of ref_dump_list.
ANGELSCRIPT: int = 0
VSCRIPT: int = 1
SOUND_OPERATORS: int = 2
PARTICLE_OPERATORS: int = 3
CVARS: int = 4
MATERIAL_SHADERS: int = 5

# "Enums" used to give a name for the position values in each element of ref_dump_list.
COMMANDS: int = 0
DUMPED_FILES: int = 1 #
WIKI_FILES: int = 2

is_windows: bool = sys.platform == "win32"
exe_extension: str = ".exe" if is_windows else ""
binary_dir: str = "bin/win64" if is_windows else "bin/linux64"
relative_dir: str = os.path.dirname(os.path.abspath(__file__))
wiki_dump_dir: str = f"{relative_dir}/dumps/"

# This dictionary acts as a easy way to update the ConCommands and file names for files that should be dumped and added to the Wiki.
# New options will have to be added manually through out the program and some dumps do specific things with their options.
# Formatting is used to allow having a directory that uses a game directory like "p2ce". Most if not all these paths are relative to the base game directory.
# Format: "( list of ConCommands/docdump.exe parameter, list of dumped file names, list of file names that will be used for the final dump )"
#! NOTE: Make sure Hammer reference dumps are last so if a Strata title doesn't have/support Hammer, it can be skipped without failing to find it.
ref_dump_list: list[tuple] = [
    # Must open a map in order for AngelScript and VScript to all dump. First three ConCommands are for the game and the last is for Hammer.
    ( ["+map sp_a2_triple_laser", "+cl_scriptsystem_dump_json", "+sv_scriptsystem_dump_json", "+scriptsystem_dump_json"], ["{}/data/client/api_reference.json", "{}/data/server/api_reference.json", "hammer/scripts/api_reference.json"], ["angelscript_client_{}.json", "angelscript_server_{}.json", "angelscript_hammer_{}.json"] ),
    ( ["+map sp_a2_triple_laser", "+sv_script_dump_docs"], ["{}/data/vscript_docs.server.json"], ["vscript.json"] ),
    ( ["sound_ops"], ["{}/data/sound_operators.json"], ["sound_operators.json"] ), # Uses docdump.exe
    ( ["particle_ops"], ["{}/data/particle_operators.json"], ["particle_operators.json"] ), # Uses docdump.exe
    ( ["+cvar_dump"], ["{}/data/cvars.json"], ["commands_{}.json"] ),
    ( ["shaders"], ["{}/data/materials.json"], ["materials.json"] ) # Uses docdump.exe
]

# List of Strata Source titles that exist and that the tool supports.
# Format: (Inner game directory, game executable, Hammer executable (use None if Hammer is not available or not supported), docdump executable (None if doesn't exist for the title))
strata_candidates: list[tuple] = [
    ("p2ce", f"p2ce{exe_extension}", f"hammer{exe_extension}", f"docdump{exe_extension}"),
    ("momentum", f"momentum{exe_extension}", f"hammer{exe_extension}", f"docdump{exe_extension}"),
]

def Find(target: str, directory: str) -> str | None:
    """Searches a directory for a target file.

    Args:
        target (str): File to search for.
        directory (str): Directory to search.

    Returns:
        str | None: Full path to file if found, else None.
    """

    if (target == None or directory == None):
        return None

    for root, dirs, files in os.walk(directory):
        if target in files:
            return os.path.join(root, target)
    return None

def GetGameDir(basegame_dir: str) -> str | None:
    """Get a game's inner game directory used by the game. This assumes that each Strata title has a different inner game directory name. Ex. "p2ce", "momentum", "revolution".

    Args:
        basegame_dir (str): Full game path.

    Returns:
        str | None: Inner game directory name, if not found then None.
    """

    for game_dir, exe, hammer, docdump in strata_candidates:
        if os.path.isdir(f"{basegame_dir}/{game_dir}"):
            return game_dir
    return None

def GetGameExe(basegame_dir: str) -> str | None:
    """Get a game's executable. This assumes that each Strata title has a different executable name. Ex. "p2ce.exe", "momentum.exe", "revolution.exe".

    Args:
        basegame_dir (str): Full game path.

    Returns:
        str | None: Game executable file name, if not found then None.
    """

    for game_dir, exe, hammer, docdump in strata_candidates:
        if Find(exe, f"{basegame_dir}/{binary_dir}"):
            return exe
    return None

def GetGameHammer(basegame_dir: str) -> str | None:
    """Get a game's Hammer executable. Ex. "hammer.exe".

    Args:
        basegame_dir (str): Full game path.

    Returns:
        str | None: Hammer executable file name, if not found then None.
    """

    game_dir: str = GetGameDir(basegame_dir)
    for cur_game_dir, exe, hammer, docdump in strata_candidates:
        if (cur_game_dir != game_dir):
            continue
        # Make sure it actually exists on disk.
        if Find(hammer, f"{basegame_dir}/{binary_dir}"):
            return hammer
    return None

def GetGameDocDump(basegame_dir: str) -> str | None:
    """Get a game's docdump executable. Ex. "docdump.exe".

    Args:
        basegame_dir (str): Full game path.

    Returns:
        str | None: docdump executable file name, if not found then None.
    """

    game_dir: str = GetGameDir(basegame_dir)
    for cur_game_dir, exe, hammer, docdump in strata_candidates:
        if (cur_game_dir != game_dir):
            continue
        # Make sure it actually exists on disk.
        if Find(docdump, f"{basegame_dir}/{binary_dir}"):
            return docdump
    return None

def ProgramStr(hammer: bool = False, docdump: bool = False) -> str:
    """Return the current program that will be run based on the passed in bools.

    Args:
        hammer (bool, optional): If it's Hammer being run return "Hammer". Defaults to False.
        docdump (bool, optional): If it's docdump being run return "docdump". Defaults to False.

    Returns:
        str: Will return "engine" if neither Hammer or docdump are being run.
    """

    if (hammer):
        return "Hammer"
    elif (docdump):
        return "docdump"
    return "engine"

def StartProgram(basegame_dir: str, args: str, hammer: bool = False, docdump: bool = False) -> None:
    """Starts up one of the three programs the script uses to acquire dumps. By default, if Hammer and docdump are false, the engine is run.

    Args:
        basegame_dir (str): Path to the game.
        args (str): Arguments that will passed to the program.
        hammer (bool, optional): If true, will run Hammer. Defaults to False.
        docdump (bool, optional): If true, will run docdump. Defaults to False.
    """

    print(f'Launching {ProgramStr(hammer, docdump)} with arguments: "{args}"')

    completedProcess = 0
    if (hammer):
        hammer_exe: str = GetGameHammer(basegame_dir)
        if (hammer_exe == None):
            print("Hammer is either not supported or couldn't be found for the Strata Source title, skipping!")
            return

        print(f'Dumping from Hammer is not supported right now, for now manually dump what comes from Hammer using: "{args.replace("+", "")}"')
        return
        completedProcess = subprocess.run(f'"{basegame_dir}/{binary_dir}/{hammer_exe}" {args}', shell=True)
    elif (docdump):
        docdump_exe: str = GetGameDocDump(basegame_dir)
        if (docdump_exe == None):
            print("docdump is either not supported or couldn't be found for the Strata Source title, skipping!")
            return

        print("YES, docdump CRASHING is NORMAL, ignore it, it will be fixed!")
        completedProcess = subprocess.run(f'"{basegame_dir}/{binary_dir}/{docdump_exe}" {args}', shell=True)
    else: # engine
        completedProcess = subprocess.run(f'"{basegame_dir}/{binary_dir}/{GetGameDir(basegame_dir)}" {args}', shell=True)

    # TODO: The "and not docdump" is needed for docdump for the moment because the program currently crashes even when it successfully dumps. REMOVE WHEN ITS FIXED!
    if (completedProcess.returncode != 0 and not docdump):
        print(f'Something went wrong when running {ProgramStr(hammer, docdump)}! Return code: "{completedProcess.returncode}"')
        print("Please check your game path and please report in the P2:CE Discord if issues still occur!")
        sys.exit(1)

def ApplyDumps(basegame_dir: str, dump_group: int) -> None:
    """Find, rename, and apply the new dumps to the Wiki's dumps folder.

    Args:
        basegame_dir (str): Path to the game.
        dump_group (int): The specific type of dumps that are being updated. (Ex. ANGELSCRIPT, SOUND_OPERATORS)
    """

    game_dir: str = GetGameDir(basegame_dir)
    hammer_exe: str = GetGameHammer(basegame_dir)
    docdump_exe: str = GetGameDocDump(basegame_dir)

    for index, dump_file in enumerate(ref_dump_list[dump_group][DUMPED_FILES]):
        dump_file = dump_file.format(game_dir)

        # If the title doesn't support hammer, skip finding any Hammer related dumps.
        if ("hammer" in dump_file and hammer_exe == None):
            continue;
        # If the title doesn't have docdump, skip finding any dumps that are used to get it.
        if ((dump_group in (SOUND_OPERATORS, PARTICLE_OPERATORS, MATERIAL_SHADERS)) and docdump_exe == None):
            continue;

        dump_src: str = f"{basegame_dir}/{os.path.dirname(dump_file)}" # Src folder of dumped files.

        print(f'Gathering and applying dump "{os.path.basename(dump_file)}" to Wiki located in: "{dump_src}"')
        if (not Find(os.path.basename(dump_file), dump_src)):
            print(f'Failed to find the dumped file: "{dump_file}"!')
            print("Please report on the P2:CE Discord!")
            sys.exit(1)

        # Fix line endings, some dumps are dumped with CRLF line endings.
        # Keeping it with LF won't cause git to track changes simply because line endings changed.
        with open(f"{basegame_dir}/{dump_file}", 'rb+') as dumped_file:
            data = dumped_file.read().replace(b'\r\n', b'\n')
            dumped_file.seek(0)
            dumped_file.write(data)
            dumped_file.truncate()
            dumped_file.close()

        os.replace(f"{basegame_dir}/{dump_file}", wiki_dump_dir + ref_dump_list[dump_group][WIKI_FILES][index].format(game_dir))

# ---------------------------

def DumpAS(basegame_dir: str) -> int:
    print("Currently, AngelScript reference dumping is not available right now.")
    print(f'For now manually dump what comes from the engine using: "{" ".join(ref_dump_list[ANGELSCRIPT][COMMANDS][:-1]).replace("+", "")}"')
    print(f'For Hammer use: "{"".join(ref_dump_list[ANGELSCRIPT][COMMANDS][-1]).replace("+", "")}"')
    return
    print("Dumping new AngelScript reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[ANGELSCRIPT][COMMANDS][:-1]), "+exit"])
    StartProgram(basegame_dir, args)

    # Run Hammer.
    args = "".join(ref_dump_list[ANGELSCRIPT][COMMANDS][-1])
    StartProgram(basegame_dir, args, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, ANGELSCRIPT)

    print("Finished dumping and applying new AngelScript reference to Wiki!")
    return 0;

def DumpVScript(basegame_dir: str) -> int:
    print("Currently, VScript reference dumping is not available right now.")
    print(f'For now manually dump what comes from the engine using: "{" ".join(ref_dump_list[VSCRIPT][COMMANDS]).replace("+", "")}"')
    return
    print("Dumping new VScript reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[VSCRIPT][COMMANDS]), "+exit"])
    StartProgram(basegame_dir, args)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, VSCRIPT)

    print("Finished dumping and applying new VScript reference to Wiki!")
    return 0;

def DumpSoundOperators(basegame_dir: str) -> int:
    print("Dumping new Sound Operators reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[SOUND_OPERATORS][COMMANDS]), f'"{basegame_dir}/{"".join(ref_dump_list[SOUND_OPERATORS][DUMPED_FILES]).format(GetGameDir(basegame_dir))}"'])
    StartProgram(basegame_dir, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, SOUND_OPERATORS)

    print("Finished dumping and applying new Sound Operators reference to Wiki!")
    return 0;

def DumpParticles(basegame_dir: str) -> int:
    print("Dumping new Particle Operators reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[PARTICLE_OPERATORS][COMMANDS]), f'"{basegame_dir}/{"".join(ref_dump_list[PARTICLE_OPERATORS][DUMPED_FILES]).format(GetGameDir(basegame_dir))}"'])
    StartProgram(basegame_dir, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, PARTICLE_OPERATORS)

    print("Finished dumping and applying new Particle Operators reference to Wiki!")
    return 0;

def DumpCVars(basegame_dir: str) -> int:
    print("Dumping new ConCommand & ConVar reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[CVARS][COMMANDS]), "+exit"])
    StartProgram(basegame_dir, args)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, CVARS)

    print("Finished dumping and applying new ConCommand & ConVar reference to Wiki!")
    return 0;

def DumpShaders(basegame_dir: str) -> int:
    print("Dumping new Material Shader reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[MATERIAL_SHADERS][COMMANDS]), f'"{basegame_dir}/{"".join(ref_dump_list[MATERIAL_SHADERS][DUMPED_FILES]).format(GetGameDir(basegame_dir))}"'])
    StartProgram(basegame_dir, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(basegame_dir, MATERIAL_SHADERS)

    print("Finished dumping and applying new Material Shader reference to Wiki!")
    return 0;

# ---------------------------

def DumpALL(basegame_dir: str) -> int:
    print("Dumping all engine references!")

    # TODO: Uncomment out when it is possible to get the AngelScript and VScript docs automatically.
    # DumpAS(basegame_dir)
    # print("\n")
    # DumpVScript(basegame_dir)
    # print("\n")
    DumpSoundOperators(basegame_dir)
    print("\n")
    DumpParticles(basegame_dir)
    print("\n")
    DumpCVars(basegame_dir)
    print("\n")
    DumpShaders(basegame_dir)
    print("\n")

    print("Dumped and applied all references to Wiki!")
    return 0

# ---------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        "wiki_dumps",
        formatter_class = argparse.RawTextHelpFormatter,
        description = """The Strata Source Wiki reference dumper! Currently supports Portal 2: Community Edition and Momentum Mod.
NOTE: This tool was designed with Portal 2: Community Edition in mind so not all options will work correctly if using another Strata Source title.
WARNING: Portal: Revolution dumping is not available at all as the wiki should have everything on it already, there will be no more game updates that add things, and Linux support overall was dropped. Portal: Revolution 2 will be supported in the future.""",
epilog="""
     ^_/ffjjjjf)l
   ^_/jjjjjjjjjjj1!.
 ,?fjjffjjjjjjjffjj(>.
>fjjffjjjjjjjjjjjffjj|<'
.I}jjjffjfjjjjjjjffffjj\\+`
   :[fjjjjjjjjjjjjjjjffjj/_^
     ,?tfffffffffffffffffjjt?,
       '```````````````^^^`^,`
                                Powered By Strata Source
 .''''''''''''''''''''''.
   .''''''''''''''''''''''.
     .''''''''''''''''''''''.
       .'''''''''''''''''''''.
         .'''''''''''''''''.
           .'''''''''''''.
             .'''''''''.
""")
    conflict_group = parser.add_mutually_exclusive_group();

    conflict_group.add_argument(
        "-a", "--all",
        dest = "dump_all",
        action = "store_true",
        help = "Dump all the available references."
    )
    conflict_group.add_argument(
        "-d", "--dump",
        dest = "dump_option",
        type = int,
        choices = [0, 1, 2, 3, 4, 5],
        # TODO: Update when AS and VScript dumping is fixed.
        help = """Specify a specific reference to dump if "-a/-all" is not specified.
(CURRENTLY NOT WORKING) AngelScript = 0
(CURRENTLY NOT WORKING) VScript = 1
Sound Operators = 2
Particle Operators = 3
ConCommands & ConVars = 4
Material Shaders = 5"""
    )
    parser.add_argument(
        "--debug",
        dest = "debug_input",
        action = "store_true",
        help = "Debug testing path inputs for the program. This will not dump at all. Need valid basegame_dir to test."
    )
    parser.add_argument(
        "basegame_dir",
        type = str,
        help = 'Full path to your Strata Source game installation for Steam. Ex. "Steam/steamapps/common/Portal 2 Community Edition"'
    )

    args = parser.parse_args();

    if (args.basegame_dir):
        game_executable: str = GetGameExe(args.basegame_dir)
        game_dir: str = GetGameDir(args.basegame_dir)
        if (not game_executable or not game_dir):
            print("Game executable or inner game directory could not be located! Are you sure you've entered the path correctly? Make sure to use quotes!")
            print('Is this a supported game? Check program help using "-h/--help".')
            print(f'basegame_dir: "{args.basegame_dir}"')
            sys.exit(1)

        #! Overall, Portal: Revolution is not supported as you can't dump much from it anyways, there is no Linux support, and nothing new will be added anyways until Revo 2.
        if (game_executable == "revolution.exe"):
            print("Portal: Revolution is not supported by this tool as 'docdump' is missing, Linux support has been dropped, and overall there will be no new changes and what is on the wiki should be what is on the current public build. If you want to dump it's references, you will need to do it manually.")
            sys.exit(1)

    # Debug with inputs
    if (args.debug_input):
        print(f'basegame_dir: "{args.basegame_dir}"')
        print(f'dump_all: "{args.dump_all}"')
        print(f'dump_option: "{args.dump_option}"')
        print(f'game_executable: "{GetGameExe(args.basegame_dir)}"')
        print(f'hammer_executable: "{GetGameHammer(args.basegame_dir)}"')
        print(f'docdump_executable: "{GetGameDocDump(args.basegame_dir)}"')
        print(f'game_dir: "{GetGameDir(args.basegame_dir)}"')
        print(f'is_windows: "{is_windows}"')
        print(f'binary_dir: "{binary_dir}"')
        print(f'relative_dir: "{relative_dir}"')
        print(f'wiki_dump_dir: "{wiki_dump_dir}"')

        print("Format String Test (ANGELSCRIPT/DUMPED_FILES):")
        for index, dump_file in enumerate(ref_dump_list[ANGELSCRIPT][DUMPED_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[ANGELSCRIPT][DUMPED_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')
        print("Format String Test (ANGELSCRIPT/WIKI_FILES):")
        for index, dump_file in enumerate(ref_dump_list[ANGELSCRIPT][WIKI_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[ANGELSCRIPT][WIKI_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')

        print("Format String Test (VSCRIPT/DUMPED_FILES):")
        for index, dump_file in enumerate(ref_dump_list[VSCRIPT][DUMPED_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[VSCRIPT][DUMPED_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')
        print("Format String Test (VSCRIPT/WIKI_FILES):")
        for index, dump_file in enumerate(ref_dump_list[VSCRIPT][WIKI_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[VSCRIPT][WIKI_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')

        print("Format String Test (CVARS/DUMPED_FILES):")
        for index, dump_file in enumerate(ref_dump_list[CVARS][DUMPED_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[CVARS][DUMPED_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')
        print("Format String Test (CVARS/WIKI_FILES):")
        for index, dump_file in enumerate(ref_dump_list[CVARS][WIKI_FILES]):
            print(f'\tref_dump_list: "{ref_dump_list[CVARS][WIKI_FILES][index].format(game_dir)}"')
            print(f'\tdump_file: "{dump_file.format(game_dir)}"')
        sys.exit(0)

    if (not args.dump_all and args.dump_option == None):
        print("'-a/--all' or '-d/--dump' need to be specified before the game path in order to dump a engine reference!")
        parser.print_usage()
        sys.exit(1)

    # Make sure the Wiki's "dumps" directory exists.
    os.makedirs("./dumps", exist_ok=True)

    # Dump all references.
    if (args.dump_all):
        sys.exit(DumpALL(args.basegame_dir))

    # Dump specific reference.
    match (args.dump_option):
        case (0):
            sys.exit(DumpAS(args.basegame_dir))
        case (1):
            sys.exit(DumpVScript(args.basegame_dir))
        case (2):
            sys.exit(DumpSoundOperators(args.basegame_dir))
        case (3):
            sys.exit(DumpParticles(args.basegame_dir))
        case (4):
            sys.exit(DumpCVars(args.basegame_dir))
        case (5):
            sys.exit(DumpShaders(args.basegame_dir))

    # If no arguments have been passed. This technically shouldn't be reached, but just in case.
    parser.print_help()

# ---------------------------

if __name__ == "__main__":
    main()