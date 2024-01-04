from layers.model.RecordFormatter import RecordFormatter


class CustomRecordFormatter(RecordFormatter):
    def format(self, record):
        # Custom record formatter implementation
        formatted_record = f"Ref Date: {record.ref_date}\n" \
                           f"Geo: {record.geo}\n" \
                           f"DGUID: {record.dguid}\n" \
                           f"Type of Product: {record.type_of_product}\n" \
                           f"UOM: {record.uom}\n" \
                           f"Value: {record.value}"
        return formatted_record
