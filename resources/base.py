from utils.randgen import ProduceChars
import random
not_implemented_error_msg = "This method has not been implemented"


# TODO - you can also convert this class into abstract class and
# define methods as abstract methods

class SampleDataException(Exception):
    def __init__(self, message, errors=""):
        print("message coming from our custom exception class")
        super().__init__(message)
        self.errors = errors


class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resource
    classes
    """

    # TODO - add all resources in this list
    resources = ["planets", "spacies", "people", "vehicles", "films", "starships"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError(not_implemented_error_msg)

    def get_resource_urls(self, resource):
        raise NotImplementedError(not_implemented_error_msg)

    def get_sample_data(self):
        raise SampleDataException(not_implemented_error_msg)


class RandomNumbers:
    """generator class to produce random numbers in a given range"""

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < 4:
            yield random.randrange(self.start, self.stop)
            current += 1


if __name__ == '__main__':
    print(RandomNumbers(1, 83))
