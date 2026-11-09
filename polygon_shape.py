"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if sides < 3:
            raise ValueError("sides must be at least 3")
        if side_length <= 0:
            raise ValueError("side_length must be greater than 0")
        if pen_size <= 0:
            raise ValueError("pen_size must be greater than 0")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle

        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        t = self._turtle
        t.penup()
        t.goto(self._x, self._y)
        t.setheading(self._angle)
        t.color(self._color)
        t.pensize(self._pen_size)
        t.pendown()
        for _ in range(self._sides):
            t.forward(self._side_length)
            t.left(360 / self._sides)
        t.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self._x = x
        self._y = y
        self._turtle.clear()
        self.draw()
