# test_data_manager.py

import unittest
import csv
import os

from layers.tests.test_record import create_record_file


class CreateRecordFileTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test case
        self.filename = "test_dataset.csv"

    def tearDown(self):
        # Clean up after the test case
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_create_record_file(self):
        # Test the create_record_file function

        # Prepare records and fieldnames for the test
        records = [
            {"name": "Juho Lee", "age": "24", "college": "Algonquin College"},
            {"name": "Jane Smith", "age": "30", "college": "XYZ College"},
            {"name": "Michael Johnson", "age": "22", "college": "123 College"}
        ]
        fieldnames = ["name", "age", "college"]

        # Call the function to create the record file
        create_record_file(self.filename, records, fieldnames)

        # Check if the file exists
        self.assertTrue(os.path.exists(self.filename))

        # Read the contents of the file
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            file_records = list(reader)

        # Verify the number of records in the file
        self.assertEqual(len(file_records), 3)

        # Verify the content of each record
        self.assertEqual(file_records[0]["name"], "Juho Lee")
        self.assertEqual(file_records[0]["age"], "24")
        self.assertEqual(file_records[0]["college"], "Algonquin College")

        self.assertEqual(file_records[1]["name"], "Jane Smith")
        self.assertEqual(file_records[1]["age"], "30")
        self.assertEqual(file_records[1]["college"], "XYZ College")

        self.assertEqual(file_records[2]["name"], "Michael Johnson")
        self.assertEqual(file_records[2]["age"], "22")
        self.assertEqual(file_records[2]["college"], "123 College")

if __name__ == '__main__':
    unittest.main()
