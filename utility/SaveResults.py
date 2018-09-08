import os

from utility.TextColors import print_red


# Saving results to a file
def save_results(results, folder_name, file_name):
    file_name_path = folder_name + "/" + file_name
    try:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        file_to_save = open(file_name_path, 'w')
        file_to_save.write(results)
        file_to_save.close()
    except Exception as e:
        print_red("[!] Error: Cannot save the result to a file! Reasons:\r\n" + str(e))
