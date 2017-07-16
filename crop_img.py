from PIL import Image
import math
import os

def crop_image(file_name,output_dir,input_dir):
    tif_file_name = input_dir+"/"+file_name+".tif"
    jpg_file_name = input_dir+"/"+file_name+".jpg"

    im = Image.open(tif_file_name)
    im_jpg = Image.open(jpg_file_name)
    pixels = list(im.getdata())
    width, height = im.size
    pixels_top_bottom = [pixels[i * width:(i + 1) * width] for i in range(height)]

    pixels_top_bottom_black_val = [i.count(0) for i in pixels_top_bottom]
    pixels_left_right_black_val = [i.count(0) for i in list(zip(*pixels_top_bottom[::-1]))]

    pixels_top_bottom_diff = [abs(j-i) for i,j in zip(pixels_top_bottom_black_val, pixels_top_bottom_black_val[1:])]
    pixels_left_right_diff = [abs(j-i) for i,j in zip(pixels_left_right_black_val, pixels_left_right_black_val[1:])]

    left_1 = pixels_left_right_diff[50:700].index(max(pixels_left_right_diff[50:700]))+50
    left_2 = pixels_left_right_diff[700:1500].index(max(pixels_left_right_diff[700:1500]))+700
    left_3 = pixels_left_right_diff[1500:2000].index(max(pixels_left_right_diff[1500:2000]))+1500
    top_1 = pixels_top_bottom_diff[50:1000].index(max(pixels_top_bottom_diff[50:1000]))+50
    top_2 = pixels_top_bottom_diff[2000:3000].index(max(pixels_top_bottom_diff[2000:3000]))+2000
    
    #print('-left-')
    #print(width)
    #print(max(pixels_left_right_diff[700:1500]))
    #print(max(pixels_left_right_diff[700:1500]))
    #print(max(pixels_left_right_diff[1500:2000]))
    #print(str(left_1) + "-" + str(left_2) + "-" + str(left_3))
    #print('-top-')
    #print(height)
    #print(str(top_1) + "-" + str(top_2))

    left_offset = 5
    top_offset = 3
    
    left_img = im_jpg.crop((left_1+left_offset,top_1+top_offset,left_2-left_offset,top_2-top_offset))
    right_img = im_jpg.crop((left_2+left_offset,top_1+top_offset,left_3-left_offset,top_2-top_offset))

    out_c1_name = file_name+"_c1.jpg"
    out_c2_name = file_name+"_c2.jpg"
    left_img.save(output_dir+out_c1_name, "JPEG")
    right_img.save(output_dir+out_c2_name, "JPEG")


file_list = []
input_dir = "input"
for file in os.listdir(input_dir):
    file_no_extention = os.path.splitext(file)[0]
    if file_no_extention not in file_list:
        file_list.append(file_no_extention)
for file_name in file_list:
    try:
        crop_image(file_name,"output/",input_dir)
    except:
        print(file_name + " got err")

