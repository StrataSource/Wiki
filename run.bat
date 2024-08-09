@ECHO OFF
REM Basic getting started script for the Wiki generator

REM Ensure we have the generator
IF NOT EXIST site\.git (
	echo Cloning submodule site...
	git submodule init site
	git submodule update site
)

cd site

REM Ensure we have our dependencies
IF NOT EXIST node_modules (
	echo Installing modules...
	call npm i
)

REM Ready to rock and roll!
echo Starting up...
call npm run dev

cd ..

