from PIL import Image, ImageFilter
import sys
import os


pics_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for item in os.listdir(pics_folder):
    newImg = Image.open(f'{pics_folder}{item}')
    cleaned_img = os.path.splitext(item)[0]
    newImg.save(f'{output_folder}{cleaned_img}.png', 'png')
    print('done!')
    
