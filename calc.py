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
from decimal import *
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
parser.add_argument('--delay', required=True, help='Weapon Delay of Main weapon', type=int)
parser.add_argument('--jt_stp', default=0, help='Store TP Rank', type=int)
parser.add_argument('--gear_stp', default=0, help='Store TP from Gear', type=int)
parser.add_argument('--merits', default=0, help='Number of Store TP Merits', type=int)
parser.add_argument('--kakka', action='store_true', help='Using Kakka:Ichi with a Ninja Subjob')
parser.add_argument('--food_stp', default=0, help='Store TP gained from food', type=int)
parser.add_argument('--dw', default=0, help='Dual Wielding - Enter the Delay of the Offhand Weapon', type=int)
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
main_delay = args.delay
off_delay = args.dw
jt_stp_lvl = args.jt_stp
merit_stp_lvl = args.merits
kakka = args.kakka
gear_stp = args.gear_stp
fstp = args.food_stp
#
# Dictionary
stp_jt = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30}
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
#
#
#
def select_traits(delay,equa_components):
    if int(delay) <= 180:
        return equa_components[0]
    elif int(delay) <= 450:
        return equa_components[1]
    elif int(delay) <= 480:
        return equa_conponents[2]
    elif int(delay) <= 530:
        return equa_components[3]
    else:
        return equa_components[4]
#
#
def jt_conv(jt_stp_lvl,stp_jt):   
    return stp_jt.get(jt_stp_lvl, 0)
#
#
def tot_stp(jt_stp,merit_stp_lvl,kakka,gear_stp,fstp):
    if kakka is True:
        bonus = (merit_stp_lvl*2)+jt_stp+10+gear_stp+fstp
        return bonus
    else:
        bonus = (merit_stp_lvl*2)+jt_stp+gear_stp+fstp
        return bonus
#
#
def delay_calc(main_delay,delay_diff,off_delay):
    return (main_delay+off_delay)-delay_diff
#
#
def core_calc(base,d_mult,floor,stp,delay):
    base_tp = floor + (delay * d_mult) / base
    stp_mod = (100 + stp) / 100
    tp_per_hit = base_tp * stp_mod
    print("Should be 14.375 unrounded TP = {}".format(tp_per_hit)) #14.375
    return tp_per_hit
#
#
#########################################################
#                                                       #
# Main Program                                          #
#                                                       #
# Remember: print(type(variable))                       #
#                                                       #
#########################################################
#
#
delay = main_delay+off_delay
traits = select_traits(delay,equa_components)
print(traits)
base = traits[2]
delay_diff = traits[0]
d_mult = traits[1]
floor = traits[3]
print("Base = {}".format(traits[2]))
print("Delay = {}".format(traits[0]))
print("Delay Multiplier = {}".format(traits[1]))
print("Floor = {}".format(traits[3]))
delay = delay_calc(main_delay,delay_diff,off_delay)
jt_stp = jt_conv(jt_stp_lvl, stp_jt)
print("Job Trait Store TP = {}".format(jt_stp))
stp = tot_stp(jt_stp, merit_stp_lvl, kakka, gear_stp, fstp)
print("Total Store TP = {}".format(stp))
tp_rate = core_calc(base, d_mult, floor, stp, delay)
context = Context(prec=3, rounding=ROUND_DOWN)
tp_rate  = context.create_decimal_from_float(tp_rate)
print("TP per swing is {}".format(tp_rate))
build = 1000/tp_rate
print("This is a {}-hit Build".format(build))
