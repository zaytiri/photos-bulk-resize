import PIL
from PIL import Image


class Resize:
    def __init__(self, root, photo, percentage):
        self.root = root
        self.photo = photo
        self.percentage = percentage

    def do(self):
        path = self.root + '\\' + self.photo.name_only + self.photo.extension
        try:
            if not self.is_image_valid(path):
                print('The image: ' + path + ', it\'s not a valid image file. Could be corrupted')
                return False

            image = Image.open(path)
            quality = (84 * self.percentage / 100)
            image.save(path, quality=round(quality), optimize=True)
            self.photo.process_size_after()
            image.close()

            if not self.is_image_valid(path):
                print('The image: ' + path + ', it\'s not a valid image file. Could be corrupted')
                return False

            return True
        except (ValueError, OSError, TypeError):
            print('Error resizing ' + path)
            return False

    def is_image_valid(self, path):
        if self.photo.size == 0:
            return False

        try:
            im = Image.open(path)
            im.verify()
            im.close()
            im = Image.open(path)
            im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            im.close()
            return True
        except (ValueError, OSError, TypeError):
            return False
