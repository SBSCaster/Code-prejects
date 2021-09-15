# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico',
         'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 
         'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 
         'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'
         ]

# months of hurricanes
months = ['October', 'September', 'September', 
          'November', 'August', 'September', 'September', 
          'September', 'September', 'September', 
          'September', 'October', 'September', 'August', 
          'September', 'September', 'August', 'August', 
          'September', 'September', 'August', 'October', 
          'September', 'September', 'July', 'August', 
          'September', 'October', 'August', 'September', 
          'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 
         1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 
         2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 
                       160, 160, 175, 175, 160, 160, 175, 
                       160, 175, 175, 190, 185, 160, 175, 
                       180, 165, 165, 160, 175, 180, 185, 
                       175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
                  ['The Bahamas', 'Northeastern United States'], 
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], 
                  ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
                  ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], 
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', 
           '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', 
           '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', 
           '64.8B', '91.6B', '25.1B']
# deaths for each hurricane
deaths = [90,4000,16,3103,179,
          184,408,682,5,1023,43,
          319,688,259,37,11,2068,
          269,318,107,65,19325,51,
          124,17,1836,125,87,45,133,
          603,138,3057,74]

# write your update damages function here:
def update_damages(damage_list):
    damages_updated = []
    for i in damage_list:
        num = i[:-1]
        if 'B' in i:
            damages_updated.append(float(num) * 100000000)
        elif 'M' in i:
            damages_updated.append(float(num) * 1000000)
        else:
            damages_updated.append(i)
    return damages_updated


damages = update_damages(damages)







# write your construct hurricane dictionary function here:
def hurricane_diction(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_dict = {}
    for i in range(len(names)):
        hurricane_dict[names[i]] = {"Name": names[i], 'Month': months[i], "Year": years[i], 
                                    'Max Wind': max_sustained_winds[i], 'Affected_Area': areas_affected[i], 
                                    'Damage': damages[i], "Deaths": deaths[i]}
    return hurricane_dict


hurricane_dictionary = hurricane_diction(names, months, years, max_sustained_winds, areas_affected, damages, deaths)







# write your construct hurricane by year dictionary function here:
def hurricane_year_diction(hurricane_dict, years):
    hurricane_year_dict = {}
    for year in years:
        values = []
        for cane in hurricane_dict.values():
            if year == cane['Year']:
                values.append(cane)
        hurricane_year_dict[year] = values
    return hurricane_year_dict

hurricane_year_dictionary = hurricane_year_diction(hurricane_dictionary, years)

# write your count affected areas function here:

def future_preperations(hurricane_dict, affected):
    areas_hit_dict = {}
    for areas in affected:
        for area in areas:
            hits = 0
            for cane in hurricane_dict.values():
                if area in cane["Affected_Area"]:
                    hits += 1
            areas_hit_dict[area] = hits
    return areas_hit_dict

how_many = future_preperations(hurricane_dictionary, areas_affected)













# write your find most affected area function here:
def most_affected(areas_hit):
    most_hit = ''
    how_often = 0
    for area in areas_hit.keys():
        if areas_hit[area] > how_often:
            how_often = areas_hit[area]
            most_hit = area
    winner = f"Most hit area is {most_hit}, which was hit {how_often} times!"
    return winner



print(most_affected(how_many))


# write your greatest number of deaths function here:
def most_kills(deaths, moabs):
    most_kills = 0
    killer_cane = ''
    for death in deaths:
        if death > most_kills:
            most_kills = death
    for moab in moabs.values():
        if moab['Deaths'] == most_kills:
            killer_cane = moab["Name"]
    return '{killer} has killed {most}. Wow.'.format(killer=killer_cane, most=most_kills)

deadly_cane = most_kills(deaths, hurricane_dictionary)



# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}



def rate_hurricanes(cane_dict, mscale):
    rated_canes = {}
    for rating in mscale.keys():
        value = []
        for cane in cane_dict.values():
            if cane['Deaths'] >= mscale[rating]:
                value.append(cane['Name'])
        rated_canes[rating] = value
    return rated_canes
    

rated_canes = rate_hurricanes(hurricane_dictionary, mortality_scale)






# write your greatest damage function here:
def greatest_damage(cane_dict):
    cost = 0
    most_damage = ''
    for cane in cane_dict.values():
        if cane['Damage'] != 'Damages not recorded':
            if float(cane['Damage']) > cost:
                cost = cane['Damage']
                most_damage = cane['Name'] 
           
    winner = f'Greatest cost in damages was ${cost}, and caused by {most_damage}!'
    return winner

deadlist_cane = greatest_damage(hurricane_dictionary)
print(deadlist_cane)





# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rating(cane_dict, dscale):
    rated_canes = {}
    for rating in dscale.keys():
        value = []
        for cane in cane_dict.values():
            if cane['Deaths'] >= dscale[rating]:
                value.append(cane['Name'])
        rated_canes[rating] = value
    return rated_canes






