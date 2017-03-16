#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
# Delay Resource                                        #
#                                                       #
# Written by: Wyrd                                      #
#                                                       #
#########################################################
#
#
#########################################################
#                                                       #
# Functions                                             #
#                                                       #
#########################################################
#
def result(dw,ma,tp):
    if dw >=1:
        atk_round = tp*2
        build = 1000/atk_round
        print("Dual wield TP per hit is : {}".format(tp))
        print("Dual Wield TP per attack round is : {}".format(atk_round))
        print("Attack Rounds to 1000 TP Weapon Skill is : {}".format(build))
        quit()
    elif ma >=1:
        print("ROFL")
        quit()
    else:
        build = 1000/tp
        print("TP per hit is : {}".format(tp))
        print("This is a {} hit build.".format(build))
        quit()
