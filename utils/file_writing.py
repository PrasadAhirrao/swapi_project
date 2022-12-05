from typing import Dict
from utils.timing import timeit

@timeit
def file_writing_func(film_data: Dict, file_name: str):
    """function to write film1 data into file"""
    with open(file_name, 'w') as file_obj:
        print('writing data into file')
        file_obj.write(str(film_data))
