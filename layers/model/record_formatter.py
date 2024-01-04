# record_formatter.py

# Define the base class for record formatters
class RecordFormatter:
    def format(self, record):
        # Abstract method for formatting a record
        pass

# Define a sub-class for a specific record format
class DefaultRecordFormatter(RecordFormatter):
    def format(self, record):
        # Perform formatting specific to the default format
        formatted_record = f"Default Format: {record.ref_date}, {record.geo}, {record.dguid}"
        return formatted_record

# Define another sub-class for a different record format
class CustomRecordFormatter(RecordFormatter):
    def format(self, record):
        # Perform formatting specific to the custom format
        formatted_record = f"Custom Format: {record.geo}, {record.ref_date}, {record.dguid}"
        return formatted_record
