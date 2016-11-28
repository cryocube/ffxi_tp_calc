#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
#                                                       #
# Written by: Wyrd                                      #
#                                                       #
#########################################################
#
#
#
#########################################################
#                                                       #
# Imports                                               #
#                                                       #
#########################################################
#
#
import math
import argparse
#
#
#########################################################
#                                                       #
# Command line Flag Construction                        #
#                                                       #
#########################################################
#
parser = argparse.ArgumentParser(
    description = 'Automates math behind Store TP and Swings to Weaponskills.',
    epilog = 'Last Updated: 20161126'
    )
parser.add_argument('--delay', required=True, help='Weapon Delay of main weapon')
parser.add_argument('--ja_stp', default=0, help='Store TP Rank')
parser.add_argument('--gear_stp', help='Store TP from Gear')
args = parser.parse_args()
print(args)
#
#
#########################################################
#                                                       #
# Variables                                             #
#                                                       #
#########################################################
#
# Variables
# str(args.name)
weapon_delay = args.delay
ja_stp_lvl = int()
merit_stp_lvl = int()
gear_haste = int()
delay = float()
d_mult = float()
base = float()
floor = float()
tp_rate = float()
#
# Tuples
stp_ja = [(1,10), (2,15), (3,20), (4,25), (5,30)]
# 
# Dictionary
# (weapon_delay_diff, delay_multiplier, base_sel, floor,)
equa_components = [(180, 1.5, 180, 5),(180, 6.5, 270, 5),(450, 1.5, 30, 11.5),(480, 1.5, 50, 13),(530, 3.5, 470, 14.5)]
#
#########################################################
#                                                       #
# Defined Functions                                     #
#                                                       #
#########################################################
#
# THOUGHT: create a list of lists (dictionary?) to condence all below checks into a single function
#
#
def delay_calc(weapon_delay):
    if weapon_delay <= 450:
        equation = int(weapon_delay) - 180
        return equation
    elif weapon_delay <= 480:
        equation = int(weapon_delay) - 450
        return equation
    elif weapon_delay <= 530:
        equation = int(weapon_delay) - 480
        return equation
    else:
        equation = int(weapon_delay) - 530
        return equation
#
#
def delay_multiplier(weapon_delay):
    if weapon_delay <= 180:
        return float(1.5)
    elif weapon_delay <= 450:
        return float(6.5)
    elif weapon_delay <= 530:
        return float(1.5)    
    else:
        return float(3.5)
#
#
def base_sel(weapon_delay):
    if weapon_delay <= 180:
        return 180
    elif weapon_delay <= 450:
        return 270
    elif weapon_delay <= 480:
        return 30
    elif weapon_delay <= 530:
        return 50
    else:
        return 470
#
#
def floor_sel(weapon_delay):
    if weapon_delay <= 450:
        return float(5)
    elif weapon_delay <= 480:
        return float(11.5)
    elif weapon_delay <= 530:
        return float(13)
    else:
        return float(14.5)
#
#
def core_calc(base,d_mult,delay,floor):
    tp_per_hit = float((floor+((delay*d_mult)/base)))
    return math.floor(float(tp_per_hit))
#
#
#########################################################
#                                                       #
# Main Program                                          #
#                                                       #
#########################################################
#
#
base = base_sel(weapon_delay)
delay = delay_calc(weapon_delay)
d_mult = delay_multiplier(weapon_delay)
floor = floor_sel(weapon_delay)
tp_rate = core_calc(base,d_mult,delay,floor)
print("Base = "+str(base))
print("Delay = "+str(delay))
print("Delay Multiplier = "+str(d_mult))
print("Floor = "+str(floor))
print("TP per swing is "+str(tp_rate))

