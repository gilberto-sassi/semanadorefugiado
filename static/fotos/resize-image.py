from PIL import Image

from resizeimage import resizeimage

fotos = ['lionel', 'penildon', 'sabine', 'mariela', 'carla', 'adriano', 'vladimir', 'aua', 'yasmin', 'javier',
         'anas', 'jean']

for foto in fotos:
    with open(f'{foto}.jpg', 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [200, 200])
            cover.save(f'{foto}-smaller.jpg', image.format)
