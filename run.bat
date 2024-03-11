@ECHO OFF
REM Basic getting started script for the Wiki generator

REM Ensure we have the generator
IF NOT EXIST generator\.git (
	echo Cloning submodule generator...
	git submodule init generator
	git submodule update generator
)

cd generator

REM Ensure we have our dependencies
IF NOT EXIST node_modules (
	echo Installing modules...
	call npm i
)

REM Ready to rock and roll!
echo Starting up...
call npm run dev

cd ..

