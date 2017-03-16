#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
# Store TP Resource                                     #
#                                                       #
# Written by: Wyrd                                      #
#                                                       #
#########################################################
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
equa_components = [(180, 63, 360, 61),(180, 88, 360, 61),(540, 20, 360, 149),(630, 28, 360, 154),(720, 24, 360,
161),(900, 28, 360, 173)]
#
traits = list()
#
#
#########################################################
#                                                       #
# Functions                                             #
#                                                       #
#########################################################
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
