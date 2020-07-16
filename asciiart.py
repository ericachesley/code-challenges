class Rectangle():
    """Initialize and update a rectangle object."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.fill_char = fill_char


    def __repr__(self):
        return f"<Rectangle '{self.fill_char}' at ({self.start_x}, {self.start_y})>"


    def change_fill(self, fill_char):
        """
        Update the fill char of the rectangle.

        For example:
        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> r.fill_char
        '+'
        >>> r.change_fill('>')
        >>> r.fill_char
        '>'
        """

        self.fill_char = fill_char


    def translate(self, axis, num):
        """
        Update the position of the rectangle.

        For example:
        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> r.start_x
        0
        >>> r.translate('x', 4)
        >>> r.start_x
        4

        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> r.end_y
        8
        >>> r.translate('y', -4)
        >>> r.end_y
        4
        """

        if axis == 'x':
            self.start_x += num
            self.end_x += num
        elif axis == 'y':
            self.start_y += num
            self.end_y += num


class Canvas():
    """Initialize, update, and render the canvas."""

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


    def __repr__(self):
        return f'<Canvas {len(self.canvas[0])} by {len(self.canvas)} chars>'                       


    def add_shape(self, shape):
        """
        Add shape to canvas.

        For example:
        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> c = Canvas()
        >>> c.shapes
        []
        >>> c.add_shape(r)
        >>> c.shapes
        [<Rectangle '+' at (0, 5)>]
        >>> r2 = Rectangle(4, 2, 6, 4, '*')
        >>> c.add_shape(r2)
        >>> c.shapes
        [<Rectangle '+' at (0, 5)>, <Rectangle '*' at (4, 2)>]
        >>> c.clear()
        """

        self.shapes.append(shape)


    def render_helper(self, shape):
        """ 
        Add each shape to the canvas.
        
        This is done at the render stage so that updates to fill_char and 
        position are accounted for.

        For example:
        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> c = Canvas()
        >>> c.canvas[6][2]
        ' '
        >>> c.render_helper(r)
        >>> c.canvas[6][2]
        '+'
        >>> c.clear()
        """

        for row in range(shape.start_y, shape.end_y + 1):
            for col in range(shape.start_x, shape.end_x + 1):
                try:
                    self.canvas[row][col] = shape.fill_char
                except IndexError:
                    continue


    def render(self):
        """
        Update and print canvas.

        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> c = Canvas([r])
        >>> c.render()
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        ++++++++  
        ++++++++  
        ++++++++  
        ++++++++  
        <BLANKLINE>
        """

        self.__init__(self.shapes)

        for shape in self.shapes:
            self.render_helper(shape)

        for row in self.canvas:
            print(''.join(row))


    def clear(self):
        """
        Clear canvas of all shapes.

        For example:
        >>> r = Rectangle(0, 5, 7, 8, '+')
        >>> c = Canvas([r])
        >>> c.render()
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        ++++++++  
        ++++++++  
        ++++++++  
        ++++++++  
        <BLANKLINE>
        >>> c.shapes
        [<Rectangle '+' at (0, 5)>]
        >>> c.clear()
        >>> c.render()
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> c.shapes
        []
        """

        self.__init__([])       


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED ***\n")