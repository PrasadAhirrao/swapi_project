# 1. TODO import all resource classes here
# 2. TODO get count of each resource
# 3. TODO get "singular" resource urls of each resource
# 4. TODO pull data from random 3 "singular" resource URLs
# 5. TODO convert swapi project into CLI application
# task1 task2 task3

import argparse
from utils.fetch_data import fetch_data
from resources.characters import Characters
from resources.species import Species
from resources.planets import Planets
from resources.vehicles import Vehicles
from resources.starships import Starships
from resources.films import Films

"""
if __name__ == '__main__':
    char = Characters()
    char_count_dict = char.get_count()
    print(f'Characters count {char_count_dict.get("count")}')
    print(f'Resource URL of People {char.get_resource_urls()}')
    print(f'Three random urls of people {char.get_random_url()}')
    print(fetch_data(char.get_random_url()))
    print('---------' * 25)

    film = Films()
    film_count_dict = film.get_count()
    print(f'Films count {film_count_dict.get("count")}')
    print(f'Resource URL of Films {film.get_resource_urls()}')
    print(f'Three random urls of Films {film.get_random_url()}')
    print(fetch_data(film.get_random_url()))
    print('---------' * 25)

    planet = Planets()
    pln_count_dict = planet.get_count()
    print(f'Planets count {pln_count_dict.get("count")}')
    print(f'Resource URL of Planets {planet.get_resource_urls()}')
    print(f'Three random urls of Planets {planet.get_random_url()}')
    print(fetch_data(planet.get_random_url()))
    print('---------' * 25)

    spec = Species()
    spec_count_dict = spec.get_count()
    print(f'Species count {spec_count_dict.get("count")}')
    print(f'Resource URL of Species {spec.get_resource_urls()}')
    print(f'Three random urls of Species {spec.get_random_url()}')
    print(fetch_data(spec.get_random_url()))
    print('---------' * 25)

    star = Starships()
    star_count_dict = star.get_count()
    print(f'Starships count {star_count_dict.get("count")}')
    print(f'Resource URL of Starships {star.get_resource_urls()}')
    print(f'Three random urls of Starships {star.get_random_url()}')
    # print(fetch_data(star.get_random_url()))
    print('---------' * 25)

    vehicle = Vehicles()
    veh_count_dict = vehicle.get_count()
    print(f'Vehicles count {veh_count_dict.get("count")}')
    print(f'Resource URL of Vehicles {vehicle.get_resource_urls()}')
    print(f'Three random urls of Vehicles {vehicle.get_random_url()}')
    # print(fetch_data(vehicle.get_random_url()))
"""

if __name__ == '__main__':
    char = Characters()
    char_count_dict = char.get_count()
    film = Films()
    film_count_dict = film.get_count()
    planet = Planets()
    pln_count_dict = planet.get_count()
    spec = Species()
    spec_count_dict = spec.get_count()
    star = Starships()
    star_count_dict = star.get_count()
    vehicle = Vehicles()
    veh_count_dict = vehicle.get_count()

    parser = argparse.ArgumentParser(description='running code of taskthree')
    parser.add_argument('dev1', type=str, choices='count')
    parser.add_argument('dev2', type=str, choices='url')

    args = parser.parse_args()

    if args.dev1 == 'count':
        print(f"count of peoples - {char_count_dict.get(args.dev1)}")
        print(f"count of films - {film_count_dict.get(args.dev1)}")
        print(f"count of planets - {pln_count_dict.get(args.dev1)}")
        print(f"count of species - {spec_count_dict.get(args.dev1)}")
        print(f"count of starships - {star_count_dict.get(args.dev1)}")
        print(f"count of vehicles - {veh_count_dict.get(args.dev1)}")
    else:
        print('ERROR: please choose correct argument')

    if args.dev2 == 'url':
        print(f'Resource URL of People {char.get_resource_urls()}')
        print(f'Three random urls of people {char.get_random_url()}')
        print(fetch_data(char.get_random_url()))
        print('---------' * 20)

        print(f'Resource URL of Films {film.get_resource_urls()}')
        print(f'Three random urls of Films {film.get_random_url()}')
        print(fetch_data(film.get_random_url()))
        print('---------' * 20)

        print(f'Resource URL of Planets {planet.get_resource_urls()}')
        print(f'Three random urls of Planets {planet.get_random_url()}')
        print(fetch_data(planet.get_random_url()))
        print('---------' * 20)

        print(f'Resource URL of Species {spec.get_resource_urls()}')
        print(f'Three random urls of Species {spec.get_random_url()}')
        print(fetch_data(spec.get_random_url()))
        print('---------' * 20)

        print(f'Resource URL of Starships {star.get_resource_urls()}')
        print(f'Three random urls of Starships {star.get_random_url()}')
        # print(fetch_data(star.get_random_url()))
        print('---------' * 20)

        print(f'Resource URL of Vehicles {vehicle.get_resource_urls()}')
        print(f'Three random urls of Vehicles {vehicle.get_random_url()}')
        # print(fetch_data(vehicle.get_random_url()))
    else:
        print('ERROR: please choose correct argument')

