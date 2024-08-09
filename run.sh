#!/bin/bash
# Basic getting started script for the Wiki generator

# Ensure we have the generator
if [ ! -f "site/.git" ]; then
	echo "Cloning submodule site..."
	git submodule init site
	git submodule update site
fi

cd site

# Ensure we have our dependencies
if [ ! -d "node_modules" ]; then
	echo "Installing modules..."
	npm i
fi

# Ready to rock and roll!
echo "Starting up..."
npm run dev

cd ..
