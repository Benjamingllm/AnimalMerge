from .animal import ANIMAL_COLLISION,Souris, Hamster, Renard, Chien, Mouton, Vache


class MergeManager:
    def __init__(self,space,animals):
        self.space = space
        self.animals = animals
        self.merge_queue = []
        self.merge_order = [Souris, Hamster, Renard, Chien, Mouton, Vache]
        self.space.on_collision(ANIMAL_COLLISION, ANIMAL_COLLISION, begin=self.check_for_merges)


    def check_for_merges(self,arbiter,space,data):
        shape_a, shape_b = arbiter.shapes
        animal_a = self.animals.get(shape_a)
        animal_b = self.animals.get(shape_b)
        if animal_a and animal_b and type(animal_a) == type(animal_b):
            self.merge(animal_a, animal_b)

    def resolve_merges(self):
        for animal_a, animal_b, next_level_class in self.merge_queue:
            if animal_a.shape in self.animals and animal_b.shape in self.animals and next_level_class:
                x = (animal_a.body.position.x + animal_b.body.position.x) / 2
                y = (animal_a.body.position.y + animal_b.body.position.y) / 2
                self.remove_animal(animal_a)
                self.remove_animal(animal_b)
                self.add_animal(next_level_class(x, y, self.space))

        self.merge_queue.clear()

    
    def add_animal(self, animal):
        self.animals[animal.shape] = animal

    def merge(self, animal_a, animal_b):
        next_level_class = self.get_next_level_class(type(animal_a))
        self.merge_queue.append((animal_a, animal_b, next_level_class))
        return self.merge_queue


    def get_next_level_class(self, animal_class):
        for type in self.merge_order:
            if type == animal_class:
                index = self.merge_order.index(type)
                if index + 1 < len(self.merge_order):
                    return self.merge_order[index + 1]

    def remove_animal(self, animal):
        self.space.remove(animal.body, animal.shape)
        del self.animals[animal.shape]
