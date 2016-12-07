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
ja_stp_lvl = args.ja_stp
merit_stp_lvl = int()
gear_haste = int()
delay = float()
d_mult = float()
base = float()
floor = float()
tp_rate = float()
ja_stp = int()
#
# Dictionary
stp_ja = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30}
# 
# Dictionary
# (weapon_delay_diff, delay_multiplier, base_sel, floor,)
equa_components = [(180, 1.5, 180, 5),(180, 6.5, 270, 5),(450, 1.5, 30, 11.5),(480, 1.5, 50, 13),(530, 3.5, 470, 14.5)]
traits = list()
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
def select_traits(weapon_delay,equa_components):
    if int(weapon_delay) <= 180:
        return equa_components[0]
    elif int(weapon_delay) <= 450:
        return equa_components[1]
    elif int(weapon_delay) <= 480:
        return equa_conponents[2]
    elif int(weapon_delay) <= 530:
        return equa_components[3]
    else:
        return equa_components[4]
#
#
def ja_conv(ja_stp_lvl,stp_ja):   
    return stp_ja.get(int(ja_stp_lvl), 0)
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
traits = select_traits(weapon_delay,equa_components)
print(traits)
base = traits[2]
delay = traits[0]
d_mult = traits[1]
floor = traits[3]
#tp_rate = core_calc(base,d_mult,delay,floor)
print("Base = "+str(base))
print("Delay = "+str(delay))
print("Delay Multiplier = "+str(d_mult))
print("Floor = "+str(floor))
#print("TP per swing is "+str(tp_rate))
ja_stp = ja_conv(ja_stp_lvl,stp_ja)
print(ja_stp)
