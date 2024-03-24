#!/bin/bash
# Basic getting started script for the Wiki generator

# Ensure we have the generator
if [ ! -f "generator/.git" ]; then
	echo "Cloning submodule generator..."
	git submodule init generator
	git submodule update generator
fi

cd generator

# Ensure we have our dependencies
if [ ! -d "node_modules" ]; then
	echo "Installing modules..."
	npm i
fi

# Ready to rock and roll!
echo "Starting up..."
npm run dev

cd ..
