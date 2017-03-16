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
# Imports / Includes                                    #
#                                                       #
#########################################################
#
#
from resources.build_args import *
from resources.delay import *
from resources.stp_calc import *
from resources.tp_per_hit import *
from resources.result import *
import argparse
import math
from decimal import *
#
#
#########################################################
#                                                       #
# Defined Functions                                     #
#                                                       #
#########################################################
#
#
def main():
    args = getArgs()
    print("Main has received {}".format(args))
    print("dw _lvl is {}".format(dw_lvl))
    delay = delay_calc(args.delay,args.off,dw_lvl,args.h2h,args.d_red,args.ma,ma_lvl,args.dw,args.dw_x)
    print("Main determined Delay {}".format(delay))
    traits = select_traits(delay,equa_components)
    jt_stp = jt_conv(args.jt_stp, stp_jt_lvl)
    stp = tot_stp(jt_stp, args.merits, args.kakka, args.gear_stp, args.food_stp)
    print("Main STP is {}".format(stp))
    tp_rate = core_calc(traits[2],traits[1],traits[3],stp,delay,traits[0])
    tp = final_calc(tp_rate)
    result(args.dw,args.ma,tp)
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
if __name__ == "__main__":
    main()
