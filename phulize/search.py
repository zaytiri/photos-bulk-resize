from phulize.output import Output
from phulize.resize import Resize
from phulize.utils.directory import Directory
from phulize.utils.folder_hierarchy import FolderHierarchy
from phulize.utils.photo_file import PhotoFile


class Search:
    def __init__(self, arguments):
        self.path = arguments.path.value
        self.extensions = arguments.extensions.value
        self.cloned_folder = arguments.folder.value
        self.percentage = arguments.quality.value
        self.higher = arguments.higher.value
        self.below = arguments.below.value

        self.folder_hierarchy = FolderHierarchy(self.path)
        self.output = Output()

    def search(self):
        main_directory = Directory(self.path)
        found_files = False

        self.folder_hierarchy.create_parent(self.cloned_folder)

        for root, dirs, files in main_directory.search_through():
            for photo in files:
                current_photo = PhotoFile(photo, root)

                if not self.is_valid(current_photo):
                    continue

                found_files = True

                current_photo.process()

                self.resize(current_photo, root)

        if found_files:
            self.output.process(main_directory.root)
            print('\nAn output file with a summary was created in the following directory: \n\t\t' + self.output.file.path + '')
        else:
            print('\nNo files were found with defined extensions.')

    def is_valid(self, photo):
        if photo.extension not in self.extensions:
            return False

        is_valid = False
        if photo.size > self.higher:
            is_valid = True

        if self.below == 0 or (self.below != 0 and photo.size < self.below):
            is_valid = True

        return is_valid

    def resize(self, photo, root):
        print('\nResizing ' + photo.absolute_path + photo.extension + '...')

        new_folder = self.folder_hierarchy.duplicate(root)
        copied_photo = photo.copy_to(new_folder, remove_original=False)

        resize = Resize(root, photo, self.percentage)
        successful = resize.do()

        if not successful:
            copied_photo.copy_to(root)
            self.output.add_unsuccessful_file(photo.absolute_path + photo.extension)
            print('Encoding unsuccessful.')
        else:
            self.output.add_file(photo)
            print('Encoding successfully done!')
