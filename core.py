#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:44:46 2020

@author: Will Anthony
@date: APR 2020

Basic gameplay functionality and core tools
"""

import random
import rules


## roll_dice function
#
# args: number of dice to roll
#
# returns: a new dice 'hand' of the desired number 
#
def roll_dice(number_of_dice):
    
    dice_roll = []
    for i in range(number_of_dice):
        dice_roll.append(random.choice(rules.dice_faces))
    
    return dice_roll

## roll_off function
#
# used to determine the order of players on game start
#
# returns: order of players
#

## reroll_function
#
# used to keep certain dice, and reroll the rest
#
# args: current hand (list), dice to re-roll by position (list)
#
# returns: the total hand (kept dice with rerolled dice)
def reroll_dice(current_hand, reroll_positions):
    new_hand = []
    new_dice = roll_dice(len(reroll_positions))
    
    # copy current hand to new hand unless position is in reroll_positions then replace with reroll
    
        
    return new_hand

class Game:

    player_list = []
    
    def __init__(self, gameserial):
        self.serial = gameserial
        self.player_list = []
        
    def PlayerCount(self):
        return len(self.player_list)    #FIXME this doesn't return number of players in the game


class Player:
      
    #chosen monster
    
    #player position relative to other players in the circle
    player_postition = 0
    
    #amount of energy a player has
    player_energy = 0
    
    #amount of health a player has, game starts with 10
    player_health = 0
    
    #number of points a player has
    player_points = 0
    
    def __init__(self, player_name):
        self.name = player_name
        self.player_health = 10
        self.player_energy = 0
        self.player_points = 0
        

def main():
    print("you are currently dans le main")
 
    print(roll_dice(6))
    
    p1 = Player('Will')
    p2 = Player('Ed')

    game1 = Game(1)
    
    game1.player_list.append(p1)
    
    #print(game1.player_list)

    this_diceroll = roll_dice(6)
    
    second_diceroll = reroll_dice(this_diceroll, [1,2,3])
    
    
    
 
if __name__=="__main__":
    main()