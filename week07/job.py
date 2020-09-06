# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @property
    def animal_type(self):
        return self.type

    @animal_type.setter
    def animal_type(self, value):
        type = ('食肉', '食草')
        if value not in type:
            raise ValueError(f'{value} type not found {type}')
        self.type = value

    @property
    def animal_physical(self):
        return self.physical

    @animal_physical.setter
    def animal_physical(self, value):
        physical = ('大型', '中型', '小型')
        if value not in physical:
            raise ValueError(f'{value} physical not found {physical}')
        self.physical = value

    @property
    def animal_character(self):
        return self.physical

    @animal_character.setter
    def animal_character(self, value):
        character = ('温顺', '凶猛')
        if value not in character:
            raise ValueError(f'{value} character not found {character}')
        self.character = value

    def is_preyer(self):
        if (
                self.type == '食肉'
                and self.physical != '小型'
                and self.character == '凶猛'
        ):
            return True
        return False

    @abstractmethod
    def is_pet(self):
        pass


class Cat(Animal):
    sound = '喵喵喵'

    def __init__(self, name, type, physical, character):
        self.name = name
        self.pet = True
        self.animal_type = type
        self.animal_physical = physical
        self.animal_character = character

    def is_pet(self):
        return not self.is_preyer()


class Dog(Animal):
    sound = '汪汪汪'

    def __init__(self, name, type, physical, character):
        self.name = name
        self.pet = True
        self.animal_type = type
        self.animal_physical = physical
        self.animal_character = character

    def is_pet(self):
        return not self.is_preyer()


class Zoo(object):

    def __init__(self, name):
        self.name = name
        self.zoo_animal = []

    def add_animal(self, animal):
        animal_species = type(animal).__name__
        if animal_species in self.__dict__:
            raise ValueError(f'{animal.name}同种动物已经存在')
        self.__dict__[animal_species] = True


if __name__ == '__main__':
    animal = Cat('大花猫', '食肉', '小型', '凶猛')
    print(animal.sound)
    print(animal.name)
    print(f'是否适合当宠物: {animal.is_pet()}')
    z = Zoo('我的动物园')
    z.add_animal(animal)
    # z.add_animal(animal)
    have_cat = hasattr(z, type(animal).__name__)
    print(have_cat)
