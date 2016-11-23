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
# Variables                                             #
#                                                       #
#########################################################
#
# Variables
weapon_delay = int()
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
#########################################################
#                                                       #
# Defined Functions                                     #
#                                                       #
#########################################################
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
    return = math.floor(float(tp_per_hit))
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

