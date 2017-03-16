from PIL import Image
import math

file_name = "2"

tif_file_name = file_name+".tif"
jpg_file_name = file_name+".jpg"

im = Image.open(tif_file_name)
im_jpg = Image.open(jpg_file_name)
pixels = list(im.getdata())
width, height = im.size
pixels_top_bottom = [pixels[i * width:(i + 1) * width] for i in range(height)]

pixels_top_bottom_black_val = [i.count(0) for i in pixels_top_bottom]
pixels_left_right_black_val = [i.count(0) for i in list(zip(*pixels_top_bottom[::-1]))]

pixels_top_bottom_diff = [abs(j-i) for i,j in zip(pixels_top_bottom_black_val, pixels_top_bottom_black_val[1:])]
pixels_left_right_diff = [abs(j-i) for i,j in zip(pixels_left_right_black_val, pixels_left_right_black_val[1:])]

left_1 = pixels_left_right_diff.index(max(pixels_left_right_diff[50:700]))
left_2 = pixels_left_right_diff.index(max(pixels_left_right_diff[700:1500]))
left_3 = pixels_left_right_diff.index(max(pixels_left_right_diff[1500:2000]))
top_1 = pixels_top_bottom_diff.index(max(pixels_top_bottom_diff[50:1000]))
top_2 = pixels_top_bottom_diff.index(max(pixels_top_bottom_diff[2000:3000]))

print('-left-')
print(left_1)
print(left_2)
print(left_3)
print('-top-')
print(top_1)
print(top_2)
left_img = im_jpg.crop((left_1+30,top_1+20,left_2-30,top_2-20))
right_img = im_jpg.crop((left_2+30,top_1+20,left_3-30,top_2-20))
left_img.save("./left.tif", "TIFF")
right_img.save("./right.tif", "TIFF")
#im_new = im.crop((0,0,100,100))
#im_new.save("./a.tif", "TIFF")
