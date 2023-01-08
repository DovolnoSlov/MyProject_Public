import os

for elem, dirs, files in os.walk(os.path.join(os.path.abspath('.'), 'file')):
    for file in files:
        if file[-4:] == '.txt':
            current_path_name = os.path.join(elem, file)
            new_path_name = os.path.join(elem, '!' + file)
            os.rename(current_path_name, new_path_name)
