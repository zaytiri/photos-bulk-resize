from datetime import date, datetime

from phulize.utils.bytes_conversion import set_converted_bytes_with_label
from phulize.utils.file import File


class Output:
    original_photos_size = 0.0
    reduced_photos_size = 0.0
    photos_not_reduced = []
    number_photos_increased = 0
    number_photos_reduced = 0
    photos = []
    file = None

    def __add_file_information(self, timestamp, photo):
        self.__add_line('[' + str(timestamp) + ']\nThe following photo was resized: ' + photo.absolute_path)

        self.__set_message_with_size('\t-The original photo size was: ', photo.size)
        self.__set_message_with_size('\t-The resized photo size is: ', photo.converted_size)

        space_saved = photo.size - photo.converted_size
        if space_saved < 0:
            self.number_photos_increased += 1
            self.__add_line('\t\t[WARNING] Size increased!')
        else:
            self.number_photos_reduced += 1

        self.__add_line('\n')
        self.original_photos_size += photo.size
        self.reduced_photos_size += photo.converted_size

    def add_file(self, photo):
        self.photos.append({
            'timestamp': datetime.utcnow(),
            'photo': photo
        })

    def add_unsuccessful_file(self, unsuccessful_file_path):
        self.photos_not_reduced.append(unsuccessful_file_path)

    def process(self, absolute_path_parent):
        date_now = '[' + str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day) + ' ' + str(
            datetime.utcnow().hour) + '-' + str(
            datetime.utcnow().minute) + '-' + str(datetime.utcnow().second) + ']'
        self.file = File(absolute_path_parent + '\\output' + date_now + '.txt')
        self.file.open('a')

        for photo in self.photos:
            self.__add_file_information(photo['timestamp'], photo['photo'])

        self.__add_line('[' + str(datetime.utcnow()) + ']\nFinal Statistics:')
        self.__set_message_with_size('\tSize of all original photos: ', self.original_photos_size)
        self.__set_message_with_size('\tSize of all resized photos: ', self.reduced_photos_size)

        space_saved = self.original_photos_size - self.reduced_photos_size
        if space_saved > 0:
            self.__set_message_with_size('\tSpace in disk saved: ', space_saved)

        self.__add_line('\n\t- Total number of photos with reduced size: ' + str(self.number_photos_reduced))
        self.__add_line('\t- Total number of photos with increased size: ' + str(self.number_photos_increased))
        self.__add_line('\t- Total number of photos unsuccessfully reduced: ' + str(len(self.photos_not_reduced)))
        total = self.number_photos_reduced + len(self.photos_not_reduced) + self.number_photos_increased
        self.__add_line('\t- Total number of photos found: ' + str(total))

        if len(self.photos_not_reduced) != 0:
            self.__add_line('\n\tThe following photos were not reduced successfully:')
            for file in self.photos_not_reduced:
                self.__add_line('\t--> ' + file)

        self.file.close()

    def __set_message_with_size(self, message, size):
        size_with_label = set_converted_bytes_with_label(size)
        self.__add_line(message + '%.2f' % size_with_label['size'] + ' ' + size_with_label['label'])

    def __add_line(self, message):
        self.file.write(message + '\n')
