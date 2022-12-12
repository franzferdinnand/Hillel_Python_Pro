class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def __contains__(self, item):
        if not isinstance(item, Point):
            return False
        else:
            return (item.x - self.center_x) ** 2 + (item.y - self.center_y) ** 2 <= self.radius ** 2


if __name__ == '__main__':
    the_point = Point(4, 4)
    # the_point = (4, 4)
    the_circle = Circle(2, 3, 6)

    print(the_point in the_circle)
