class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self): # special method, built-in function
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self): # special method, built-in function
        return self.pages


book = Book("Python Rock!", "Jose", 250)
print(book)
print(len(book))
