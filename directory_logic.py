# Author: Thomas H2
# This scripts performs the logic for creating/moving the directories in a logical way

import os
import shutil

pwd = os.path.dirname(__file__)
joined_valid = os.path.join(pwd, 'Valid')
joined_temp = os.path.join(pwd, 'Temp')

def move_to_temp(file_list):
    # placing them all into temp folder

    if (os.path.exists(joined_temp) is False):
        os.mkdir(joined_temp)
    
    for file_name in file_list:
        try:
            shutil.move(os.path.join(pwd, file_name), joined_temp)
        except:
            return False
    
    return True


def move_to_valid(file_list):
    # checking if the pre-requsite file directories exist

    if (os.path.exists(joined_valid) is False):
        os.mkdir(joined_valid)
    
    #going through and grabbing the month year, appending the directories
    
    for file_name in file_list:
        join_year = os.path.join(joined_valid, file_name[9:13])
        join_month = os.path.join(join_year, file_name[13:15])
        if (os.path.exists(join_year) is False):
            os.mkdir(join_year)
        if (os.path.exists(join_month) is False):
            os.mkdir(join_month)
            
        full_file_path = os.path.join(joined_valid, file_name[9:13], file_name[13:15])
        try:
            shutil.move(os.path.join(joined_temp, file_name), full_file_path)
        except:
            return False
    
    return True