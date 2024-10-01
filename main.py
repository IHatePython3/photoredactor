from PIL import Image

image = Image.open("monro.jpg")
print('Ширина -', image.width)
print('Высота -', image.height)
print('Цветовая модель - ', image.mode)




red, green, blue = image.split()

red.save('red.jpg')
green.save('green.jpg')
blue.save('blue.jpg')

new_image = Image.merge("RGB", (red, green, blue))
new_image.save('new.jpg')

imagine_red = Image.open('red.jpg')
cropped_red = imagine_red.crop((0,0,645,522))
imagine_blue = Image.open('blue.jpg')
cropped_blue = imagine_blue.crop((100,0,745,522))
cropped_blue.save('cropped_blue.jpg')
cropped_red.save('cropped_red.jpg')

image_red = Image.open('cropped_red.jpg')
image_blue = Image.open('cropped_blue.jpg')
image_blended = Image.blend(image_red, image_blue, 0.5)
image_blended.save('blended_blue.jpg')


cropped_red_ = imagine_red.crop((100,0,745,522))
cropped_blue_ =  imagine_blue.crop((0,0,645,522))
cropped_blue_.save('cropped_blue_left.jpg')
cropped_red_.save('cropped_red_right.jpg')

images_red = Image.open('cropped_red_right.jpg')
images_blue = Image.open('cropped_blue_left.jpg')
image_blended2 = Image.blend(images_red, images_blue, 0.5)
image_blended2.save('blended_red.jpg')





imagine_green = Image.open('green.jpg')
cropped_green = imagine_green.crop((50, 0, 645, 522 ))
cropped_green.save('cropped_green.jpg')
image_green = Image.open("cropped_red.jpg")
new_converted_image = Image.merge("RGB", (image_red, image_blue, image_green))
new_converted_image.save('blended_rgb.jpg')