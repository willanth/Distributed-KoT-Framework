#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:44:46 2020

@author: Will Anthony
@date: APR 2020

Basic gameplay functionality and core tools

TODO: implement "type hinting" per
https://www.python.org/dev/peps/pep-0484/
https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

TODO: accountability logging to a game log CSV 
"""

import random
import rules
from typing import List, Set, Dict, Tuple, Optional


## roll_dice function
#
# args: number of dice to roll
#
# returns: a new dice 'hand' of the desired number 
#
def roll_dice(number_of_dice: int):
    
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
def roll_off(gameobj):
    
    # for number of players (upper bound set in rules) roll for each 
    for player in gameobj.player_list:
        roll = roll_dice(1)
        print(player.name +" rolls a: " + str(roll[0]))
    # announce which players need to roll off again
    
    # announce the winner
    return

## reroll_function
#
# used to keep certain dice, and reroll the rest
#
# args: current hand (list), dice to re-roll by position (list)
#
# returns: the total hand (kept dice with rerolled dice)
def reroll_dice(current_hand, reroll_positions):
    new_hand = []
    
    # copy current hand to new hand unless position is in reroll_positions then replace with reroll
    new_hand = current_hand
    for i, val in enumerate(new_hand):
        if i in reroll_positions:
            value = roll_dice(1)
            new_hand[i] = value[0]     
        
    return new_hand

class Game:

    player_list = []
    
    # game serial number to deconflicht concurrent gameplay, acts as seed for shared key
    serial = 0
    
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
    
    # list of cards the player holds
    player_cards = []
    
    def __init__(self, player_name):
        self.name = player_name
        self.player_health = 10
        self.player_energy = 0
        self.player_points = 0
        self.player_cards = []
        

def main():
    print("you are currently dans le main")
 
    print(roll_dice(6))
    
    p1 = Player('Will')
    p2 = Player('Ed')

    game1 = Game(1)
    
    game1.player_list.append(p1)
    game1.player_list.append(p2)    
    
    print(game1.PlayerCount())

    this_diceroll = roll_dice(6)
    print(this_diceroll)
    
    second_diceroll = reroll_dice(this_diceroll, [1,2,3])
    
    print(second_diceroll)
    
    roll_off(game1)
    
    
 
if __name__=="__main__":
    main()