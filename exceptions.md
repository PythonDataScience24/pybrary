# Exception Handling in Pybrary

## Rationale for Exception Handling

Exception handling is a crucial part of any software project to ensure that the application can gracefully handle unexpected situations without crashing. In the Pybrary project, we implemented try and except blocks to manage potential errors that might occur during file operations, such as reading from or writing to a CSV file. Here is the rationale for our decision and how we dealt with exceptions:

### File Operations

When working with file operations, such as reading from or writing to a CSV file, there are several potential issues that can arise, such as:

- The file might not exist.
- The file might be in use by another application.
- There could be permission issues preventing access to the file.
- The file could be corrupted or not in the expected format.

To handle these scenarios, we used try and except blocks in the `LibraryManager` class's `load_csv` and `save_data` methods.

### Implementation

#### load_csv Method

In the `load_csv` method, we handle the `FileNotFoundError` exception to account for the possibility that the CSV file does not exist when the application is first run. By catching this exception, we allow the application to proceed without interruption, and an empty library is initialized.

```python
def load_csv(self):
    try:
        with open('library.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.full_library.append(row)
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist
```
#### save_data Method
In the save_data method, we handle potential IO errors that might occur during the file writing process. This ensures that if an error occurs, it is logged and the application can attempt to recover or inform the user appropriately.

### Data Validation
To ensure data integrity, we validate user inputs for various fields such as year, pages, and rating. If the input is invalid, we raise an exception to inform the user and prevent the application from proceeding with incorrect data.

### User Input Validation
We handle the following cases:

- Empty Input: If a user tries to add a book without providing necessary details.
- Invalid Rating: If the rating of a book is not between 1 and 5.
- Invalid Data Types: If non-numeric values are entered in fields such as year, pages, or rating.

### User Feedback and Logging
Currently, we do not have a robust mechanism for user feedback or logging beyond printing error messages. Enhancing this aspect could involve implementing logging to a file and providing more user-friendly messages via the GUI.

### Fallback Mechanisms
We primarily use try and except blocks to catch exceptions and prevent the application from crashing. There are no advanced fallback mechanisms implemented at this time.

### Testing and Debugging
We ensure the robustness of our exception handling through unit tests. The book_test.py file includes tests for various scenarios to verify that our exception handling works as expected.
