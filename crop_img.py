from PIL import Image
import math

im = Image.open('1.tif')
pixels = list(im.getdata())
width, height = im.size
pixels_top_bottom = [pixels[i * width:(i + 1) * width] for i in range(height)]
pixels_left_right = [i.count(0) for i in list(zip(*pixels_top_bottom[::-1]))]
pixels_left_right_diff = [abs(j-i) for i,j in zip(pixels_left_right, pixels_left_right[1:])]

print(pixels_left_right_diff)

#im_new = im.crop((0,0,100,100))
#im_new.save("./a.tif", "TIFF")
