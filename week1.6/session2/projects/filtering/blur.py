import image
import filters

photo = Image.read(coins.pgm)

filters.blue(photo)

Image.write_pgm(coins.pgm)