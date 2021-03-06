from rasa.core.slots import Slot

valid_colors = {'green', 'blue', 'black', 'brown', 'yellow', 'orange', 'red', 'purple'}
valid_objects = {'apple', 'orange', 'banana', 'strawberry', 'kiwi', 'brick'}
generic_objects = {'something', 'object', 'thing', 'item', 'fruit', 'vegetable'}
valid_placements = {'left', 'right', 'middle'}


def update_known_objects(objects):
    valid_objects.update(objects)


def update_known_colors(colors):
    valid_colors.update(colors)


class ColorSlot(Slot):

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value in valid_colors:
                r = [1.0, 1.0]
            else:
                r = [0.0, 1.0]
        return r


class ObjectSlot(Slot):

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value in valid_objects:
                r = [1.0, 1.0]
            elif self.value in generic_objects:
                r = [1.0, 0.0]
            else:
                r = [0.0, 1.0]
        return r


class PlacementSlot(Slot):

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value in valid_placements:
                r = [1.0, 1.0]
            else:
                r = [0.0, 1.0]
        return r
