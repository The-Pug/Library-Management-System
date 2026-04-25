# Just a formality project, for capgemini sessions.
# Just Barely Good enough.
# Not much features.

from utilis import user_data, admin_data
from add_books import add
from show_books import show
from remove_books import remove
from issue_books import issue
from return_book import return_book
from register import register

def library():
    
    
    while True :
        
        x = input("Enter The L.E.M.S. as 'User or admin' \n : ").upper() 

        if x  == "USER":
            a = input("Enter your User_Id \n: ")
            b = input("\n Enter your  User_Password :")

            if a in user_data[0].keys():
                if b == user_data[0][a]:
        
                    while True :

                        print('''

                        1. See  All Books.
                        2. Issue Book.
                        3. Return Book.
                        4. Check Warnings.
                        5. Exit.
                        
                        ''')
                    
                        choice_u = int(input("Enter your choice (int only) \n: "))

                        if choice_u == 1 :
                            show()

                        elif choice_u == 2:
                            issue()
                        
                        elif choice_u == 3:
                            return_book()

                        elif choice_u == 4:
                            print("Fines system will soon be implemented. Be aware.\n")
                        
                        elif choice_u == 5:
                            break
                else :
                        print("\n Invalid Passcode.")
                
            else :
                    print("\n User Not Registered.")

        elif  x == "ADMIN" :

            g = input("\n Enter your Admin_Id : ")
            h = input("\n Enter your  Admin_Password :")

            if g in admin_data[0].keys():
                if h == admin_data[0][g]:
                    
                    while True :
                        print('''

                        1. See  All Books.
                        2. Add Books.
                        3. Remove Books.
                        4. Exit.
                        
                        ''')

                        choice_a = int(input("Enter your choice (in int) \n: "))

                        if choice_a == 1 :
                            show()

                        elif choice_a == 2:
                            add()
                        
                        elif choice_a == 3:
                            remove()

                        elif choice_a == 4 :
                            break

                else :
                        print("\n Invalid Passcode.")
                
            else :
                    print("\n Admin Not Registered.")


print("""----------------------------------------
------ Welcome to our Library EMS ------
---------------------------------------- 
--Library Electronic Management System--
----------------------------------------- """)


print("~ Who are you ?  \n")

print("""1. Register.
2. Log-In.
3. Exit. """)


p = int(input("Enter your choice (int only) :  \n"))

if p == 1:
    register()
elif p == 2 :
    library()
elif p == 3:
        print("Shutting down L.E.M.S... Goodbye!")
        break 
else:
        print("Invalid choice.")