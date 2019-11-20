# Snake

A simple environment written in python 3.6 for the game snake for [open AI Request for research 2.0](https://openai.com/blog/requests-for-research-2/)

Table of Contents

1. [Objective](#Objective)
2. [Installation](#Installation)
3. [Rules](#Rules)
4. [Modes](#Modes)
    4.1 [Human](#Human-player)
5. [Task List](#TaskList)
 

## Objective
>⭐⭐ Slitherin’. Implement and solve a multiplayer clone of the classic Snake game (see slither.io for inspiration) as a Gym environment. Environment: have a reasonably large field with multiple snakes; snakes grow when eating randomly-appearing fruit; a snake dies when colliding with another snake, itself, or the wall; and the game ends when all snakes die. Start with two snakes, and scale from there. Agent: solve the environment using self-play with an RL algorithm of your choice. You’ll need to experiment with various approaches to overcome self-play instability (which resembles the instability people see with GANs). For example, try training your current policy against a distribution of past policies. Which approach works best? Inspect the learned behavior: does the agent learn to competently pursue food and avoid other snakes? Does the agent learn to attack, trap, or gang up against the competing snakes? Tweet us videos of the learned policies!

[(src)](https://openai.com/blog/requests-for-research-2/)

## Installation
Steps:
1. Clone the repo
2. Go into the project's root directory
3. Activate the virtual environment (snake)
    * Linux : `source snake\bin\activate`
4. Install required packages `pip3 install -r requirements.txt` (__SKIP IF ON LINUX__)
5. cd into the folder 'src'
6. run `python3 game.py --help` to get usage

## Rules
The game of snake has very simple rules:
* The snake can move left, right, up or down
* The snake can eat fruits to increase score and length
* The snake dies when it hits a wall or runs into itself

## Modes

#### Human Player
Status : **Implemented**

Usage : `python3 game.py --agent H`

Allows for a human player to interact with the game and play it.

Use arrow keys for movement.

Have fun, and DFTBA!

## Task List
List of features and algorithms to implement:
- [x] Human Player
- [ ] Random path
- [ ] BFS
- [ ] DFS (recursive)
- [ ] DFS (iterative)
- [ ] Dijkstra
- [ ] A*
- [ ] Neural Network
- [ ] Monte Carlo
- [ ] Genetic algorithm   