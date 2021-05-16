inputfile = open("triangles.in", "r")
outputfile = open("triangles.out", "w")
n = inputfile.readline()
n = int(n)


class Point:
    def __init__(self, x_value: int, y_value: int):
        self.x_value = x_value
        self.y_value = y_value

possibilities = []

points = []
for i in range(n):
    points.append(0)


for i in range(n + 1):
    nx = inputfile.read(1)
    if nx != "\n" and nx != " ":
        nx = int(nx)

    ny = inputfile.read(2)
    ny = ny.strip()
    ny = ny
    points[i - 1] = Point(nx, ny)
print("")
for j in range(3):
    possibilities.append(points)

for i in range(n):
    # start at first point.
    point1 = points[i]
    for j in range(n):
        point2 = points[j]
        if point2 != point1:
            if point1.x_value == point2.x_value:
                for g in range(n):
                    point3 = points[i]
                    if point3 != point2:
                        if point3.y_value == point1.y_value:
                            if point3.x_value != point1.x_value:
                                height = int(point2.y_value) - int(point1.y_value)
                                print(height)
                                base = int(point3.x_value) - int(point1.x_value)
                                print(base)
                                areatriangle = 0.5*base*height
                                print(areatriangle * 2)
