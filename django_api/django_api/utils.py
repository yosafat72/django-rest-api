import random
import string


class Utils:

    def randomStringForId():
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(10))
