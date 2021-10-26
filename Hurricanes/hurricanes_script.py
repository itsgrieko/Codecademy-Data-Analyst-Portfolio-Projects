# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
def update_damage(dmg_lst):
    """Returns damages list converted to floats"""
    updated_damages = []
    for item in dmg_lst:
        if item[-1] == 'B':
            updated_damages.append(float(item[:-1]) * 10**9)
        elif item[-1] == 'M':
            updated_damages.append(float(item[:-1]) * 10**6)
        else:
            updated_damages.append(item)
    return updated_damages


updated_damages = update_damage(damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dict(names, months, years, winds, areas, damages, deaths):
    """Returns dictionary of all hurricane info."""
    hurricane_stats = {}
    for i in range(0, len(names)):
        hurricane_stats[names[i]] = {'Name': names[i],
                                     'Month': months[i],
                                     'Year': years[i],
                                     'Max Sustained Wind': winds[i],
                                     'Areas Affected': areas[i],
                                     'Damage': damages[i],
                                     'Deaths': deaths[i]}
    return hurricane_stats


hurricanes = construct_hurricane_dict(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# print(hurricanes)

#test = 'Florida' in hurricanes['Cuba I']['Areas Affected']
# print(test)

# write your construct hurricane by year dictionary function here:


def construct_years_dict(hurricanes):
    """Returns dictionary of hurricanes sorted by year."""
    years_dict = {}
    for hurricane in hurricanes:
        current_year = hurricanes[hurricane]['Year']
        if current_year not in years_dict:
            years_dict[current_year] = [hurricanes[hurricane]]
        else:
            years_dict[current_year].append(hurricanes[hurricane])
    return years_dict


construct_years_dict(hurricanes)


# write your count affected areas function here:
def count_areas(hurricanes):
    """Returns dictionary of how many times an area has been hit by a hurricane."""
    areas = {}
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]['Areas Affected']:
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
    return areas


areas_counted = count_areas(hurricanes)

# write your find most affected area function here:


def find_most_affected_area(affected):
    """Returns the most affected area, and the number of occurences."""
    most_affected_count = 0
    most_affected_area = []
    for area in affected:
        if affected[area] > most_affected_count:
            most_affected_count = affected[area]
            most_affected_area = [area]
        elif affected[area] == most_affected_count:
            most_affected_area.append(area)
    return most_affected_area, most_affected_count


print('Most affected area is:', find_most_affected_area(areas_counted))

# write your greatest number of deaths function here:


def find_most_deaths(hurricanes):
    """Returns which hurricane caused the most deaths, and the number."""
    death_count = 0
    most_death = []
    for hurricane in hurricanes:
        current_deaths = hurricanes[hurricane]['Deaths']
        if current_deaths > death_count:
            death_count = current_deaths
            most_death = [hurricane]
        elif current_deaths == death_count:
            most_death.append(hurricane)
    return most_death, death_count


print('Most deaths were:', find_most_deaths(hurricanes))


# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


def categorize_mortality(hurricanes):
    """Returns a dictionary of each hurricane categorized by its mortality scale."""
    mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        deaths = hurricanes[hurricane]['Deaths']
        current_cane = hurricanes[hurricane]
        if deaths == 0:
            mortality[0].append(current_cane)
        elif deaths < mortality_scale[1]:
            mortality[1].append(current_cane)
        elif deaths < mortality_scale[2]:
            mortality[2].append(current_cane)
        elif deaths < mortality_scale[3]:
            mortality[3].append(current_cane)
        elif deaths < mortality_scale[4]:
            mortality[4].append(current_cane)
        else:
            mortality[5].append(current_cane)
    print(mortality[4])


categorize_mortality(hurricanes)

# write your greatest damage function here:


def find_most_cost(hurricanes):
    """Returns the costliest hurricane, and its cost."""
    cost_count = 0
    most_cost = []
    for hurricane in hurricanes:
        current_cost = hurricanes[hurricane]['Damage']
        if type(current_cost) != str:
            if current_cost > cost_count:
                cost_count = current_cost
                most_cost = [hurricane]
            elif current_cost == cost_count:
                most_cost.append(hurricane)
    return most_cost, cost_count


print('Highest cost was:', find_most_cost(hurricanes))

# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def categorize_damage(hurricanes):
    """Returns a dictionary of each hurricane, categorized by cost."""
    damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricanes:
        current_damage = hurricanes[hurricane]['Damage']
        current_cane = hurricanes[hurricane]
        if type(current_damage) is not str:
            if current_damage < damage_scale[1]:
                damage[1].append(current_cane)
            elif current_damage < damage_scale[2]:
                damage[2].append(current_cane)
            elif current_damage < damage_scale[3]:
                damage[3].append(current_cane)
            elif current_damage < damage_scale[4]:
                damage[4].append(current_cane)
            else:
                damage[5].append(current_cane)
        else:
            damage[0].append(current_cane)
    return damage


categorized_damages = categorize_damage(hurricanes)

print(categorized_damages[5])
