# Author: Thomas H2
# Purpose of this script is to test the logic of creating a logical directory 
# Same file was used but was just moved between 

import unittest
import directory_logic as dl

# testing directory logic

class directory_test(unittest.TestCase):

    # test to determine program is resilent to files not being in directory

    def move_to_temp_not_there(self):
        self.assertFalse(dl.move_to_temp(['MED_DATA_20220803153921.csv']))

    # test to determine program is resilent to files being in directory
    def move_to_temp_exists(self):
        self.assertTrue(dl.move_to_temp(['MED_DATA_20220803153921.csv']))
    
    # test to determine if program is resilent to files not being in directory

    def move_to_valid_not_there(self):
        self.assertFalse(dl.move_to_valid(['MED_DATA_20220803153921.csv']))

    # test to determine of program can transfer the files
    def move_to_valid_exists(self):
        self.assertTrue(dl.move_to_valid(['MED_DATA_20220803153921.csv']))

if '__name__' == '__main__':
    unittest.main()
