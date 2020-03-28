import random
import os
import tempfile

array_for_files = []


def sort_file(not_sorted_file, sorted_file, max_length_of_line):
    read_file(not_sorted_file, max_length_of_line)
    sorting()
    making_sorted_file(sorted_file)


def read_file(not_sorted_file, max_length_of_line):
    temp_array = []
    if not os.path.exists(not_sorted_file):
        raise FileNotFoundError("File {0} not found.".format(not_sorted_file))
    with open(not_sorted_file, "r") as f:
        for line in f:
            temp_array.append(int(line))
            if len(temp_array) >= max_length_of_line:
                temp_array.sort()
                with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp:
                    temp.writelines("{}\n".format(i) for i in temp_array)
                    array_for_files.append(temp)
                temp_array.clear()


def merge_sort_for_files(temp, file_1, file_2):
    line_from_file1 = file_1.readline()
    line_from_file2 = file_2.readline()
    while line_from_file1 and line_from_file2:
        if int(line_from_file1) > int(line_from_file2):
            temp.writelines(line_from_file2)
            line_from_file2 = file_2.readline()
        else:
            temp.writelines(line_from_file1)
            line_from_file1 = file_1.readline()
    if line_from_file1 is not None:
        while line_from_file1:
            temp.writelines(line_from_file1)
            line_from_file1 = file_1.readline()
    if line_from_file2 is not None:
        while line_from_file2:
            temp.writelines(line_from_file2)
            line_from_file2 = file_2.readline()


def delete_file_from_array(file):
    if os.path.exists(file.name):
        array_for_files.pop(0)
        os.remove(file.name)
    else:
        raise FileNotFoundError("File {0} not found.".format(file))


def sorting():
    while len(array_for_files) > 1:
        with open(array_for_files[0].name, "r") as file_1, open(array_for_files[1].name, "r") as file_2:
            with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp:
                merge_sort_for_files(temp, file_1, file_2)
                array_for_files.append(temp)
        delete_file_from_array(file_1)
        delete_file_from_array(file_2)


def making_sorted_file(sorted_file):
    temp = array_for_files[0]
    with open(sorted_file, "w") as file_for_sorted:
        with open(temp.name, "r") as temp_file:
            file_for_sorted.writelines("{}".format(i) for i in temp_file)
    delete_file_from_array(temp)

