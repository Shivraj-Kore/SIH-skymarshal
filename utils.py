# import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def is_point_inside_circle(center_x, center_y, x_circum, y_circum, x_check, y_check):
    # Define the center and circumference points
    center_point = Point(center_x, center_y)
    circumference_point = Point(x_circum, y_circum)

    # Create a circle polygon using the center and circumference points
    circle = center_point.buffer(center_point.distance(circumference_point))

    third_point = Point(x_check, y_check)

    # Check if the third point is inside the circle
    is_inside = circle.contains(third_point)

    # Print the result
    return is_inside 

def is_point_inside_rectangle(rect_a_x, rect_a_y, rect_b_x, rect_b_y, rect_c_x, rect_c_y, rect_d_x, rect_d_y, point_x, point_y):
    # Define the rectangle as a polygon
    rectangle = Polygon([(rect_a_x, rect_a_y), (rect_b_x, rect_b_y), (rect_c_x, rect_c_y), (rect_d_x, rect_d_y)])

    # Create a Point object
    point = Point(point_x, point_y)

    # Check if the point is inside the rectangle
    is_inside = rectangle.contains(point)

    # Print the result
    return is_inside