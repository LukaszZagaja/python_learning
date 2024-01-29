# new_dict = {new_key:new_value for item in iterable}
# new_dict = {new_key:new_value for (key,value) in dict.items()}  ---- creating dict from other dict/just copying
# can also use conditionals (if/else)
#new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

import random
city_names = ['Paris', 'London', 'Berling', 'Washington', 'Warsaw']
city_temp = {city:random.randint(20,30) for city in city_names}
print(city_temp)


city_temp_over_25 = {city:temperature for (city,temperature) in city_temp.items() if temperature>=25}
print(city_temp_over_25)
