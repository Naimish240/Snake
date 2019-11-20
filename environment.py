# Import statemtnts
import random
import curses
from curses import textpad

# Function to create food at random point on grid
def create(snake, box):
    food = False
    while not food:
        food = [random.randint(box[0][0] + 1, box[1][0] - 1), 
                random.randint(box[0][1] + 1, box[1][1] - 1)]        
        if food in snake:
            food = False
    return food

def score(scr, s, w):
    # Score tracking
    text = "Score: {}".format(s)    # Text for score
    scr.addstr(1, w // 2 - len(text), text) 

# Main body
def main(scr, agent):
    curses.curs_set(0)          # Turns blinking off
    h, w = scr.getmaxyx()       # Gets screen dimensions
    s = 0                       # Initial score
    box = [[3, 3], [h-3, w-3]]  # Box co-ordinates
    textpad.rectangle(scr,      # Draws box
                    box[0][0], 
                    box[0][1], 
                    box[1][0], 
                    box[1][1])  

    snake = [[h//2, w//2 + 1],  # Draws snake
             [h//2, w//2 + 0], 
             [h//2, w//2 - 1]]          
    
    if agent == 'H':
        scr.nodelay(1)          # Removes waiting
        scr.timeout(100)        # Refreshes every x ms
    
    dirn = curses.KEY_RIGHT     # Initial direction of snake is right

    for x, y in snake:          # Prints snake
        scr.addstr(x, y, '#')
    
    food = create(snake, box)   # Creates a food element
    scr.addstr(food[0], food[1], '*')

    score(scr, 0, w)            # Function call to print score

    while True:                 # While loop for game event
        key = scr.getch()       # Gets input from user

        # Updates direction of snake when user presses an arrow key
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            dirn = key

        # Logic to update snake head
        head =  snake[0]
        if dirn == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif dirn == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif dirn == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif dirn == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]

        # Insert new head and print
        snake.insert(0, new_head)
        scr.addstr(new_head[0], new_head[1], '#')
        
        # If food is eaten
        if snake[0] == food:
            s += 1              # Updates score
            score(scr, s, w)    # Prints score

            # Creates and prints new food
            food = create(snake, box)
            scr.addstr(food[0], food[1], '*')

            if agent == 'H':    # Human agent
                # Increase speed
                scr.timeout(100 - (len(snake)//3) % 90)

        # Food is not eaten
        else:
            scr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        # Game over conditions
        if (snake[0][0] in [box[0][0], box[1][0]] or 
        snake[0][1] in [box[0][1], box[1][1]] or 
        snake[0] in snake[1:]):
            scr.addstr(h//2, w//2, "Game Over!")
            scr.nodelay(0)
            scr.getch()
            break

curses.wrapper(main, 'R')