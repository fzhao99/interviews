from data_structures.LinkedList import LinkedList
from random import randint
import unittest

class Animal:
    def __init__(self, name, time_stamp = None):
        self.name = name
        self.order = time_stamp

    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def is_earlier(self, other_animal):
        return self.get_order() < other_animal.get_order()


class Dog(Animal):
    pass

class Cat(Animal):
    pass



class AnimalShelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.order = 0

    def dequeueAny(self):
        if len(self.cats) == 0:
            return self.dequeueDog()
        if len(self.dogs) == 0:
            return self.dequeueCat()

        cur_cat = self.cats.head.value
        cur_dog = self.dogs.head.value

        if cur_cat.is_earlier(cur_dog):
            self.cats.head = self.cats.head.next
            return cur_cat
        if cur_dog.is_earlier(cur_cat):
            self.dogs.head = self.dogs.head.next
            return cur_dog

    def dequeueDog(self):
        cur_dog = self.dogs.head.value
        self.dogs.head = self.dogs.head.next
        return cur_dog

    def dequeueCat(self):
        cur_cat = self.cats.head.value
        self.cats.head = self.cats.head.next
        return cur_cat

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1

        if type(animal) is Dog:
            self.dogs.add(animal)
        if type(animal) is Cat:
            self.cats.add(animal)


class Tests(unittest.TestCase):
    def test_dequeue_any(self):
        s = AnimalShelter()
        s_test = []

        for i in range(10):
            cat_or_dog = randint(0,1)

            if cat_or_dog:
                cat = Cat(str(i))
                s.enqueue(cat)
                s_test.append(cat.order)
            else:
                dog = Dog(str(i))
                s.enqueue(dog)
                s_test.append(dog.order)

        lst = []

        for i in range(10):
            item = s.dequeueAny()
            lst.append(item.order)

        self.assertEqual(s_test, lst)

if __name__ == "__main__":
    unittest.main()
