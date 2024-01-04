# Import necessary libraries
import csv

# Import the Record class
from layers.model.record import Record
from layers.model.record_formatter import RecordFormatter, DefaultRecordFormatter


# Define the data manager (Business Layer)
class DataManager:
    def __init__(self):
        self.records = []

        def format_records(self, formatter: RecordFormatter = DefaultRecordFormatter()):
            for record in self.records:
                record.display_formatted_record(formatter)

    def load_data(self, dataset):
        # Load data from a dataset CSV file
        try:
            with open(dataset, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    record = Record(*row)
                    self.records.append(record)
        except FileNotFoundError:
            print(f"File '{dataset}' not found!")

    def save_data(self, dataset):
        # Save data to a CSV file
        try:
            with open(dataset, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                for record in self.records:
                    csv_writer.writerow([
                        record.ref_date, record.geo, record.dguid, record.type_of_product, record.type_of_storage,
                        record.uom, record.uom_id, record.scalar_factor, record.scalar_id, record.vector,
                        record.coordinate, record.value, record.status, record.symbol, record.terminated,
                        record.decimals
                    ])
        except PermissionError:
            print("Permission denied!")

            def get_total_quantity_by_geo_and_product(self):
                # Calculate total quantity of each product for each geographical location
                data = {}
                for record in self.records:
                    geo = record.geo
                    product = record.type_of_product
                    value = float(record.value)

                    if geo not in data:
                        data[geo] = {}

                    if product not in data[geo]:
                        data[geo][product] = 0

                    data[geo][product] += value

                return data

    def display_records(self, start_index, end_index):
        # Display a range of records
        for i in range(start_index, end_index):
            if i >= len(self.records):
                break
            record = self.records[i]
            print(f"Record {i + 1}:")
            print(f"Ref Date: {record.ref_date}")
            print(f"Geo: {record.geo}")
            print(f"DGUID: {record.dguid}")
            # Display other fields

    def create_record(self, ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor,
                      scalar_id, vector, coordinate, value, status, symbol, terminated, decimals):
        # Create a new record object with provided arguments and add it to the records list
        record = Record(ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id,
                        vector, coordinate, value, status, symbol, terminated, decimals)
        self.records.append(record)

    def edit_record(self, index, record_data):
        # Edit an existing record at the specified index
        if index < len(self.records):
            record = Record(*record_data)
            self.records[index] = record

    def delete_record(self, index):
        # Delete a record at the specified index
        if index < len(self.records):
            del self.records[index]

    def get_total_quantity_by_geo_and_product(self):
        # Calculate total quantity of each product for each geographical location
        data = {}
        for record in self.records:
            geo = record.geo
            product = record.type_of_product
            value = record.value

            if value.strip() == '':
                continue

            value = float(value)

            if geo not in data:
                data[geo] = {}

            if product not in data[geo]:
                data[geo][product] = 0

            data[geo][product] += value

        return data