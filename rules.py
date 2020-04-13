#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:06:45 2020

@author: Will Anthony
@date: APR 2020

Rules and constants for the gameplay
"""

import os

# detect text files
file_list = [f for f in os.listdir(os.getcwd()) if f.endswith('.csv')]

dice_faces = ('fist', 'energy', 'heart', 3, 2, 1)

monster_names = ('Alienoid','Space Penguin','The King','Gigazaur','Cyber Kitty','Mecha Dragon')

MAX_PLAYERS = 6

def main():
    print("you are currently dans le main")
    
if __name__=="__main__":
    main()