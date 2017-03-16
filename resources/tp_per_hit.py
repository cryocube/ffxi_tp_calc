#!/usr/bin/python3
#########################################################
#                                                       #
# TP Calculation Tool                                   #
# TP Per Hit Resource                                   #
#                                                       #
# Written by: Wyrd                                      #
#                                                       #
#########################################################
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
from decimal import *
#
#
#########################################################
#                                                       #
# Functions                                             #
#                                                       #
#########################################################
#
def core_calc(base,d_mult,floor,stp,delay,delay_diff):
    base_tp = floor + ((delay-delay_diff)* d_mult) / base
    stp_mod = (100 + stp) / 100
    tp_per_hit = base_tp * stp_mod
    print("Should be 127 unrounded TP = {}".format(tp_per_hit))
    return tp_per_hit
#
#
def final_calc(tp_rate):
    context = Context(prec=3, rounding=ROUND_DOWN)
    tp = context.create_decimal_from_float(tp_rate)
    return tp
