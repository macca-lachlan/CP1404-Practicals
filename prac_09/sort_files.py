import shutil
import os

EXTENSIONS = ['doc', 'docx', 'png', 'gif', 'txt', 'xls', 'xlsx', 'jpg']


def main():
    os.chdir('FilesToSort')
    # print("Current directory is", os.getcwd())

    storage_locations = []
    for i in range(0, len(EXTENSIONS)):
        folder_name = input("What category would you like to sort {} files into?".format(EXTENSIONS[i]))
        storage_locations.append(folder_name)

    # print(storage_locations)

    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            extension = read_extension(filename)

            for i in range(0, len(EXTENSIONS)):
                if EXTENSIONS[i] == extension:
                    position = i

            move_file(filename, storage_locations[position])


def read_extension(filename):
    extension = ''
    for position, char in enumerate(filename):
        if char == '.':
            for i in range(position + 1, len(filename)):
                extension += filename[i]
    extension = extension
    return extension


def move_file(filename, storage_location):
    try:
        os.mkdir(storage_location)
        shutil.move(filename, storage_location)
    except FileExistsError:
        shutil.move(filename, storage_location)


main()
