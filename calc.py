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
parser.add_argument('--dw', default=0, help='Dual Wield Level',type=int)
parser.add_argument('--off', default=0, help='Delay of Off Hand Weapon', type=int)
parser.add_argument('--d_red', default=0, help='Delay Reduction Modifier', type=int)
parser.add_argument('--h2h', action='store_true', help='Hand to Hand Flag')
parser.add_argument('--ma', default=0, help='Martial Arts Rank', type=int)
parser.add_argument('--dw_x', default=0, help='Extra Dual Wield Gain', type=int)
args = parser.parse_args()
print(args)
#
#
#########################################################
#                                                       #
# Variables                                             #
#                                                       #
#########################################################
#`
# Dictionary
stp_jt_lvl = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30}
dw_lvl = {1: 10, 2: 15, 3: 25, 4: 30, 5: 35, 6: 37}
ma_lvl = {1: 400, 2: 380, 3: 360, 4: 340, 5: 320, 6: 300, 7: 280, 8: 275, 9: 270}
#
# Dictionary
# (weapon_delay_diff, delay_multiplier, base_sel, floor)
equa_components = [(180, 63, 360, 61),(180, 88, 360, 61),(540, 20, 360, 149),(630, 28, 360, 154),(720, 24, 360,
161),(900, 28, 360, 173)]
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
def select_traits(delay,equa_components):
    if int(delay) <= 180:
        return equa_components[0]
    elif int(delay) <= 540:
        return equa_components[1]
    elif int(delay) <= 630:
        return equa_conponents[2]
    elif int(delay) <= 720:
        return equa_components[3]
    elif int(delay) <= 900:
        return equa_components[4]
    else:
        return equa_components[5]
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
#
def delay_calc(main_delay,off_delay,dw_lvl,h2h,d_red,ma,ma_lvl,dw,dw_x):
    if dw >=1 and h2h == True:
            print("Invalid Mode Selections.  Cannot be both Dual Wield and Hand to Hand.")
            quit()
    elif dw >=1:
        dw_red = ((dw_lvl.get(dw,0))+dw_x)
        delay = ((main_delay+off_delay)*(1-((d_red+dw_red)/100)))/2
        print(delay)
        cap = (main_delay+off_delay)*float(.2)
        if delay >= cap:
            return delay
        else:
            print('Delay is capped at .2 of Main and off added...you monster')
            return cap
    elif h2h == True:
        delay = ((ma_lvl.get(ma, 0))-d_red)
        if delay >=96:
            return delay
        else:
            print('Hand to Hand delay caps at 96')
            return int(96)
    else:
        delay = main_delay*(1-(d_red/100))
        cap = (main_delay*int(.2))
        if delay >= cap:
            return delay
        else:
            print('Delay is capped at .2 of Main...you monster')
            return cap
#
#
def core_calc(base,d_mult,floor,stp,delay,delay_diff):
    base_tp = floor + ((delay-delay_diff)* d_mult) / base
    stp_mod = (100 + stp) / 100
    tp_per_hit = base_tp * stp_mod
    print("Should be 127 unrounded TP = {}".format(tp_per_hit))
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
delay = delay_calc(args.delay,args.off,dw_lvl,args.h2h,args.d_red,args.ma,ma_lvl,args.dw,args.dw_x)
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
jt_stp = jt_conv(args.jt_stp, stp_jt_lvl)
print("Job Trait Store TP = {}".format(jt_stp))
stp = tot_stp(jt_stp, args.merits, args.kakka, args.gear_stp, args.food_stp)
print("Total Store TP = {}".format(stp))
tp_rate = core_calc(base, d_mult,floor, stp, delay,delay_diff)
print("Unmodified tp rate is "+str(tp_rate))
context = Context(prec=3, rounding=ROUND_DOWN)
tp_rate = context.create_decimal_from_float(tp_rate)
# move this into a defined function to know the difference between attack rounds for dw/h2h and hits for 2h
print("TP per swing is {}".format(tp_rate))
build = 1000/tp_rate
print("This is a {} attack round build".format(build))
