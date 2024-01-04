from layers.model.RecordFormatter import RecordFormatter


class DefaultRecordFormatter(RecordFormatter):
    def format(self, record):
        # Default record formatter implementation
        formatted_record = f"Ref Date: {record.ref_date}\n" \
                           f"Geo: {record.geo}\n" \
                           f"DGUID: {record.dguid}\n" \
                           f"Type of Product: {record.type_of_product}\n" \
                           f"Type of Storage: {record.type_of_storage}\n" \
                           f"UOM: {record.uom}\n" \
                           f"UOM ID: {record.uom_id}\n" \
                           f"Scalar Factor: {record.scalar_factor}\n" \
                           f"Scalar ID: {record.scalar_id}\n" \
                           f"Vector: {record.vector}\n" \
                           f"Coordinate: {record.coordinate}\n" \
                           f"Value: {record.value}\n" \
                           f"Status: {record.status}\n" \
                           f"Symbol: {record.symbol}\n" \
                           f"Terminated: {record.terminated}\n" \
                           f"Decimals: {record.decimals}"
        return formatted_record
