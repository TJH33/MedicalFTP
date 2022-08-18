# Author: Charlie
# This file checks the filename provided.
# Filename convention:
# MED_DATA_YYYYMMDDHHMMSS.csv
# Example:
# MED_DATA_20210505201229.csv

# Libraries imported
import re


# Main Function --------------------------------------------------------------------------------------------------------

# Define the function and pass in the filename.
def is_valid_filename(filename):
    is_valid = False
    regex = "^MED_DATA_([0-9]{4})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])([0-1][0-9]|2[0-3])([0-5][0-9]){2}.csv$"
    if len(filename) == 27 and re.search(regex, filename):
        is_valid = True
    print(is_valid)
    return is_valid
