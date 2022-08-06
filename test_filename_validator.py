# Author: Charlie
# This file tests 'file_name_validator.py'
# Libraries imported
import pytest
import file_name_validator


# This function tests if a valid filename is accepted.
def test_valid():
    assert file_name_validator.is_valid_filename("MED_DATA_20210505201229.csv") is True


# This function tests if an invalid length is accepted.
def test_length():
    assert file_name_validator.is_valid_filename("MED_DATA_20210505201229X.csv") is False


# This function tests the beginning 'MED_DATA_' check is accurate.
def test_beginning():
    assert file_name_validator.is_valid_filename("M3D_DATA_20210505201229.csv") is False


# This function tests the year section of the filename check only accepts numbers.
def test_year():
    assert file_name_validator.is_valid_filename("MED_DATA_XXXX0505201229.csv") is False


# This function tests the months section of the filename check.
def test_month():
    # This asserts that invalid months '00' and '13' are False.
    assert file_name_validator.is_valid_filename("MED_DATA_20210005201229.csv") is False
    assert file_name_validator.is_valid_filename("MED_DATA_20211305201229.csv") is False
    # This asserts that the months section only accepts numbers.
    assert file_name_validator.is_valid_filename("MED_DATA_2021XX05201229.csv") is False


# This function tests the days section of the filename check.
def test_day():
    # This asserts that invalid days '00' and '32' are False.
    assert file_name_validator.is_valid_filename("MED_DATA_20210500201229.csv") is False
    assert file_name_validator.is_valid_filename("MED_DATA_20210532201229.csv") is False
    # This asserts that the days section only accepts numbers.
    assert file_name_validator.is_valid_filename("MED_DATA_202105XX201229.csv") is False


# This function tests the hours section of the filename check.
def test_hours():
    # This asserts that invalid hours '24' is False.
    assert file_name_validator.is_valid_filename("MED_DATA_20210505241229.csv") is False
    # This asserts that the hours section only accepts numbers.
    assert file_name_validator.is_valid_filename("MED_DATA_20210505XX1229.csv") is False


# This function tests the minutes section of the filename check.
def test_minutes():
    # This asserts that invalid minutes '60' is False.
    assert file_name_validator.is_valid_filename("MED_DATA_20210505206029.csv") is False
    # This asserts that the minutes section only accepts numbers.
    assert file_name_validator.is_valid_filename("MED_DATA_2021050520XX29.csv") is False


# This function tests the seconds section of the filename check.
def test_seconds():
    # This asserts that invalid seconds '60' is False.
    assert file_name_validator.is_valid_filename("MED_DATA_20210505201260.csv") is False
    # This asserts that the seconds section only accepts numbers.
    assert file_name_validator.is_valid_filename("MED_DATA_202105052012XX.csv") is False


# This function tests the extension of the filename.
def test_extension():
    # This asserts that invalid extension '.xml' isn't accepted.
    assert file_name_validator.is_valid_filename("MED_DATA_20210505201229.xml") is False
