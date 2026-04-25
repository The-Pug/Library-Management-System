from utilis import books


def remove():
        x = input("The Book that is going to be removed : ")
        y = input("Enter the book id: ")

        if x in books[0].keys() :
            if y == books[0][x] :
                del books[0][x]
                del books[1][y]
            

