from utilis import books


def return_book():
        
        x = input("Book to Return : ")
        y = input("Enter the book id: ")
        z = input("Enter your user id :")

        if z in user_data[2] and x in user_data[2][z]:

                books[0][x] = y
                books[1][y] = "Available"
                
                user_data[2][z].remove(x)
                print("Book returned successfully!")
        
        else:
            print("Record not found for this user/book.")
