# pydantic modules
from models.datamodels.characters import Characters as Char
from models.datamodels.films import Films as Film
from models.datamodels.planets import Planets as Plan
from models.datamodels.species import Species as Spec
from models.datamodels.starships import Starships as Star
from models.datamodels.vehicles import Vehicles as Vehi

# resource classes
from resources.characters import Characters
from resources.films import Films
from resources.planets import Planets
from resources.species import Species
from resources.vehicles import Vehicles
from resources.starships import Starships

if __name__ == "__main__":

    character_data = Characters().get_sample_data()
    character_data = Char(**character_data)

    breakpoint()
    film_data = Films().get_sample_data()
    film_data = Film(**film_data)

    planet_data = Planets().get_sample_data()
    planet_data = Plan(**planet_data)

    species_data = Species().get_sample_data()
    species_data = Spec(**species_data)

    starship_data = Starships().get_sample_data()
    starship_data = Star(**starship_data)

    vehicle_data = Vehicles().get_sample_data()
    vehicle_data = Vehi(**vehicle_data)