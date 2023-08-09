from PIL import Image, ImageFilter

img = Image.open('./pokedex/squirtle.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blurry_squirtle.png', 'png') 

new_img = Image.open('./blurry_squirtle.png')

newly_filtered = new_img.filter(ImageFilter.SMOOTH)
newly_filtered.save('smooth_squirtle.png', 'png') 

img0 = Image.open('./pokedex/pikachu.jpg')

filtered_img0 = img0.filter(ImageFilter.BLUR)

filtered_img0.save('blury.png', 'png')


img2 = Image.open('./pokedex/pikachu.jpg')

filtered_img2 = img2.filter(ImageFilter.SMOOTH)

filtered_img2.save('smooth.png', 'png')

print(filtered_img)



img1 = Image.open('./pokedex/pikachu.jpg')

filtered_img1 = img1.filter(ImageFilter.SMOOTH)

filtered_img1.save('smooth.png', 'png')


con_img = Image.open('./pokedex/pikachu.jpg')

convert_img = con_img.convert('P')
convert_img.save('brown.png', 'png')


# con_img1 = Image.open('./pokedex/pikachu.jpg')

# convert_img1 = con_img1.convert('L')
# rotat = convert_img1.rotate(90)
# rresiz = rotat.resize((300, 300))
# .save('geez.png', 'png')
# box = (100, 100, 400, 400)
# cropedPikca = convert_img1.crop(box)
# cropedPikca.show()
# rresiz.show()


astronaut = Image.open('./astro.jpg')
# print(astronaut.size)
# astronaut.show()
astronaut.thumbnail((400, 400))
# print(astronaut.size)
astronaut.save('resized.jpg')
astronaut.show()



