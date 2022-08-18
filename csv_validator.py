import csv
import re


def validate_csv(file):
    test_criteria = []

    with open(csv.reader) as csv_file:
        file = csv_file.readlines()

        if not validate_header(get_header(file)):
            # If invalid header, patch it on the fly
            file[0] = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                       "reading7", "reading8", "reading9", "reading10"]
            test_criteria.append('Invalid header')
            csv_file.writelines(file)
        batch_ids = []

        for line in file[1:]:
            # Check if batch id is a duplicate
            if id := line[0] not in batch_ids:
                batch_ids.append(id)
            # If duplicate raise an error
            else:
                test_criteria.append('Duplicate batch id')

            if not validate_timestamp(line[1]):
                test_criteria.append('Invalid timestamp')

            readings = line[2:]
            total_readings = 0
            for reading in readings:
                total_readings += 1
                if not validate_float(reading):
                    test_criteria.append('Invalid reading')
                    break

            if total_readings != 10:
                test_criteria.append("Invalid number of readings")

    return test_criteria


def validate_float(num):
    float_regex = "(?:[0-8][0-9]{2}|900))"
    return re.match(float_regex, num)


def validate_timestamp(time):
    time_regex = '\"(?:[0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\"'
    return re.match(time_regex, time)


def validate_header(header):
    valid_header = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6",
                    "reading7", "reading8", "reading9", "reading10"]
    return header == valid_header


def get_header(file):
    return file[0]

