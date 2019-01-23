#!/usr/bin/env python3
'''Exercise-1: Working with Geometric Objects

Usage:
    ./read_attributes.py

Author:
    Simone Claridge - 01.22.2019
'''

# Import necessary geometric objects from shapely module
from shapely.geometry import LineString, Polygon


def getArea(polygon):
	# Get the area if a polygon
	if type(polygon) == Polygon:
		area = polygon.area
		return area
	else:
		return "Error: not a polygon"


def getCentroid(shape):
	# Get the centroid of the line or polygon
	shape_centroid = shape.centroid
	return shape_centroid


def getLength(polyline):
	# Get the length of the polygon exterior if the parameter is a polygon
	if type(polyline) == Polygon:
		exterior = polyline.exterior
		return exterior
	# Get the length of the line if the parameter is a line
	elif type(polyline) == LineString:
		length = polyline.length
		return length
	else:
		return "Error: LineString or Polygon geometries required!"


line = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(getCentroid(line))

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(getArea(poly))

print(getLength(poly))
print(getLength(line))
