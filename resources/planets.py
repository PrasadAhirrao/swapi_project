from resources.base import ResourceBase
from utils.fetch_data import hit_url
from resources.base import RandomNumbers
from typing import List


class Planets(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = 'api/planets'

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
        for i in RandomNumbers(1, 61):
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
    var = Planets()
    count_ = var.get_count()
    print(count_)
    print(var.get_random_url())
