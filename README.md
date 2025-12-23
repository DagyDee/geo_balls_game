# ball_game

**Author:** DagyDee  
**Project type:** Python game  
**Primary use case:** Geocaching (mystery caches)

---

## Overview

This repository contains a small interactive game designed as a puzzle component for geocaching mystery caches.

The gameplay is based on a simple hide-and-seek mechanic: players click on moving objects to reveal hidden messages. Some messages contain clues (indexes or values) required to calculate final GPS coordinates.

The internal game name is **Click & Seek Coordinates Game**.  
The repository name **ball_game** reflects the original implementation using ball-shaped objects.

## Gameplay

- Multiple objects move across the screen
- Clicking an object may reveal a hidden message
- Some messages contain geocaching clues
- Messages are displayed briefly
- All required clues must be collected to solve the puzzle

## Features

- Click-based interaction
- Temporary message display
- Configurable object count and speed
- Resizable window
- Theme-ready design (objects can be replaced with custom assets)

## Requirements

- Python 3.10+
- pyglet

## Installation

Clone the repository:

`git clone https://github.com/DagyDee/ball_game.git`
`cd ball_game`

Create and activate a virtual environment (recommended):

`python -m venv venv`
`venv\Scripts\activate   # Windows`

Install dependencies:

`pip install pyglet`

## Running the Game

From the repository root:

`python balls.py`

The game window will open and start immediately.

## Configuration

Core game parameters are defined as constants in the main file and can be adjusted easily:

- Window size
- Object speed
- Number of objects
- Message display duration
- Object labels / clues

## Use in Geocaching

The game is intended for use as a custom puzzle in mystery caches.

Typical usage:
- Each object reveals a partial clue
- Players combine clues to calculate final coordinates
- The game can be themed or modified per cache

## License

Intended for personal, educational, and geocaching use.  
If reused or modified, please credit the author.

## Author

**DagyDee**  
GitHub: https://github.com/DagyDee
