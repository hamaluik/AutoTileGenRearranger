#!/usr/bin/env python
from wand.image import Image
import argparse

# get the arguments
parser = argparse.ArgumentParser(description='Rearranges the tiles in an AutoTileGen output file into a more human-friendly format.')
parser.add_argument('file', nargs=1, help='the name of AutoTileGen\'s output filename')
args = parser.parse_args()

# set up mappings
mapping = [
	[[2, 1], [9, 2], [7, 2], [7, 0], [9, 0], [8, 2], [7, 1], [8, 0]],
	[[9, 1], [3, 4], [2, 4], [8, 4], [8, 3], [9, 3], [9, 4], [8, 1]],
	[[2, 0], [3, 1], [2, 2], [1, 1], [3, 0], [3, 2], [1, 2], [1, 0]],
	[[2, 3], [0, 1], [3, 3], [0, 2], [1, 3], [0, 0], [5, 1], [7, 4]],
	[[6, 4], [6, 3], [7, 3], [5, 4], [4, 4], [4, 3], [5, 3], [6, 2]],
	[[4, 2], [4, 0], [6, 0], [5, 2], [4, 1], [5, 0], [6, 1], -1]]

# now try to open the file
with Image(filename=args.file[0]) as img:
	tileWidth = int(img.width / 8)
	tileHeight = int(img.height / 6)
	print("Auto-detected tile size: %dx%d" % (tileWidth, tileHeight))
	print("Beginning re-arrangement...");
	with Image(width=tileWidth*10, height=tileHeight*5) as rImg:
		for x in range(0, 8):
			for y in range(0, 6):
				sx = x * tileWidth
				sy = y * tileHeight
				with img[sx:sx+tileWidth, sy:sy+tileHeight] as tile:
					if mapping[y][x] != -1:
						rImg.composite(tile, mapping[y][x][0]*tileWidth, mapping[y][x][1]*tileHeight)
		rImg.format = 'png'
		rImg.save(filename='%s.r.png' % args.file[0])
	print("Done!");