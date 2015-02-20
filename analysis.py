#!/usr/bin/python

# Your Name
# Physics 91SI Spring 2013
# Lab #3, Part 2
#
# Data analysis module
#
# This module contains a few assorted functions for loading data from a text
# file and performing operations on it
#
# Input file is expected to contain data in columns, separated by whitespace

import sys
import numpy as np
from matplotlib import pyplot as plt

# Return a list tuples (x, y), sorted by x-value, that represents the data of the file. 
def load(filename):
	data = []
	datafile = open(filename)
	for line in datafile:
		cols = line.split()
		x = float(cols[0])
		y = float(cols[1])
		data.append((x,y))
	datafile.close()
	return sort_x(data)

# Return a copy of data, sorted by x-value
def sort_x(data):
	keyx = lambda (x, y): x
	return sorted(data, key=keyx)

# Unpacking function, if you need just
# the x or y values in a list
def getxy(data):
	return zip(*data)

# Plot the data in a separate window
def plot(data):
	x, y = getxy(data)
	plt.figure(1)
	plt.ion()
	plt.plot(x, y)
	plt.show()

# Label the point data[index] with text
def label(data, index, text):
	plt.figure(1)
	plt.annotate(text, data[index])
	plt.show()

# Find the maximum value (sample function)
def max(values):
	if len(values) == 0:
		return None
	current = values[0]
	for val in values:
		if val > current:
			current = val
	return current


# Find the index of the point (x, y) with the maximum y value
def max_y_index(data):
	#####
	# Your code goes here
	#####
	pass # Replace this with your code


# Find the index of the point (x, y) with the maximum y value
# on the interval [xmin, xmax]
def find_peak(data, xmin, xmax):
	#####
	# Your code goes here
	#####
	pass # Replace this with your code



def main():
	pass # We're never going to run our main method here!

if __name__ == '__main__':
	main()
