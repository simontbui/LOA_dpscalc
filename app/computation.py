def get_multiplier(atk=1, dmg=1, c_rate = 0, c_dmg = 200, kbw=False):    
    c_rate = c_rate / 100
    if c_rate > 1:
        c_rate = 1

    c_dmg = c_dmg/100

    multiplier = ((c_rate * c_dmg) + ((1-c_rate) * 1)) 

    #dps after kbw penalty: 20% less damage 10% of the time
    if kbw == True:
        multiplier = (multiplier*.9) + (multiplier*.8*.1)

    multiplier *= atk * dmg

    return round(multiplier, 3)   