from layers.presentation.presentation import Presentation
from layers.business.data_manager import DataManager

# Run the program
if __name__ == '__main__':
    """
    Entry point of the program.

    This code creates an instance of the Presentation class and runs the program by calling the run() method.
    The Presentation class handles the user interface and interacts with the DataManager class, which manages the data.

    Example:
        python main.py
    """

    presentation = Presentation()
    presentation.run()

    # # Run the unit test
    # test_data_manager()
