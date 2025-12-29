#!/bin/bash
# Basic getting started script for the Wiki generator

# Ensure the wiki software exists and is update to date.
if [ ! -f "site/.git" ]; then
	echo "Cloning wiki source submodule as 'site'..."
	git submodule update --init site
else
	# Pull new strata-wiki changes if the repository gets updated.
	echo Pulling any new wiki source submodule changes...
	git submodule update --remote
fi

cd site

# Make sure the node modules exist for the Wiki.
if [ ! -d "node_modules" ]; then
	echo "Installing node modules..."
	npm i
fi

# Ready to rock and roll!
echo "Starting up..."
npm run build
npm run dev

cd ..
