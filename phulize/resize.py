from PIL import Image
import PIL
import piexif

import sys
import os
from datetime import datetime

from phulize.utils.operating_system import OperatingSystem, OperatingSystemEnum


class Resize:
    def __init__(self, root, photo, percentage):
        self.root = root
        self.photo = photo
        self.percentage = percentage

    def do(self):
        path = self.root + self.get_correct_slash_symbol() + self.photo.name_only + self.photo.extension
        try:
            if not self.is_image_valid(path):
                print('The image: ' + path + ', it\'s not a valid image file. Could be corrupted')
                return False

            image = Image.open(path)
            
            file_info = os.stat(path)
            
            if 'IMG' in self.photo.name_only:

                photo_title_splitted = self.photo.name_only.split('_')
                print (photo_title_splitted)
                year = photo_title_splitted[1][0:4]
                month = photo_title_splitted[1][4:6]
                day = photo_title_splitted[1][6:]
                hour = photo_title_splitted[2][0:2]
                minutes = photo_title_splitted[2][2:4]
                seconds = photo_title_splitted[2][4:]

                filename = path
                exif_dict = piexif.load(filename)
                new_date = datetime(int(year), int(month), int(day), int(hour), int(minutes), int(seconds)).strftime("%Y:%m:%d %H:%M:%S")
                piexif.remove(filename)

                exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
                exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
                exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
                exif_bytes = piexif.dump(exif_dict)

            quality = (84 * self.percentage / 100)
            image.save(path, quality=round(quality), optimize=True)
            self.photo.process_size_after()
            image.close()
            
            if 'IMG' in self.photo.name_only:
                piexif.insert(exif_bytes, filename)

            if not self.is_image_valid(path):
                print('The image: ' + path + ', it\'s not a valid image file. Could be corrupted')
                return False

            return True
        except (ValueError, OSError, TypeError) as e:
            print('Error resizing ' + path)
            print('Forward the following error to this package\'s author:')
            print(e)
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

    def get_correct_slash_symbol(self):
        operating_system = OperatingSystem().get_current()
        
        if operating_system == OperatingSystemEnum.LINUX:
            return '/'
        
        return '\\'