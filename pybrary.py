import gooeypie as gp

from librarian import Librarian
from library_manager import LibraryManager
from gui import LibraryGUI


def main():
    # Initialize the main application window
    pybrary = gp.GooeyPieApp('pybrary')

    # Create the Library Manager
    library_manager = LibraryManager()

    librarian = Librarian(pybrary, library_manager)

    # Create the GUI
    library_gui = LibraryGUI(pybrary, library_manager, librarian)

    # Run the application
    pybrary.run()


if __name__ == "__main__":
    main()
