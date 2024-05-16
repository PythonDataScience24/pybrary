import gooeypie as gp
from library_manager import LibraryManager
from gui import LibraryGUI


def main():
    # Initialize the main application window
    pybrary = gp.GooeyPieApp('pybrary')

    # Create the Library Manager
    library_manager = LibraryManager()

    # Create the GUI
    library_gui = LibraryGUI(pybrary, library_manager)

    # Run the application
    pybrary.run()


if __name__ == "__main__":
    main()
