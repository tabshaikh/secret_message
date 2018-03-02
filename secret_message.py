import os


def rename_files ():
    file_list = os.listdir("./prank")
    table = str.maketrans(dict.fromkeys('0123456789'))  # The to make the list of all excluded alphabets
    saved_path = os.getcwd()
    print("The current working directory is:"+saved_path)
    os.chdir("./prank")
    saved_path = os.getcwd()
    print("The current working directory is:"+saved_path)
    print(file_list)
    for file in file_list:
        os.rename(file, file.translate(table))


rename_files()