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

### Detailed Changes

#### 1. Creation of `LibraryManager` Class

- **File**: `library_manager.py`
- **Responsibilities**:
  - Manage the library data.
  - Add, delete, and search for books.
  - Load and save data to/from a CSV file.