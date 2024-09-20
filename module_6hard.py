import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != self.sides_count:
            self.__sides = [list(sides)[0]] * self.sides_count
        elif len(sides) == self.sides_count:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color.clear()
            self.__color.extend([r, g, b])
            return self.__color

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides.clear()
            self.__sides.extend(new_sides)
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        square = self.__radius ** 2 * math.pi
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 0

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        half_per = (a + b + c) / 2
        square = math.sqrt((half_per * (half_per - a) * (half_per - b) * (half_per - c)))
        return square

    def get_height(self):
        self.__height = (2 * self.get_square()) / self.get_sides()[0]
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [list(sides)[0]] * self.sides_count
        self.volume = 0

    def get_volume(self):
        self.volume = self.get_sides()[0] ** 3
        return self.volume


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