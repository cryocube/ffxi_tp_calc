#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
# Input Resource                                        #
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
import argparse
#
#
#########################################################
#                                                       #
# Command line Flag Construction                        #
#                                                       #
#########################################################
#
def getArgs(argv=None):
    parser = argparse.ArgumentParser(
        description = 'Automates math behind Store TP and Swings to Weaponskills.',
        epilog = 'Last Updated: 20170316'
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
    args = parser.parse_args(argv)
    print(args)
    return parser.parse_args(argv)

