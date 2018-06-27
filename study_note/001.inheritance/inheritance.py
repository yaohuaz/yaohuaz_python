class Pet:
    def __init__(self,
                 name: str):
        self._name = name

    def voice(self):
        raise NotImplementedError()

    @property
    def name(self) -> str:
        return self._name


class Dog(Pet):
    def __init__(self,
                 name: str,
                 chase_cat: bool):
        Pet.__init__(self, name)
        self._chase_cat = chase_cat

    def voice(self) -> str:
        return 'au'

    @property
    def chase_cat(self) -> bool:
        return self._chase_cat


class Cat(Pet):
    def __init__(self,
                 name: str,
                 afraid_dog: bool):
        Pet.__init__(self, name)
        self._afraid_dog = afraid_dog

    def voice(self) -> str:
        return 'meow'

    @property
    def afraid_dog(self) -> bool:
        return self._afraid_dog

if __name__ == '__main__':
    dog_1 = Dog('Dog_One', True)
    dog_2 = Dog('Dog_Two', False)
    print('--name {} --voice {} --chase-cat {}'.format(dog_1.name, dog_1.voice(), dog_1.chase_cat))
    print('--name {} --voice {} --chase-cat {}'.format(dog_2.name, dog_2.voice(), dog_2.chase_cat))

    cat_1 = Cat('Cat_One', True)
    cat_2 = Cat('Cat_Two', False)
    print('--name {} --voice {} --afraid-dog {}'.format(cat_1.name, cat_1.voice(), cat_1.afraid_dog))
    print('--name {} --voice {} --afraid-dog {}'.format(cat_2.name, cat_2.voice(), cat_2.afraid_dog))

