import os
from pickletools import optimize
from PIL import Image
import pillow_avif

current_path = os.path.dirname(os.path.abspath(__file__))
formats_to_convert = ('avif', 'webp')
files_to_convert = []
output_path = os.path.join(current_path, 'output')

if not os.path.exists(output_path):
    os.makedirs(output_path)

# Get list of files to convert from current path
dir_list = os.listdir(current_path)

for file_name in dir_list:
    if file_name.endswith(formats_to_convert):
        files_to_convert.append(file_name)

print(f"Files to convert: {files_to_convert}")

# Convert files in a loop to gif
for file in files_to_convert:
    file_name, extension = os.path.splitext(file)
    path_to_save = os.path.join(output_path, f'{file_name}.gif')
    im = Image.open(file)
    im.info.pop('background', None)
    # Fix quality
    im.save(path_to_save, 
            'gif', save_all=True, 
            loop=0, 
            optimize=True)
    