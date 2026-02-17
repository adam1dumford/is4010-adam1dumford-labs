class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize the Book object.
        """
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        """
        Calculates the age of the book based on the current year (2025).
        """
        return 2025 - self.year

    def __str__(self):
        """
        String representation method.
        Returns a formatted string: "Title" by Author (Year)
        """
        return f'"{self.title}" by {self.author} ({self.year})'


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        """
        Constructor for EBook.
        Uses super() to handle title, author, and year, then handles file_size.
        """
        # Call the parent class (Book) constructor first
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """
        Overrides the parent string method to include file size.
        """
        # Get the string from the parent class first
        book_string = super().__str__()
        # Append the file size information
        return f"{book_string} ({self.file_size} MB)"


if __name__ == "__main__":
    # 1. Create and print a standard Book instance
    my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    print("Standard Book:")
    print(my_book)
    print(f"Age: {my_book.get_age()} years old\n")

    # 2. Create and print an EBook instance
    my_ebook = EBook("The Martian", "Andy Weir", 2011, 2)
    print("EBook:")
    print(my_ebook)
    
    # 3. Verify EBook inherited the get_age method correctly
    print(f"EBook Age: {my_ebook.get_age()} years old")