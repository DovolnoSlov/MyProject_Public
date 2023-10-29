import os


def __Rename_Files(dir_name: str) -> None:
    """
    This function finds the specified directory in the working directory, and renames all files.txt in it

    Args:
        dir_name (str): directory containing files to rename
    """

    dir_path = os.path.join(os.path.abspath('..'), dir_name)
    if not os.path.exists(dir_path):
        raise FileNotFoundError('The specified directory was not found')
    for elem, dirs, files in os.walk(dir_path):
        for file in files:
            if file[-4:] == '.txt':
                current_path_name = os.path.join(elem, file)
                new_path_name = os.path.join(elem, '!' + file)
                os.rename(current_path_name, new_path_name)


def main_rename_fun() -> None:
    """ This function is the main for running the program """

    spec_dir_name = input('Enter the name of the required directory: ')
    #spec_dir_name = 'file2' # ErrorTest

    try:
        __Rename_Files(spec_dir_name)
    except FileNotFoundError as ex:
        print(ex)


if __name__ == "__main__":
    main_rename_fun()