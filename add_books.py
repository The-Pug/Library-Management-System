from utilis import books


def add():
        x = input("New Book Name : ")
        y = input("Enter the book id: ")
        books[0][x] = y
        books[1][y] = "Available"

