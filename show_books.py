from utilis import books

def show():
        x = books[0]
        y = books[1]

        for i,j in books[0].items():
            s = books[1].get(j, "Unknown")
            print(f"| Name: {i} | ID: {j} | Status: {s} |")
            print("---------------------\n")

