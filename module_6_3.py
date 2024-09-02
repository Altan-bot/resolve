class Horse:
    x_distance = 0
    _sound = 'Frrr'

    def __init__(self, dx):
        self.dx = dx

    def run(self):
        self.x_distance += self.dx
        return self.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, dy):
        self.dy = dy

    def flu(self):
        self.y_distance += self.dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        self.sound = super()._sound
        self.sound = super().sound

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        super().run()
        super().flu()
        return self.x_distance, self.y_distance

    def get_pos(self):
        pegasus = (self.x_distance, self.y_distance)
        return pegasus

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
