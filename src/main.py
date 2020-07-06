#!/usr/bin/python
import math
import sys


def output(surface, parameter, passing_point, parallel_vec, intersection_points, infin):
    parameter = int(parameter)
    if (surface == 1):
        print("Sphere of radius {}".format(parameter))
    if (surface == 2):
        print("Cylinder of radius {}".format(parameter))
    if (surface == 3):
        print("Cone with a {} degree angle".format(parameter))
    print("Line passing through the point (%i, %i, %i) and parallel to the vector (%i, %i, %i)" %
          (passing_point[0], passing_point[1], passing_point[2], parallel_vec[0], parallel_vec[1], parallel_vec[2]))
    if len(intersection_points) > 0:
        if (len(intersection_points)) > 1:
            print("{} intersection points:".format(len(intersection_points)))
        else:
            print("{} intersection point:".format(len(intersection_points)))
        for i in range(len(intersection_points)):
            print("(%.3f, %.3f, %.3f)" % (intersection_points[i][0], intersection_points[i][1], intersection_points[i][2]))
    elif infin == 0:
        print("No intersection point.")
    else:
        print("There is an infinite number of intersection points.")
    sys.exit(0)


def calc_cylinder(point, vector, parameter):
    passing_point = point
    parallel_vec = vector
    intersection_points = []
    new = []
    infin = 0
    tmp_1 = 0
    tmp_2 = 0

    if (vector[0] == 0 and vector[1] == 0):
        if (math.pow(parameter, 2) == math.pow(point[0], 2) + math.pow(point[1], 2)):
            infin = 1
    else:
        under_square = (math.pow(vector[1], 2) + math.pow(vector[0], 2)) * math.pow(parameter, 2) - math.pow(point[0], 2) * math.pow(vector[1], 2) + 2 * point[0] * point[1] * vector[0] * vector[1] - math.pow(point[1], 2) * math.pow(vector[0], 2)
        if under_square >= 0:
            tmp_1 = -((-math.sqrt(under_square)) + point[1] * vector[1] + point[0] * vector[0]) / (math.pow(vector[1], 2) + math.pow(vector[0], 2))
            solve_x1 = point[0] + tmp_1 * vector[0]
            solve_y1 = point[1] + tmp_1 * vector[1]
            solve_z1 = point[2] + tmp_1 * vector[2]
            new.append(solve_x1)
            new.append(solve_y1)
            new.append(solve_z1)
            intersection_points.append(new)
            new = []
            tmp_2 = -((math.sqrt(under_square)) + point[1] * vector[1] + point[0] * vector[0]) / (
                        math.pow(vector[1], 2) + math.pow(vector[0], 2))
            solve_x2 = point[0] + tmp_2 * vector[0]
            solve_y2 = point[1] + tmp_2 * vector[1]
            solve_z2 = point[2] + tmp_2 * vector[2]
            if solve_z1 != solve_z2 and solve_x1 != solve_x2 and solve_y1 != solve_y2:
                new.append(solve_x2)
                new.append(solve_y2)
                new.append(solve_z2)
                intersection_points.append(new)
    output(2, parameter, passing_point, parallel_vec, intersection_points, infin)


def calc_cone(point, vector, parameter):
    if parameter >= 90:
        sys.exit(84)
    intersection_points = []
    x1 = [0.0, 0.0, 0.0]
    x2 = [0.0, 0.0, 0.0]
    infin = 0
    parameter = math.radians(parameter)
    a = math.pow(vector[0], 2) + math.pow(vector[1], 2) - math.pow(vector[2] * math.tan(parameter), 2)
    b = 2 * point[0] * vector[0] + 2 * point[1] * vector[1] - 2 * point[2] * vector[2] * math.pow(math.tan(parameter), 2)
    c = math.pow(point[0], 2) + math.pow(point[1], 2) - math.pow(point[2], 2) * math.pow(math.tan(parameter), 2)
    if a == 0:
        if b == 0:
            if c == 0:
                infin = 1
                output(3, parameter, point, vector, intersection_points, infin)
            else:
                output(3, parameter, point, vector, intersection_points, infin)
        else:
            l = -c / b
            x1[0] = point[0] + l * vector[0]
            x1[1] = point[1] + l * vector[1]
            x1[2] = point[2] + l * vector[2]
            intersection_points.append(x1)
            output(3, parameter, point, vector, intersection_points, infin)
    delta = math.pow(b, 2) - 4 * a * c
    if delta < 0:
        output(3, parameter, point, vector, intersection_points, infin)
    elif delta == 0:
        l = -b/(2 * a)
        x1[0] = point[0] + l * vector[0]
        x1[1] = point[1] + l * vector[1]
        x1[2] = point[2] + l * vector[2]
        intersection_points.append(x1)
        output(3, parameter, point, vector, intersection_points, infin)
    elif delta > 0:
        l1 = ((-b - math.sqrt(delta))/(2 * a))
        l2 = ((-b + math.sqrt(delta))/(2 * a))
        x1[0] = point[0] + l1 * vector[0]
        x1[1] = point[1] + l1 * vector[1]
        x1[2] = point[2] + l1 * vector[2]
        x2[0] = point[0] + l2 * vector[0]
        x2[1] = point[1] + l2 * vector[1]
        x2[2] = point[2] + l2 * vector[2]
        if l1 > l2:
            intersection_points.append(x2)
            intersection_points.append(x1)
        else:
            intersection_points.append(x1)
            intersection_points.append(x2)
        output(3, parameter, point, vector, intersection_points, infin)


def calc_sphere(point, vector, parameter):
    passing_point = point
    parallel_vec = vector
    intersection_points = []
    new = []
    infin = 0
    tmp_under_break = math.pow(vector[0], 2) + math.pow(vector[1], 2) + math.pow(vector[2], 2)
    tmp = -1 * (vector[0] * point[0] + vector[1] * point[1] + vector[2] * point[2]) / tmp_under_break
    p = math.pow(tmp, 2)
    q = (math.pow(point[0], 2) + math.pow(point[1], 2) + math.pow(point[2], 2) - math.pow(parameter, 2)) / tmp_under_break
    under_square = p - q
    if under_square >= 0:
        v_1 = tmp + math.sqrt(under_square)
        new.append(point[0] + v_1 * vector[0])
        new.append(point[1] + v_1 * vector[1])
        new.append(point[2] + v_1 * vector[2])
        intersection_points.append(new)
    new = []
    if under_square > 0:
        v_2 = tmp - math.sqrt(under_square)
        new.append(point[0] + v_2 * vector[0])
        new.append(point[1] + v_2 * vector[1])
        new.append(point[2] + v_2 * vector[2])
        intersection_points.append(new)

    output(1, parameter, passing_point, parallel_vec, intersection_points, infin)
    return


def calculation(surface, point, vector, parameter):
    if surface == 2:
        calc_cylinder(point, vector, parameter)
    elif surface == 3:
        calc_cone(point, vector, parameter)
    elif surface == 1:
        calc_sphere(point, vector, parameter)


def run_function():
    surface = int(sys.argv[1])
    point = []
    vector = []
    parameter = float(sys.argv[8])

    if not (0 < surface < 4):
        sys.exit(84)
    for i in range (2, 5):
        point.append(float(sys.argv[i]))
    for i in range (5, 8):
        vector.append(float(sys.argv[i]))
    if parameter <= 0:
        sys.exit(84)
    if vector[0] == 0 and vector[1] == 0 and vector[2] == 0:
        sys.exit(84)
    calculation(surface, point, vector, parameter)


def error_tryer():
    try:
        list = []
        for i in range(1, len(sys.argv)):
            list.append(int(sys.argv[i]))
    except ValueError:
        sys.exit(84)


def input():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("USAGE")
        print("    ./104intersection opt xp yp zp xv yv zv p")
        print("\nDESCRIPTION")
        print("      opt           surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
        print("      (xp, yp, zp)  coordinates of a point by which the light ray passes through")
        print("      (xv, yv, zv)  coordinates of a vector parallel to the light ray")
        print("      p             parameter: radius of the sphere, radius of the cylinder, or")
        print("                    angle formed by the cone and the Z-axis")
        sys.exit(0)
    if (len(sys.argv) != 9):
        sys.exit(84)
    else:
        error_tryer()
        run_function()
        sys.exit(0)

input()