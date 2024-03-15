import os
from pickletools import optimize
from PIL import Image
import pillow_avif

current_path = os.path.dirname(os.path.abspath(__file__))
formats_to_convert = ('avif', 'webp')
files_to_convert = []
input_path = os.path.join(current_path, 'input')
output_path = os.path.join(current_path, 'output')

if not os.path.exists(output_path):
    os.makedirs(output_path)

# Get list of files to convert from current path
dir_list = os.listdir(input_path)

for file_name in dir_list:
    if file_name.endswith(formats_to_convert):
        files_to_convert.append(os.path.join(input_path, file_name))

print(f"Files to convert: {files_to_convert}")

# Convert files in a loop to gif
for file_path in files_to_convert:
    file_path_no_ext, extension = os.path.splitext(file_path)
    file_name = os.path.split(file_path_no_ext)[1]
    path_to_save = os.path.join(output_path, f'{file_name}.gif')
    im = Image.open(file_path)
    im.info.pop('background', None)
    # Fix quality
    im.save(path_to_save, 
            'gif', 
            save_all=True,
            disposal=2, 
            loop=0,
            optimize=True)
    