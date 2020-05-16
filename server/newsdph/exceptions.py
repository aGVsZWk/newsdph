
class DoesNotExist(Exception):
    pass


class ObjectDoesNotExist(Exception):
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '%s DoesNotExist' % self.model.__name__
