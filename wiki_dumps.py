# A script to gather all the available engine dumps to update the ones on the Wiki.
# Requires for you to input the installation path for Portal 2: Community Edition.
#! While programmed to work with other Strata Source titles, only P2:CE has all the commands and tools available for dumping.
#! Only use other Strata Source titles if you know what you are doing.

import os, sys, argparse

# "Enums" meant to be used to put array positions to names for ref_dump_list
ANGELSCRIPT: int = 0
VSCRIPT: int = 1
SOUND_OPERATORS: int = 2
PARTICLE_OPERATORS: int = 3
CVARS: int = 4
MATERIAL_SHADERS: int = 5

COMMANDS: int = 0
DUMPED_FILES: int = 1
WIKI_FILES: int = 2

is_windows: bool = sys.platform == "win32"
binary_dir: str = "bin/win64" if is_windows else "bin/linux64"
relative_dir: str = os.path.dirname(os.path.abspath(__file__))
wiki_dump_dir: str = f"{relative_dir}/dumps/"

# This dictionary acts as a easy way to update the ConCommands and file names for files that should be dumped and added to the Wiki.
# New options will have to be added manually through out the program and some dumps do specific things with their options.
# Format: "( list of ConCommands/docdump.exe parameter, list of dumped file names, list of Wiki file names )"
#! NOTE: Make sure Hammer reference dumps are last so if a Strata title doesn't have/support Hammer, it can be skipped without failing to find it.
ref_dump_list: list[tuple] = [
    # Must open a map in order for AngelScript and VScript to all dump.
    ( ["+map sp_a2_triple_laser", "+cl_scriptsystem_dump_json", "+sv_scriptsystem_dump", "+scriptsystem_dump_json"], ["{}/data/client/api_reference.json", "{}/data/server/api_reference.json", "hammer/scripts/api_reference.json"], ["angelscript_client_{}.json", "angelscript_server_{}.json", "angelscript_hammer_{}.json"] ),
    ( ["+map sp_a2_triple_laser", "+sv_script_dump_docs"], ["{}/data/vscript_docs.server.json"], ["vscript.json"] ),
    ( ["sound_ops"], ["sound_operators.json"], ["sound_operators.json"] ), # Uses docdump.exe
    ( ["particle_ops"], ["particle_operators.json"], ["particle_operators.json"] ), # Uses docdump.exe
    ( ["+cvar_dump"], ["{}/data/cvars.json"], ["commands_{}.json"] ),
    ( ["shaders"], ["materials.json"], ["materials.json"] ) # Uses docdump.exe
]

# List of Strata Source titles that exist and that the tool supports.
# Format: (Inner game directory, game executable, Hammer executable (use None if Hammer is not available or not supported), docdump executable (None if doesn't exist for the title))
strata_candidates: list[tuple] = [
    ("p2ce", "p2ce.exe" if is_windows else "p2ce", "hammer.exe" if is_windows else "hammer", "docdump.exe" if is_windows else "docdump"),
    ("momentum", "momentum.exe" if is_windows else "momentum", "hammer.exe" if is_windows else "hammer", "docdump.exe" if is_windows else "docdump"),
    ("revolution", "revolution.exe", "hammer.exe", None), #! Linux support was removed from Revolution :(
]

def Find(target: str, directory: str) -> str | None:
    """
    Searches a directory for a target file.

    :param target: File to search for.
    :type target: str
    :param directory: Directory to search.
    :type directory: str
    :return: Full path to file if found, else None.
    :rtype: str | None
    """

    if (target == None or directory == None):
        return None

    for root, dirs, files in os.walk(directory):
        if target in files:
            return os.path.join(root, target)
    return None

def GetGameDir(game_path: str) -> str | None:
    """
    Get a game's inner game directory used by the game. This assumes that each Strata title has a different inner game directory name. Ex. "p2ce", "momentum", "revolution".

    :param game_path: Full game path.
    :type game_path: str
    :return: Inner game directory name, if not found then None.
    :rtype: str | None
    """

    for game_dir, exe, hammer, docdump in strata_candidates:
        if os.path.isdir(f"{game_path}/{game_dir}"):
            return game_dir
    return None

def GetGameExe(game_path: str) -> str | None:
    """
    Get a game's executable. This assumes that each Strata title has a different executable name. Ex. "p2ce.exe", "momentum.exe", "revolution.exe".

    :param game_path: Full game path.
    :type game_path: str
    :return: Game executable file name, if not found then None.
    :rtype: str | None
    """

    for game_dir, exe, hammer, docdump in strata_candidates:
        if Find(exe, f"{game_path}/{binary_dir}"):
            return exe
    return None

def GetGameHammer(game_path: str) -> str | None:
    """
    Get a game's Hammer executable. Ex. "hammer.exe".

    :param game_path: Full game path.
    :type game_path: str
    :return: Hammer executable file name, if not found then None.
    :rtype: str | None
    """

    game_dir: str = GetGameDir(game_path)
    for cur_game_dir, exe, hammer, docdump in strata_candidates:
        if (cur_game_dir != game_dir):
            continue
        # Make sure it actually exists on disk.
        if Find(hammer, f"{game_path}/{binary_dir}"):
            return hammer
    return None

def GetGameDocDump(game_path: str) -> str | None:
    """
    Get a game's docdump executable. Ex. "docdump.exe".

    :param game_path: Full game path.
    :type game_path: str
    :return: docdump executable file name, if not found then None.
    :rtype: str | None
    """

    game_dir: str = GetGameDir(game_path)
    for cur_game_dir, exe, hammer, docdump in strata_candidates:
        if (cur_game_dir != game_dir):
            continue
        # Make sure it actually exists on disk.
        if Find(docdump, f"{game_path}/{binary_dir}"):
            return docdump
    return None

def ProgramStr(hammer: bool = False, docdump: bool = False) -> str:
    """
    Return the current program that will be run based on the passed in bools.

    :param hammer: If it's Hammer being run return "Hammer".
    :type hammer: bool
    :param docdump: If it's docdump being run return "docdump".
    :type docdump: bool
    :return: Will return "engine" if neither Hammer or docdump are being run.
    :rtype: str
    """

    if (hammer):
        return "Hammer"
    elif (docdump):
        return "docdump"
    return "engine"

def StartProgram(game_path: str, args: str, hammer: bool = False, docdump: bool = False) -> None:
    """
    Starts up one of the three programs the script uses to acquire dumps. By default, if Hammer and docdump are false, the engine is run.

    :param game_path: Path to the game.
    :type game_path: str
    :param args: Arguments that will passed to the program.
    :type args: list[str]
    :param hammer: If true, will run Hammer.
    :type hammer: bool
    :param docdump: If true, will run docdump.
    :type docdump: bool
    """

    print(f'Launching {ProgramStr(hammer, docdump)} with arguments: "{args}"')

    return_code: int
    if (hammer):
        hammer_exe: str = GetGameHammer(game_path)
        if (hammer_exe == None):
            print("Hammer is either not supported or couldn't be found for the Strata Source title, skipping!")
            return

        print(f'Dumping from Hammer is not supported right now, for now manually dump what comes from Hammer using: "{args.replace("+", "")}"')
        return
        return_code = os.system(f'"{game_path}/{binary_dir}/{hammer_exe}" {args}')
    elif (docdump):
        docdump_exe: str = GetGameDocDump(game_path)
        if (docdump_exe == None):
            print("docdump is either not supported or couldn't be found for the Strata Source title, skipping!")
            return

        print("YES, docdump CRASHING is NORMAL, ignore it, it will be fixed.")
        return_code = os.system(f'"{game_path}/{binary_dir}/{docdump_exe}" {args}')
    else: # engine
        return_code = os.system(f'"{game_path}/{binary_dir}/{GetGameDir(game_path)}" {args}')

    # TODO: The "and not docdump" is needed for docdump for the moment because the program is currently crashed. REMOVE WHEN ITS FIXED!
    if (return_code != 0 and not docdump):
        print(f'Something went wrong when running {ProgramStr(hammer, docdump)}! Return code: "{return_code}"')
        print("Please check your game path and please report in the P2:CE Discord if issues still occur!")
        sys.exit(1)

def ApplyDumps(dump_path: str, dump_group: int, game_path: str = "") -> None:
    """
    Find, rename, and apply the new dumps to the Wiki's dumps folder.

    :param dump_path: Directory where the dumps should be looked for.
    :type dump_path: str
    :param dump_group: The specific type of dumps that are being updated. (Ex. ANGELSCRIPT, SOUND_OPERATORS)
    :type dump_group: int
    """

    game_dir: str = GetGameDir(dump_path)
    if (game_dir == None):
        game_dir = GetGameDir(game_path)
    hammer_exe: str = GetGameHammer(game_path)
    docdump_exe: str = GetGameDocDump(game_path)

    for index, dump_file in enumerate(ref_dump_list[dump_group][DUMPED_FILES]):
        dump_file = dump_file.format(game_dir)

        # If the title doesn't support hammer, skip finding any Hammer related dumps.
        if ("hammer" in dump_file and hammer_exe == None):
            continue;
        # If the title doesn't have docdump, skip finding any dumps that are used to get it.
        if ((dump_group in (SOUND_OPERATORS, PARTICLE_OPERATORS, MATERIAL_SHADERS)) and docdump_exe == None):
            continue;

        print(f'Gathering and applying dump "{os.path.basename(dump_file)}" to Wiki located in: "{dump_path}/{os.path.dirname(dump_file)}"')
        if (not Find(os.path.basename(dump_file), f"{dump_path}/{os.path.dirname(dump_file)}")):
            print(f'Failed to find the dumped file: "{dump_file}"!')
            print("Please report on the P2:CE Discord!")
            sys.exit(1)

        # Fix line endings, some dumps are dumped with CRLF line endings.
        # Keeping it with LF won't cause git to track changes simply because line endings changed.
        with open(f"{dump_path}/{dump_file}", 'rb+') as dumped_file:
            data = dumped_file.read().replace(b'\r\n', b'\n')
            dumped_file.seek(0)
            dumped_file.write(data)
            dumped_file.truncate()

        os.replace(f"{dump_path}/{dump_file}", wiki_dump_dir + ref_dump_list[dump_group][WIKI_FILES][index].format(game_dir))

# ---------------------------

def DumpAS(game_path: str) -> int:
    print("Currently, AngelScript reference dumping is not working right now. This will be fixed later by engine updates.")
    print(f'For now manually dump what comes from the engine using: "{" ".join(ref_dump_list[ANGELSCRIPT][COMMANDS][:-1]).replace("+", "")}"')
    print(f'For Hammer use: "{"".join(ref_dump_list[ANGELSCRIPT][COMMANDS][-1]).replace("+", "")}"')
    return
    print("Dumping new AngelScript reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[ANGELSCRIPT][COMMANDS][:-1]), "+exit"])
    StartProgram(game_path, args)

    # Run Hammer.
    args = "".join(ref_dump_list[ANGELSCRIPT][COMMANDS][-1])
    StartProgram(game_path, args, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(game_path, ANGELSCRIPT)

    print("Finished dumping and applying new AngelScript reference to Wiki!")
    return 0;

def DumpVScript(game_path: str) -> int:
    print("Currently, VScript reference dumping is not working right now. This will be fixed later by engine updates.")
    print(f'For now manually dump what comes from the engine using: "{" ".join(ref_dump_list[VSCRIPT][COMMANDS]).replace("+", "")}"')
    return
    print("Dumping new VScript reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[VSCRIPT][COMMANDS]), "+exit"])
    StartProgram(game_path, args)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(game_path, VSCRIPT)

    print("Finished dumping and applying new VScript reference to Wiki!")
    return 0;

def DumpSoundOperators(game_path: str) -> int:
    print("Dumping new Sound Operators reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[SOUND_OPERATORS][COMMANDS]), " ".join(ref_dump_list[SOUND_OPERATORS][WIKI_FILES])])
    StartProgram(game_path, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(relative_dir, SOUND_OPERATORS, game_path)

    print("Finished dumping and applying new Sound Operators reference to Wiki!")
    return 0;

def DumpParticles(game_path: str) -> int:
    print("Dumping new Particle Operators reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[PARTICLE_OPERATORS][COMMANDS]), " ".join(ref_dump_list[PARTICLE_OPERATORS][WIKI_FILES])])
    StartProgram(game_path, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(relative_dir, PARTICLE_OPERATORS, game_path)

    print("Finished dumping and applying new Particle Operators reference to Wiki!")
    return 0;

def DumpCVars(game_path: str) -> int:
    print("Dumping new ConCommand & ConVar reference....")

    # Run the engine.
    args: str = " ".join(["-novid", " ".join(ref_dump_list[CVARS][COMMANDS]), "+exit"])
    StartProgram(game_path, args)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(game_path, CVARS)

    print("Finished dumping and applying new ConCommand & ConVar reference to Wiki!")
    return 0;

def DumpShaders(game_path: str) -> int:
    print("Dumping new Material Shader reference....")

    # Run docdump.
    args: str = " ".join([" ".join(ref_dump_list[MATERIAL_SHADERS][COMMANDS]), " ".join(ref_dump_list[MATERIAL_SHADERS][WIKI_FILES])])
    StartProgram(game_path, args, False, True)

    # Find the dumps and apply them to the Wiki.
    ApplyDumps(relative_dir, MATERIAL_SHADERS, game_path)

    print("Finished dumping and applying new Material Shader reference to Wiki!")
    return 0;

# ---------------------------

def DumpALL(game_path: str) -> int:
    print("Dumping all engine references!")

    # TODO: Uncomment out when it is possible to get the AngelScript and VScript docs automatically.
    # DumpAS(game_path)
    # print("\n")
    # DumpVScript(game_path)
    # print("\n")
    DumpSoundOperators(game_path)
    print("\n")
    DumpParticles(game_path)
    print("\n")
    DumpCVars(game_path)
    print("\n")
    DumpShaders(game_path)
    print("\n")

    print("Dumped and applied all references to Wiki!")
    return 0

# ---------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        "wiki_dumps",
        formatter_class = argparse.RawTextHelpFormatter,
        description = "The Strata Source Wiki reference dumper! Currently supports Portal 2: Community Edition, Momentum Mod, and Portal: Revolution.",
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
        type=int,
        choices = [0, 1, 2, 3, 4, 5],
        # TODO: Update when fixed.
        help = 'Specify a specific reference to dump if "-a/-all" is not specified.\n(CURRENTLY NOT WORKING) AngelScript = 0\n(CURRENTLY NOT WORKING) VScript = 1\nSound Operators = 2\nParticle Operators = 3\nConCommands & ConVars = 4\nMaterial Shaders = 5'
    )
    parser.add_argument(
        "--debug",
        dest = "debug_input",
        action = "store_true",
        help = "Debug testing path inputs for the program, will not dump, please ignore! Need valid game_path to test!"
    )
    parser.add_argument(
        "game_path",
        type=str,
        help = 'Full path to your Strata Source game installation for Steam. Ex. "Steam/steamapps/common/Portal 2 Community Edition"'
    )

    args = parser.parse_args();

    if (args.game_path):
        game_executable: str = GetGameExe(args.game_path)
        game_dir: str = GetGameDir(args.game_path)
        if (not game_executable or not game_dir):
            print("Game executable or inner game directory could not be located! Are you sure you've entered the path correctly? Make sure to use quotes!")
            print('Is this a supported game? Check program help using "-h/--help".')
            print(f'game_path: "{args.game_path}"')
            sys.exit(1)

        #! Linux support was removed from Revolution, Linux users will have to dump it manually.
        if (not is_windows and game_executable == "revolution.exe"):
            print("Portal: Revolution's Linux support has been removed. If you are on Linux and want to dump it's references, you will need to do it manually.")
            sys.exit(1)

    # Debug with inputs
    if (args.debug_input):
        print(f'game_path: "{args.game_path}"')
        print(f'dump_all: "{args.dump_all}"')
        print(f'dump_option: "{args.dump_option}"')
        print(f'game_executable: "{GetGameExe(args.game_path)}"')
        print(f'hammer_executable: "{GetGameHammer(args.game_path)}"')
        print(f'docdump_executable: "{GetGameDocDump(args.game_path)}"')
        print(f'game_dir: "{GetGameDir(args.game_path)}"')
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
        sys.exit(DumpALL(args.game_path))

    # Dump specific reference.
    match (args.dump_option):
        case (0):
            sys.exit(DumpAS(args.game_path))
        case (1):
            sys.exit(DumpVScript(args.game_path))
        case (2):
            sys.exit(DumpSoundOperators(args.game_path))
        case (3):
            sys.exit(DumpParticles(args.game_path))
        case (4):
            sys.exit(DumpCVars(args.game_path))
        case (5):
            sys.exit(DumpShaders(args.game_path))

    # If no arguments have been passed. This technically shouldn't be reached, but just in case.
    parser.print_help()

# ---------------------------

if __name__ == "__main__":
    main()