from maths.engravings import engrav_dict
from maths.computation import get_multiplier

class final_dps:
    def __init__ (self, engravings=[], engrav_lvl=[], c_rate=0, c_dmg=200, damage=1):
        self.engrav = [x for x in engravings if x != "---"]
        self.engrav_lvl = engrav_lvl[0: len(self.engrav)]

        #final stat values used in computation
        self.c_rate = c_rate 
        self.c_dmg = c_dmg
        self.damage = damage
        self.atk = 1

        #final output variable
        self.multiplier = 0

        #xtracting & adding engraving bonuses to the 4 final stat values
        kbw = False
        for i in range(len(self.engrav)):
            engrav = self.engrav[i]
            if engrav == 'Keen Blunt Weapon':
                kbw = True
            engrav_lvl = self.engrav_lvl[i]
            bonus = engrav_dict[engrav][engrav_lvl]
            
            self.c_rate += bonus['Crit']
            self.c_dmg += bonus['Crit_Dmg']
            self.atk += bonus['Atk'] / 100
            if bonus['Dmg'] != 0:
                self.damage *= 1 + (bonus['Dmg'] / 100)

        #print(self.c_rate, self.c_dmg, self.atk, self.damage, kbw)
        self.multiplier = get_multiplier(c_rate=self.c_rate, c_dmg=self.c_dmg,
                                         atk=self.atk, dmg=self.damage, kbw=kbw)

#print(final_dps("Cursed Doll", "Grudge", engrav1_lvl=3, engrav2_lvl=2, c_rate=60).multiplier)
