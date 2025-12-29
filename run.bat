@ECHO OFF
REM Basic getting started script for the Wiki generator

REM Ensure the wiki software exists and is update to date.
IF NOT EXIST "site/.git" (
	echo "Cloning wiki source submodule as 'site'..."
	git submodule update --init site
) ELSE (
	REM Pull new strata-wiki changes if the repository gets updated.
	echo "Pulling any new wiki source submodule changes..."
	git submodule update --remote
)

cd site

REM Make sure the node modules exist for the Wiki.
IF NOT EXIST node_modules (
	echo "Installing node modules..."
	call npm i
)

REM Ready to rock and roll!
echo "Starting up..."
call npm run build
call npm run dev

cd ..
