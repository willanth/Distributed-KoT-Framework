# -*- coding: utf-8 -*-
"""
WANKoT Client 

@author Will Anthony
@date APR 2020

About this software:
    
    Wide-Area-Network King of Tokyo (WANKoT) is a framework for the play of 
    the tabletop game "King of Tokyo".  It seeks to respect all original 
    gameplay rules and contents.
    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


# Detect location and find/build directory structure
print(os.path.dirname(os.path.realpath(__file__)))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())

#os.chdir('data')


def main():
    print("you are currently dans le main")
    
if __name__=="__main__":
    main()