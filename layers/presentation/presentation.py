import csv
import matplotlib.pyplot as plt
from layers.business.data_manager import DataManager


class Presentation:
    def __init__(self):
        # Initialize the Presentation class with a DataManager instance
        self.data_manager = DataManager()

    def print_full_name(self):
        # Print the full name
        print("Juho Lee")

    def display_menu(self):
        # Display the menu options
        print("Menu:")
        print("1. Reload data from dataset")
        print("2. Persist data to disk")
        print("3. Select and display record(s)")
        print("4. Create a new record")
        print("5. Select and edit a record")
        print("6. Select and delete a record")
        print("7. Display Horizontal Bar Chart")
        print("0. Exit")

    def run(self):
        # Run the presentation layer

        self.print_full_name()
        self.data_manager.load_data("dataset.csv")

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.data_manager.load_data("dataset.csv")
                print("Data reloaded!")
            elif choice == '2':
                filename = input("Enter the filename to save the data: ")
                self.data_manager.save_data(filename)
                print("Data saved to disk!")
            elif choice == '3':
                start = int(input("Enter the starting index: "))
                end = int(input("Enter the ending index: "))
                self.data_manager.display_records(start, end)
            elif choice == '4':
                ref_date = input("Enter the ref_date: ")
                geo = input("Enter the geo: ")
                dguid = input("Enter the dguid: ")
                type_of_product = input("Enter the type_of_product: ")
                type_of_storage = input("Enter the type_of_storage: ")
                uom = input("Enter the uom: ")
                uom_id = input("Enter the uom_id: ")
                scalar_factor = input("Enter the scalar_factor: ")
                scalar_id = input("Enter the scalar_id: ")
                vector = input("Enter the vector: ")
                coordinate = input("Enter the coordinate: ")
                value = input("Enter the value: ")
                status = input("Enter the status: ")
                symbol = input("Enter the symbol: ")
                terminated = input("Enter the terminated: ")
                decimals = input("Enter the decimals: ")

                self.data_manager.create_record(ref_date, geo, dguid, type_of_product, type_of_storage,
                                                uom, uom_id, scalar_factor, scalar_id, vector, coordinate,
                                                value, status, symbol, terminated, decimals)
                print("Record created!")
            elif choice == '5':
                index = int(input("Enter the index of the record to edit: "))
                record_data = input("Enter the new record data (comma-separated): ").split(',')
                self.data_manager.edit_record(index, record_data)
                print("Record edited!")
            elif choice == '6':
                index = int(input("Enter the index of the record to delete: "))
                self.data_manager.delete_record(index)
                print("Record deleted!")
            elif choice == '7':
                self.display_horizontal_bar_chart()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_horizontal_bar_chart(self):
        # Display a horizontal bar chart representing total quantity of each product by geographical location
        data = self.data_manager.get_total_quantity_by_geo_and_product()

        for geo, products in data.items():
            products_list = list(products.keys())
            quantities = list(products.values())

            plt.barh(products_list, quantities)
            plt.xlabel("Total Quantity")
            plt.ylabel("Type of Product")
            plt.title(f"Total Quantity of Products in {geo}")
            plt.show()

