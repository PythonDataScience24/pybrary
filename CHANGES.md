# Changes in Pybrary Project

## Refactoring Single Class to Multiple Classes

### Overview

In the initial implementation of the Pybrary project, the entire functionality was contained within a single script. This included both the user interface (UI) logic and the library management logic. To improve the modularity, readability, and maintainability of the code, we refactored the project into multiple classes, each with a specific responsibility.

### Changes Made

1. **Separation of Concerns**: 
   - The original code had all the logic for managing the library and the UI in one place. We separated these concerns by creating distinct classes for managing the library data and handling the UI.

2. **New Classes**:
   - **LibraryManager**: This class is responsible for all operations related to managing the library data, such as adding, deleting, searching, loading, and saving books.
   - **LibraryGUI**: This class is responsible for creating and managing the graphical user interface (GUI) of the application.
   - **Librarian**: This class handles the storing, deleting and overwriting of books, so it is not done in the GUI directly.
   - **Pybrary**: This class integrates all the components together.

### Detailed Changes

#### 1. Creation of `LibraryManager` Class

- **File**: `library_manager.py`
- **Responsibilities**:
  - Manage the library data.
  - Add, delete, and search for books.
  - Load and save data to/from a CSV file.

#### 2. Creation of `Librarian` Class

- **File**: `librarian.py`
- **Responsibilities**:
  - Call functions of the `LibraryManager` when buttons are pressed.

#### 3. Creation of `LibraryGUI` Class

- **File**: `gui.py`
- **Responsibilities**:
  - Create and manage the graphical user interface.
  - Handle user interactions and events.

#### 4. Creation of `Pybrary` Class

- **File**: `pybrary.py`
- **Responsibilities**:
  - Integrate all the components (`LibraryManager`, `LibraryGUI`, and `Librarian`) together.
  - Serve as the entry point for the application.

### Bug Fixes and Improvements

1. **GUI Bug Fixes**:
   - Fixed the delete button functionality.
   - Added exception handling to prevent empty fields in Author or Year.
   - Implemented a pop-up error message for exceptions.

2. **Rating Validation**:
   - Ensured that the book rating can only be between 1 and 5.
   - Invalid inputs (including characters in the Year field) are now properly handled.

3. **New Tab for Visualizations**:
   - Added a new tab with simple visualizations using Matplotlib.

4. **Improved Search Function**:
   - Enhanced the search functionality to allow searching by pages, author, or genre.

5. **Unit Testing**:
   - Created a test class `book_test.py` with simple unit tests.

6. **Resizable GUI**:
   - Made the GUI resizable for better user experience.
