from PIL import Image

image = Image.open("monro.jpg")
print('Ширина -', image.width)
print('Высота -', image.height)
print('Цветовая модель - ', image.mode)

red, green, blue = image.split()

coordinates_red = (100,0, red.width, red.height)
cropped_red = red.crop(coordinates_red)
coordinates_red_1 = (50, 0 , red.width-50, red.height)
cropped_red_old = red.crop(coordinates_red_1)
blended_red = Image.blend(cropped_red, cropped_red_old,0.5)
coordinates_blue = (0,0,blue.width-100,blue.height)
cropped_blue = blue.crop(coordinates_blue)
coordinates_blue_1 = (50, 0 , blue.width-50, blue.height)
cropped_blue_old = red.crop(coordinates_blue_1)
blended_blue = Image.blend(cropped_blue, cropped_blue_old,0.5)
coordinates_green = (50,0, green.width-50, green.height)
cropped_green = green.crop(coordinates_green)

new_image = Image.merge("RGB", (cropped_red, cropped_green, cropped_blue))
new_image.thumbnail((80,80))
new_image.save('avatar.jpg')
