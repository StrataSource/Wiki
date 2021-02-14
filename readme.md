# Chaos Source Wiki

This repository contains the markdown pages for the wiki available here: [https://www.chaosinitiative.com/wiki](https://www.chaosinitiative.com/wiki)

# Contribute
Everybody can contribute to the wiki. Please just fork this repo, commit your changes to a new branch and then create a pull request!

## Guidelines
Pull requests are thoroughly reviewed before being accepted. All contributions must adhere to these guidelines

### Pages have to
- be related to Chaos Source
- not be a duplicate of an existing page
- contain formal, passive language (No `I think` or `Next you go to`)

### Please do
- embed images or videos that showcase what is being explained
- add links wherever possible
- use proper, rich [markdown styling](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Please don't
- create pages for general Hammer Editor tutorials
- advertise
- add malicious links or (any) downloads

## Images and other media
We don't host any images ourselves. This helps with versioning and reduces workload. Please upload media that should be embedded into a page to some file hosting service like [imgur](https://imgur.com)

## Deployment
The online wiki is automatically updated every time this repository receives a new commit

# Technologies
This wiki is programmed in-house in [ASP.NET](https://dotnet.microsoft.com/apps/aspnet) 5.

- [Markdig](https://www.nuget.org/packages/Markdig/)
- [LibGit2Sharp](https://www.nuget.org/packages/LibGit2Sharp)