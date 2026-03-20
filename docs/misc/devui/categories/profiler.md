---
title: Profiler
weight: 30
---

# Profiler

The Profiler tab is the third tab in the Developer UI menu. Its main purpose is dynamically debugging different aspects of the map and the engine, showing the exact budget and usage. Additionally, a `.txt` report can be generated, containing every event that happened in a specified period of time. The menus of this tab are useful for optimising maps, materials and game events.

![All the menus of the Profiler tab](images/prof_all.png)

It consists of 8 menus - **Texture Budget Per-Frame**, **Texture Budget Global**, **Misc Graphics Stats**, **VProf Budget**, **VProf Report Generator**, **VProf Counters**, **c** and **VProf UI**.

****

## Texture Budget Per-Frame

Explanation

![Texture Budget Per-Frame when looking at a heavy map](images/prof_tbudget1.png)

Difference between map and wall budgets

![Texture Budget Per-Frame when looking at a wall](images/prof_tbudget2.png)

Values:
* Values

![Texture Budget Per-Frame menu](images/prof_tbudget1-menu.png)

****

## Texture Budget Global

Explanation

![Texture Budget Global](images/prof_tbudgetglob.png)

Values:
* Values

![Texture Budget Global menu](images/prof_tbudgetglob-menu.png)

****

## Misc Graphics Tab

Explanation

![Misc Graphics Tab](images/prof_misc.png)

Values:
* Values

****

## VProf Budget

Explanation

![VProf Budget](images/prof_vbudget.png)

> [!CAUTION]
> When having `Historgam` enabled, do not oversize the window! Developer UI can only have a certain amount of graphs drawn at the same time, drawing too many overflows the buffer and crashes the game!

Values:
* Values

****

## VProf Report Generator

Explanation

![VProf Report Generator](images/prof_vreport.png)

Values:
* Values

### VProf Generated Report

It also has an after-report window called **VProf Generated Report** that contains the reported file.

![VProf Generated Report](images/prof_vreport_gen.png)

Values:
* Values

****

## VProf Counters

Explanation

![VProf Counters](images/prof_vcount.png)

Values:
* Values

![VProf Counters Menu](images/prof_vcount-menu.png)

****

## VProf Tree

Explanation

![VProf Tree](images/prof_vtree.png)

Values:
* Values

![VProf Tree menu](images/prof_vtree-menu.png)

****

## VProf UI

Explanation

![VProf Tree](images/prof_vui.png)

****

# Ignore (TODO NOTES)

> There are 2 screenshots - one showing texture budget with the whole map visible, and the second showing the corner. TOTAL GRAPH MUST BE SHOWN BIGGER. The difference is huge.

> In the budgets, show that the values are map-specific. Also don't forget to describe each of them.

> In VProf Budget, scaling up the window with histogram enabled crashes the game.
