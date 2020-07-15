class Rectangle():

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.fill_char = fill_char

    def change_fill(self, fill_char):
        self.fill_char = fill_char

    def translate(self, axis, num):
        if axis == 'x':
            self.start_x += num
            self.end_x += num
        elif axis == 'y':
            self.start_y += num
            self.end_y += num


class Canvas():

    def __init__(self, shapes=[]):
        self.shapes = shapes
        self.canvas = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]                       

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_helper(self, shape):
        for row in range(shape.start_y, shape.end_y + 1):
            for col in range(shape.start_x, shape.end_x + 1):
                try:
                    self.canvas[row][col] = shape.fill_char
                except IndexError:
                    continue

    def render(self):
        self.__init__(self.shapes)

        for shape in self.shapes:
            self.render_helper(shape)

        for row in self.canvas:
            print(''.join(row))

    def clear(self):
        self.__init__()       


c = Canvas()
r = Rectangle(0, 5, 7, 8, '+')
r2 = Rectangle(4, 2, 6, 4, '*')
c.add_shape(r)
c.add_shape(r2)
c.render()
r.change_fill('c')
r2.translate('x', -2)
r2.translate('y', 1)
c.render()
