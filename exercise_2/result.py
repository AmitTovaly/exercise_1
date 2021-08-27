import os
import shutil
from py7zr import unpack_7zarchive
from setuptools import glob

root_dir = os.path.dirname(os.path.abspath(__file__))

# unzip
shutil.register_unpack_format('7zip',['.7z'],unpack_7zarchive)
shutil.unpack_archive(root_dir + '/main_folder.7z',root_dir)

# Get all the paths of the photos
photo_paths=glob.glob(root_dir + '/main_folder/**/*.jpg',recursive=True)

# Print image full name
image_full_name=list(map(os.path.basename,photo_paths))
print(list(map(lambda s: s.strip(".jpg"),image_full_name)))

# Print the number of all the  pictures
print("numbers of all the pictures: " + str(len(image_full_name)))

# Print the number of all the folders
folders =glob.glob(root_dir + '/main_folder/*')
print("numbers of all the pictures" + str(len(folders)))

# Print the full paths to all the folders
print("full paths to all the folders: " +str(folders))

# Print dictionary with the key is the name of each picture's parent folder and
# value is a list of all of the pictures inside the parent folder.
find_photos = lambda parent_folder: (parent_folder,glob.glob(parent_folder + '/**/*.jpg', recursive=True))
print("parent_dictionary:" + str(dict(map(find_photos,folders))))


# Print a filtered list with the name of the folders that contains the letter 'i'
folder_names = list(map(os.path.basename , folders))
print(list(filter(lambda folder_name: 'i' in folder_name, folder_names)))