# Define the record object (Model Layer)
from layers.model.record_formatter import RecordFormatter


class Record:
    def __init__(self, ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id,
                 vector, coordinate, value, status, symbol, terminated, decimals):
        # Initialize the record object with the provided attributes
        self.ref_date = ref_date
        self.geo = geo
        self.dguid = dguid
        self.type_of_product = type_of_product
        self.type_of_storage = type_of_storage
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals

    def display_formatted_record(self, formatter: RecordFormatter):
        # Display the record in the specified format using the provided formatter
        formatted_record = formatter.format(self)
        print(formatted_record)
