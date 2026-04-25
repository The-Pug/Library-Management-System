from utilis import user_data, admin_data

def register():

            
        x = input("Register in The L.E.M.S. as 'User or admin' : ").upper()

        if x  == "USER":
            a = input("Enter your User_Id : ")
            b = input("\n Enter your  User_Password :")

            user_data[0][a]= b
            user_data[1][a]= []
            user_data[2][a]= []
            user_data[3][a]= []

        elif  x == "ADMIN" :

            z = "L.E.M.S.001"

            g = input("\n Enter your Admin_Id : ")
            h = input("\n Enter your  Admin_Password :")
            i = input("\n Enter the special code : ")


            if i == z :
                admin_data[0][g] = h
