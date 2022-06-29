engrav_list = [
    '---',
    'All Out Attack',
    'Adrenaline',
    'Barricade',
    'Cursed Doll',
    'Ether Predator',
    'Grudge',
    'Hit Master',
    'Increase Mass',
    'Keen Blunt Weapon',
    'Master Brawler',
    'Master of Ambush',
    "Master's Tenacity",
    'MP Efficiency Increase',
    'Precise Dagger',
    'Raid Captain',
    'Stabilized Status',
    'Super Charge'
]

#to retrieve bonuses of engraving @ certain level: engrav_dict['engraving'][level]
engrav_dict = {}
for engrav in engrav_list:
    engrav_dict[engrav] = []
    for i in range(4):
        engrav_dict[engrav].append({'Crit': 0, 'Crit_Dmg': 0, 'Atk': 0, 'Dmg': 0})

#All Out Attack bonuses
engrav_dict["All Out Attack"][1]['Dmg'] = 4
engrav_dict["All Out Attack"][2]['Dmg'] = 10
engrav_dict["All Out Attack"][3]['Dmg'] = 20

#Adrenaline bonuses
engrav_dict["Adrenaline"][1]['Crit'] = 5
engrav_dict["Adrenaline"][2]['Crit'] = 10
engrav_dict["Adrenaline"][3]['Crit'] = 15
engrav_dict["Adrenaline"][1]['Atk'] = 1.8
engrav_dict["Adrenaline"][2]['Atk'] = 3.6
engrav_dict["Adrenaline"][3]['Atk'] = 6

#Barricade bonuses
engrav_dict["Barricade"][1]['Dmg'] = 3
engrav_dict["Barricade"][2]['Dmg'] = 8
engrav_dict["Barricade"][3]['Dmg'] = 16

#Cursed Doll bonuses
engrav_dict["Cursed Doll"][1]['Atk'] = 3
engrav_dict["Cursed Doll"][2]['Atk'] = 8
engrav_dict["Cursed Doll"][3]['Atk'] = 16

#Ether Predator bonuses
engrav_dict["Ether Predator"][1]['Atk'] = 6
engrav_dict["Ether Predator"][2]['Atk'] = 9
engrav_dict["Ether Predator"][3]['Atk'] = 15

#Grudge bonuses
engrav_dict["Grudge"][1]['Dmg'] = 4
engrav_dict["Grudge"][2]['Dmg'] = 10
engrav_dict["Grudge"][3]['Dmg'] = 20

#Hit Master bonuses
engrav_dict["Hit Master"][1]['Dmg'] = 3
engrav_dict["Hit Master"][2]['Dmg'] = 8
engrav_dict["Hit Master"][3]['Dmg'] = 16

#Increase Mass bonuses
engrav_dict["Increase Mass"][1]['Atk'] = 4
engrav_dict["Increase Mass"][2]['Atk'] = 10
engrav_dict["Increase Mass"][3]['Atk'] = 18

#Keen Blunt Weapon bonuses
engrav_dict["Keen Blunt Weapon"][1]['Crit_Dmg'] = 10
engrav_dict["Keen Blunt Weapon"][2]['Crit_Dmg'] = 25
engrav_dict["Keen Blunt Weapon"][3]['Crit_Dmg'] = 50

#Master Brawler bonuses
engrav_dict["Master Brawler"][1]['Dmg'] = 5
engrav_dict["Master Brawler"][2]['Dmg'] = 12
engrav_dict["Master Brawler"][3]['Dmg'] = 25

#Master of Ambush bonuses
engrav_dict["Master of Ambush"][1]['Dmg'] = 5
engrav_dict["Master of Ambush"][2]['Dmg'] = 12
engrav_dict["Master of Ambush"][3]['Dmg'] = 25

#Master's Tenacity bonuses
engrav_dict["Master's Tenacity"][1]['Dmg'] = 3
engrav_dict["Master's Tenacity"][2]['Dmg'] = 8
engrav_dict["Master's Tenacity"][3]['Dmg'] = 16

#MP Efficiency Increase bonuses
engrav_dict["MP Efficiency Increase"][1]['Dmg'] = 3
engrav_dict["MP Efficiency Increase"][2]['Dmg'] = 6
engrav_dict["MP Efficiency Increase"][3]['Dmg'] = 12

#Precise Dagger bonuses
engrav_dict["Precise Dagger"][1]['Crit'] = 4
engrav_dict["Precise Dagger"][2]['Crit'] = 10
engrav_dict["Precise Dagger"][3]['Crit'] = 20
engrav_dict["Precise Dagger"][1]['Crit_Dmg'] = -12
engrav_dict["Precise Dagger"][2]['Crit_Dmg'] = -12
engrav_dict["Precise Dagger"][3]['Crit_Dmg'] = -12

#Stabilized Status bonuses
engrav_dict["Stabilized Status"][1]['Dmg'] = 3
engrav_dict["Stabilized Status"][2]['Dmg'] = 8
engrav_dict["Stabilized Status"][3]['Dmg'] = 16

#Super Charge bonuses
engrav_dict["Super Charge"][1]['Dmg'] = 4
engrav_dict["Super Charge"][2]['Dmg'] = 10
engrav_dict["Super Charge"][3]['Dmg'] = 20

###