class book :
    def __init__(self, title , author , isbn , available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def display_info(self) :
        print(f"Title : {self.title} , author : {self.author} , ISBN : {self.isbn} , available : {self.available}")
        