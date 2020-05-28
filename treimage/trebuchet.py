"""
Creates a trebuchet out of points.

Inspired by the OptArt book by Robert Bosch.
"""
from functools import cached_property

__all__ = ['FlexibleTrebuchet', 'A', 'B', 'C', 'D']

class FlexibleTrebuchet:
    """
    Flexible trebuchet is like a normal trebuchet, but
    instead of a diagnal line going through the center, we move
    the end point to make two different lines that connect
    to the center.
    """
    def __init__(self, x1: float, y1: float,
                 size: float, brightness: float):
        """
        Parameters
        ==========
        x1: Top left corner, horizontal pos
        y1: Top left corner, vertical pos
        size: Multiplicative factor for width/height
        brightness: Float between 0 and 1
        """
        assert size >= 1
        assert 0 <= brightness <= 1
        self._x1: float = x1
        self._y1: float = y1
        self._size: float = size
        self._brightness: float = brightness

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @property
    def size(self):
        return self._size

    @property
    def brightness(self):
        return self._brightness

    @cached_property
    def x2(self):
        return self.x1 + (4 * self.size)

    @cached_property
    def y2(self):
        return self.y1 + (4 * self.size)

    def scale_position_point(self, point):
        scaled_point = (self.size * point[0], self.size * point[1])
        return (self.x1 + scaled_point[0], self.y1 + scaled_point[1])

    @cached_property
    def midpoint(self):
        raise NotImplementedError

    @cached_property
    def points(self):
        raise NotImplementedError



class A(FlexibleTrebuchet):
    """Follows the A Trebuchet from OptArt."""
    @cached_property
    def midpoint(self):
        normalized_point = (-2 * self.brightness + 3, 2 * self.brightness + 1)
        return self.scale_position_point(normalized_point)

    @cached_property
    def points(self):
        return ((self.x1, self.y1), self.midpoint, (self.x2, self.y2), (self.x1, self.y2))


class B(FlexibleTrebuchet):
    """Follows the B Trebuchet from OptArt."""
    @cached_property
    def midpoint(self):
        normalized_point = (-2 * self.brightness + 3, -2 * self.brightness + 3)
        return self.scale_position_point(normalized_point)

    @cached_property
    def points(self):
        return ((self.x1, self.y1), (self.x2, self.y1), self.midpoint, (self.x1, self.y2))

class C(FlexibleTrebuchet):
    """Follows the C Trebuchet from OptArt."""
    @cached_property
    def midpoint(self):
        normalized_point = (2 * self.brightness + 1, -2 * self.brightness + 3)
        return self.scale_position_point(normalized_point)

    @cached_property
    def points(self):
        return ((self.x1, self.y1), self.midpoint, (self.x2, self.y2), (self.x2, self.y1))

class D(FlexibleTrebuchet):
    """Follows the D Trebuchet from OptArt."""
    @cached_property
    def midpoint(self):
        normalized_point = (2 * self.brightness + 1, 2 * self.brightness + 1)
        return self.scale_position_point(normalized_point)

    @cached_property
    def points(self):
        return ((self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1), self.midpoint)
