# Book Class
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id}) - {'Available' if self.available else 'Not Available'}"

# Base LibraryMember Class
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self._borrowed_books = []

    def borrow_book(self, book):
        if len(self._borrowed_books) >= self.get_borrow_limit():
            print(f"{self.name} has reached the borrowing limit.")
            return
        if book.available:
            book.available = False
            self._borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is currently not available.")

    def return_book(self, book):
        if book in self._borrowed_books:
            book.available = True
            self._borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

    def get_borrow_limit(self):
        return 2  # default limit

    def list_borrowed_books(self):
        return [book.title for book in self._borrowed_books]

# StudentMember Class
class StudentMember(LibraryMember):
    def get_borrow_limit(self):
        return 3

# TeacherMember Class
class TeacherMember(LibraryMember):
    def get_borrow_limit(self):
        return 5

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def add_member(self, member):
        self.members.append(member)
        print(f"New member: {member.name}")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f" - {book}")

    def list_members(self):
        print("Registered Members:")
        for member in self.members:
            print(f" - {member.name} (ID: {member.member_id})")
