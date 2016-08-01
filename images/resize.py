"""Resize files(matched PATTERN) in INDIR with SIZE and save them in OUTDIR. Requires Python Imaging Library(PIL). Copyright 2016 rapmocha."""

import os
import glob
from PIL import Image

INDIR = 'animals'
OUTDIR = 'animals_thumbnail'
PATTERN = '*.jpg'
SIZE = (256, 256)


def resize():
    for infile in glob.glob(os.path.join(INDIR, PATTERN)):
        img = Image.open(infile)
        img.thumbnail(SIZE)
        basename = os.path.basename(infile)
        outfile = os.path.join(OUTDIR, basename)
        img.save(outfile, 'JPEG')


if __name__ == '__main__':
    resize()
