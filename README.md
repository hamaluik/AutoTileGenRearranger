AutoTileGenRearranger
=====================

A simple tool to convert the mangled mess of tiles output by [AutoTileGen](http://autotilegen.com/) into something a little more friendly.

It turns something like this:

![Sample AutoTileGen Output](https://raw.githubusercontent.com/FuzzyWuzzie/AutoTileGenRearranger/master/Tileset.png "Sample AutoTileGen Output")

Into this:

![Human-Friendly Version](https://raw.githubusercontent.com/FuzzyWuzzie/AutoTileGenRearranger/master/Tileset.png.r.png "Human-Friendly Version")

Requirements
============

* Python
* ImageMagick
* Python Wand
    - Install with: `pip install wand`

Usage
=====

```bash
python AutoTileGenRearranger.py Tileset.png
```

* Replace `Tileset.png` with the file spit out by AutoTileGen.
* The output file would then be `Tileset.png.r.png`
