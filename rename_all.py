#!/usr/bin/python
import os
import sys


def rename_directories(list_new_name, list_old_name):
    for name in os.listdir(os.getcwd()):
        if os.path.isdir(name) and name[0].islower():
            new_name = name[0].upper() + name[1: len(name)]
            os.rename(name, new_name)
            list_old_name.append(name)
            list_new_name.append(new_name)


def rename_files(list_new_name, list_old_name):
    for name in os.listdir(os.getcwd()):
        if not os.path.isdir(name) and name[0].isupper():
            new_name = name[0].lower() + name[1: len(name)]
            os.rename(name, new_name)
            list_old_name.append(name)
            list_new_name.append(new_name)


def print_list(_list):
    for ind in range(0, len(_list)):
        print(_list[ind], ', ' if len(_list) != ind + 1 else '', sep='', end='')
    print()


def print_changes(list_new_name, list_old_name, rename_what):
    the_first_warning = "The " + rename_what + " was renamed"
    the_second_warning = "The new " + rename_what
    if list_new_name.__len__() != 1 or list_old_name.__len__() != 1:
        rename_what = 'directories' if rename_what == 'directory' else 'files'

        the_first_warning = "The " + rename_what + " were renamed"
        the_second_warning = "The new " + rename_what

    if list_new_name.__len__() != 0 or list_old_name.__len__() != 0:
        print(the_first_warning, end=': ')
        print_list(list_old_name)

        print(the_second_warning, end=': ')                
        print_list(list_new_name)
    

def __main__():
    for step in range(2):
        rename_what = "directories" if step == 0 else "files" 
        list_old_name = []
        list_new_name = []
        if step == 0:
            rename_directories(list_new_name, list_old_name)
        else:
            rename_files(list_new_name, list_old_name)
        print_changes(list_new_name, list_old_name, "directory" if step == 0 else "file")


if __name__ == "__main__":
    __main__();
