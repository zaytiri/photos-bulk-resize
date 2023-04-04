from phulize.utils.directory import Directory


class FolderHierarchy:
    def __init__(self, root):
        self.__root = root
        self.original = None
        self.clone = None

    def create_parent(self, new_folder):
        self.original = Directory(self.__root)
        new_directory = Directory(self.original.last_folder_path)
        parent_path = new_directory.create_folder(new_folder)
        self.clone = Directory(parent_path)

    def duplicate(self, file_root):
        clone_path = self.clone.root

        path_name_list = file_root.split('\\')
        pass_main_folder = False
        for folder in path_name_list:
            if folder == self.original.current_folder:
                pass_main_folder = True

            if pass_main_folder:
                clone_path = clone_path + '\\' + folder
                self.clone.create_folder(clone_path)

        return clone_path
