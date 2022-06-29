def get_multiplier(c_rate = 0, c_dmg = 200, atk=1, dmg=1, kbw=False):    
    c_rate = c_rate / 100
    if c_rate > 1:
        c_rate = 1
    if c_rate < 0:
        raise ValueError("Crit must be non-negative.")

    c_dmg = c_dmg/100

    multiplier = ((c_rate * c_dmg) + ((1-c_rate) * 1)) 

    #dps after kbw penalty: 20% less damage 10% of the time
    #IMPORTANT: kbw bool is only for the penalty. c_dmg input should be adjusted to include kbw bonus
    #See final_dps in dps.py line 28
    if kbw == True:
        multiplier = (multiplier*.9) + (multiplier*.8*.1)

    multiplier *= atk * dmg

    return round(multiplier, 3)   