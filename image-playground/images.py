from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')  # gives a grayscale img.
crooked = filtered_img.rotate(90)
# resized = filtered_img.resize((300, 300)) # acceps a tuple

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)

# filtered_img.save("gray.png", "png")
crooked.save("crooked.png", "png")
crooked.show()
