#!/usr/bin/env python

## http://tetris.wikia.com/wiki/Tetris_Guideline
## http://stackoverflow.com/questions/1969005/enumerations-in-python (Objects with functionality)

# Useful modules
import sys
# PyGame
import pygame
from pygame.locals import *
# Classes
from pieces import *
from game import *
from config import *

def process_input(event, block):
    # TODO do some refactoring and get rid of this 'global'
    global MOVE_TICKER

    if MOVE_TICKER == 0:
        MOVE_TICKER = MOVE_TICKER_DEFAULT

        # If a key was pressed, check that the piece can move
        # in the specified direction, and move it accordingly
        if (event.type == KEYDOWN):
            if event.key == pygame.K_LEFT:
                if block.can_move(LEFT):
                    block.move(LEFT)
            elif event.key == pygame.K_RIGHT:
                if block.can_move(RIGHT):
                    block.move(RIGHT)
            elif event.key == pygame.K_DOWN:
                if block.can_move(DOWN):
                    block.move(DOWN)
            elif event.key == pygame.K_UP:
                block.rotate()
        # Either way (at each turn), move the block down once
        block.move(DOWN)

    elif MOVE_TICKER > 0:
        MOVE_TICKER -= 1

def main():
    # TODO do some refactoring and get rid of this 'global'
    global MOVE_TICKER

    # Initialise the game engine
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode(W_SIZE)
    pygame.display.set_caption("Tetris")

    # Create clock
    clock = pygame.time.Clock()

    # Create the Game
    game = Game()
    block = Block()
    # block = BlockO()

    while True:
        # Lock the game at default fps
        clock.tick(FPS)

        # Clear the screen
        screen.fill(WHITE)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # If the piece has reached the bottom or the top of the stack of pieces
        if block.has_finished(game):
            # Merge it with current game state
            game.merge(block)
            # Spawn a new piece
            block = Block()
        # If not, process the keyboard input and move accordingly
        else:
            process_input(event, block)

        # Draw game to screen
        game.draw(screen)
        block.draw(screen)

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()


