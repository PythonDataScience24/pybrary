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
