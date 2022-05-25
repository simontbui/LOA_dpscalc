def crit_dps(c_rate, c_dmg=200, kbw=0):
    #kbw c_dmg bonus at lvl=0,1,2,3
    kbw_bonus = [0, .1, .25, .5]

    c_rate = c_rate / 100
    if c_rate > 1:
        c_rate = 1

    c_dmg = (c_dmg/100) + kbw_bonus[kbw]

    dps = ((c_rate * c_dmg) + ((1-c_rate) * 1)) 

    #dps after kbw penalty: 20% less damage 10% of the time
    if kbw != 0:
        dps = (dps*.9) + (dps*.8*.1)

    return round(dps, 3)

#test runs
print(crit_dps(50))
