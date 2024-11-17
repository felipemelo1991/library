class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available:
      self.available = False
      return True
    else:
      return False

  def return_book(self):
    self.available = True

  def display_info(self):
    print(f'Book "{self.title}", written by {self.author}')

class Library(Book):
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def display_books(self):
    for book in self.books:
      book.display_info()

  def get_book_by_title(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        return book
      else:
        None

library = Library()


book1 = Book("Dracula", "Bram Stoker")
book2 = Book("1984", "George Orwell")
book3 = Book("Frankenstein", "Mary Shelley")
books = [book1, book2, book3]

for book in books:
  library.add_book(book)
library.display_books()
