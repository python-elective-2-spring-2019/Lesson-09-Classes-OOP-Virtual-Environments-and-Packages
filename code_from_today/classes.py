class A:
    
    # Class attributes
    xxx = "Claus jlkjlkjlk"
    
    # constructor and instance attributes
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def __str__(self):
        return "[" + self._name + ","+ self.xxx + "]"

    def __len__(self):
        return 1234


class B:
    pass