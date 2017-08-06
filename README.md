# cc0datasets

## Images

from [Public Domain Pictures - Free Stock Photos](http://www.publicdomainpictures.net/)

### animals

1. gazelle.jpg
    - [KC Zoo 10 Free Stock Photo - Public Domain Pictures](http://www.publicdomainpictures.net/view-image.php?image=43291&picture=kc-zoo-10)
    - Animal at Kansas City Zoo, cannot remember the name sorry.
    - Polaroid IS2132
    - 1/362s, f 5.7, ISO 100, 71 mm
1. pelicans.jpg
    - [The King Of The Zoo Free Stock Photo - Public Domain Pictures](http://www.publicdomainpictures.net/view-image.php?image=52246&picture=the-king-of-the-zoo)
    - Picture taken at Ueno Zoo, Tokyo, Japan
    - Nikon 1 V1
    - 10/4000s, f 5.6, ISO 100, 30 mm
1. pelicans.jpg
    - [Zoo Pelicans Free Stock Photo - Public Domain Pictures](http://www.publicdomainpictures.net/view-image.php?image=77410&picture=zoo-pelicans)
    - Beautiful pelicans swimming around at a pond at the John Ball park zoo.
    - Canon EOS Rebel T3i
    - 1/400s, f 8.0, ISO 100, 116 mm
1. penguins.jpg
    - [Penguins In Zoo Free Stock Photo - Public Domain Pictures](http://www.publicdomainpictures.net/view-image.php?image=7420&picture=penguins-in-zoo)
    - Group of penguins getting ready for swim in Chester zoo
    - Canon EOS 5D Mark II
    - 1/320s, f 5.6, ISO 100, 400 mm
1. zebra.jpg
    - [Zebra In Melbourne Zoo Free Stock Photo - Public Domain Pictures](http://www.publicdomainpictures.net/view-image.php?image=33133&picture=zebra-in-melbourne-zoo)
    - Zebra in Melbourne Zoo Australia
    - Nikon D40x
    - 10/5000s, f 5.6, ISO 200, 62 mm
    
### animals_thumbnail

- gazelle.jpg
- pelicans.jpg
- penguins.jpg
- pollarbear.jpg
- zebra.jpg

Images obtained by resizing images in `animals` by Pillow
 `im.thumbnail` with size 256x256 i.e. :

```
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
    img.save(outfile, 'JPEG')
```

See:

- [Image Module — Pillow (PIL Fork) 3.1.2 documentation](http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails)
- [Index of Packages : Python Package Index](https://pypi.python.org/pypi/Pillow)

### png

1. antinous_mondragone.png
    - [Antinous-bysten i Louvre, Nordisk familjebok - File:Antinous Mandragone profil.jpg - Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Antinous_Mandragone_profil.jpg#/media/File:Antinous-bysten_i_Louvre,_Nordisk_familjebok.png)
1. wappen.png
    - [Wappen Mörsch 1919-1987 - File:Wappen Mörsch 1919-1987.png - Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Wappen_M%C3%B6rsch_1919-1987.png?uselang=ja#/media/File:Wappen_M%C3%B6rsch_1919-1987.png)
1. keyboard.png
    - [test 0514 | rapmocha | Flickr](https://www.flickr.com/photos/140867404@N05/26922373761/in/dateposted-public/)

