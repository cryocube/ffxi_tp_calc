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
# Variables                                             #
#                                                       #
#########################################################
#`
# Dictionary
dw_lvl = {1: 10, 2: 15, 3: 25, 4: 30, 5: 35, 6: 37}
ma_lvl = {1: 400, 2: 380, 3: 360, 4: 340, 5: 320, 6: 300, 7: 280, 8: 275, 9: 270}
#
#
#########################################################
#                                                       #
# Functions                                             #
#                                                       #
#########################################################
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
