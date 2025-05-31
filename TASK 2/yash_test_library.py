from yash_library_system import *

# Setup library
central_library = Library()

# Add books
book1 = Book("1984", "George Orwell", 101)
book2 = Book("Python Basics", "John Smith", 102)
book3 = Book("Data Structures", "Alice Brown", 103)
central_library.add_book(book1)
central_library.add_book(book2)
central_library.add_book(book3)

# Add members
student_yash = StudentMember("Yash Nangla", "S001")
teacher_rishabh = TeacherMember("Prof. Rishabh", "T001")
central_library.add_member(student_yash)
central_library.add_member(teacher_rishabh)

# Borrowing books
student_yash.borrow_book(book1)
student_yash.borrow_book(book2)
student_yash.borrow_book(book3) 

teacher_rishabh.borrow_book(book3) 
teacher_rishabh.borrow_book(book2)  
