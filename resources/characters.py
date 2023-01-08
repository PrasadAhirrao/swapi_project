from resources.base import ResourceBase
from utils.fetch_data import hit_url
from resources.base import RandomNumbers
from typing import List


class Characters(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = 'api/people'
        self.__character_range = [1, 82]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def character_range(self):
        return self.__character_range

    @character_range.setter
    def character_range(self, new_rang):
        self.__character_range = new_rang

    def get_count(self):
        r_url = self.relative_url
        plural_character_url = self.home_url + r_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result

    def get_random_url(self):
        random_url_list = []
        for i in RandomNumbers(1, 82):
            result = self.get_resource_urls() + '/' + str(i)
            random_url_list.append(result)
        return random_url_list

    def get_resource_urls(self):
        return self.home_url + self.relative_url

    def get_sample_data(self, id_=1):
        complete_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(complete_url)
        data = response.json()
        return data


if __name__ == '__main__':
    char = Characters()
    # print(char.get_resource_urls())
    # print(char.get_count())
    print(char.get_random_url())


