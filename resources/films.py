from resources.base import ResourceBase
from utils.fetch_data import hit_url
from resources.base import RandomNumbers
from typing import List


class Films(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = 'api/films'

    @property
    def relative_url(self):
        return self.__relative_url


    def get_count(self):
        r_url = self.relative_url
        plural_url = self.home_url + r_url
        response = hit_url(plural_url)
        result = response.json()
        return result

    def get_random_url(self):
        random_url_list = []
        for i in RandomNumbers(1, 7):
            result = self.get_resource_urls() + '/' + str(i)
            random_url_list.append(result)
        return random_url_list

    def get_resource_urls(self):
        return self.home_url + self.relative_url


if __name__ == '__main__':
    var = Films()
    count_ = var.get_count()
    print(count_)
    print(var.get_random_url())
