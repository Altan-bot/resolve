class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *args):
        massive_lst = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive_lst.append(6)
            self.sides = massive_lst
            self.get_sides()

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__(self):
        return self.side * self.sides_count


class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__()/(2*3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return ((self.side) ** 2) / (4 * 3.141569)


class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height


class Cube(Figure):
    sides_count = 12

    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
            self.__sides = set_side_lst
            return self.__sides

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())