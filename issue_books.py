from utilis import books, user_data

def issue():

    x = input("The Book that you wnt to issue: ")
    y = input("Enter the book id: ")
    z = input("Enter your user id :")

    if  x in books[0].keys():
        if y == books[0][x]:
            
            user_data[2][z].append(x)
            
            
            del books[0][x]
            del books[1][y]
