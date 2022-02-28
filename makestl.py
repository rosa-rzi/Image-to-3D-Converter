#!/usr/bin/env python

import sys

from imageprep import prepareImg
from meshcreator import to_mesh

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print >> sys.stderr, "Usage: ./img2stl <path_to_image> <new_stl_filename>" # if input is called wrong then it was output this, otherwise makes stl
	img = prepareImg(sys.argv[1]) # takes first input (image) and prepares it
	to_mesh(img, sys.argv[2], 2)