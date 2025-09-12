class member :
    def __init__(self , name , membership_id , borrowed_books):
        self.name = name
        self.membership = membership_id
        self.borrowed_books = borrowed_books
    def borrow_book(self , book) :
      print(f"{self.name}brrowed'{book.title}'") 
    def return_book(self , book) :
       print(f"{self.name}returned'{book.title}'")