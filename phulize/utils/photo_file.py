import os.path
import shutil

from phulize.utils.directory import Directory


class PhotoFile:
    extension = ''
    absolute_path = ''
    name_only = ''
    size = 0
    converted_size = 0

    def __init__(self, name, root):
        self.__name = name
        self.__root = root

        self.__process_extension_file()

    def process(self):
        self.__process_file_name()
        self.__process_absolute_path()
        self.process_size_before()

    def process_size_before(self):
        self.size = os.path.getsize(self.absolute_path + self.extension)

    def process_size_after(self):
        self.converted_size = os.path.getsize(self.absolute_path + self.extension)

    def copy_to(self, new_path, remove_original=True):
        directory = Directory(new_path)
        original = r'{}'.format(self.absolute_path) + self.extension
        target = directory.create(self.__name)

        shutil.copyfile(original, target)

        if remove_original:
            directory = Directory(self.absolute_path + self.extension)
            directory.remove()

        copied_photo = PhotoFile(self.__name, new_path)
        copied_photo.process()
        return copied_photo

    def exists(self):
        return Directory(self.absolute_path + self.extension).exists()

    def __process_file_name(self):
        file_name = self.__name.split('.')
        file_name.pop()
        self.name_only = '.'.join(file_name)

    def __process_extension_file(self):
        self.extension = '.' + self.__name.split('.')[len(self.__name.split('.')) - 1]

    def __process_absolute_path(self):
        directory = Directory(self.__root)
        self.absolute_path = directory.create(self.name_only)
