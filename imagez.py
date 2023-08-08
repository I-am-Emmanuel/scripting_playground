from PIL import Image, ImageFilter

img = Image.open('./pokedex/squirtle.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blurry_squirtle.png', 'png') 

new_img = Image.open('./blurry_squirtle.png')

newly_filtered = new_img.filter(ImageFilter.SMOOTH)
newly_filtered.save('smooth_squirtle.png', 'png') 

from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save('blury.png', 'png')


img = Image.open('./pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save('smooth.png', 'png')

print(filtered_img)



img = Image.open('./pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save('smooth.png', 'png')




