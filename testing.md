# Testing.md

## Function: `search_books`

### Description
The `search_books` function in the `LibraryManager` class searches the library for books that match the given title, author, and genre. An unexpected result might occur if the search terms are not correctly converted to lowercase or if there are issues with the search logic.

### Test Cases
1. **Search by Title**
   - **Description**: Ensure the function finds a book by its title.
   - **Input**: `title_search="The gREAT Gatsby", author_search="", genre_search=""`
   - **Expected Output**: `[["The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Novel"]]`

2. **Search by Author**
   - **Input**: `title_search="", author_search="HARPER Lee", genre_search=""`
   - **Expected Output**: `[["To Kill a Mockingbird", "Harper Lee", "Fiction", "Novel"]]`

3. **Search by Genre**
   - **Input**: `title_search="", author_search="", genre_search="dystopian"`
   - **Expected Output**: `[["1984", "George Orwell", "Fiction", "Dystopian"]]`

4. **No Match Found**
   - **Input**: `title_search="Nonexistent Title😀", author_search="", genre_search=""`
   - **Expected Output**: `[]`

## Function: `add_book`

The `add_book` function in the `LibraryManager` class adds a new book to the library. An unexpected result might occur if the function fails to append the new book correctly or handles duplicates incorrectly.

## Function: `delete_book`

The `delete_book` function in the `LibraryManager` class deletes an existing book from the library. An unexpected result might occur if the function fails to remove the book correctly or handles non-existent books incorrectly.
