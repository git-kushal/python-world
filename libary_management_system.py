books =[]

def add_book():
    title=input("book title: ")
    author=input("Author name: ")
    books.append({"title":title,"author":author})

def view_book():
    if not books:
        print("No book avalable")
    for b in books:
        print(f"{b["title"]} by {b["author"]}")

def search_book():
    name=input("Search book title: ")
    found=False
    for b in books:
        if name.lower() in b["title"].lower():
            print(f"Found: {b['title']} by {b['author']}")
            found = True
    if not found:
        print("Not found.")

def menu():
    while True:
        print("\n1. Add Book\n2. View All Books\n3. Search Book\n4. Exit")
        try:
            ch = int(input("Choice: "))
            if ch == 1:
                add_book()
            elif ch == 2:
                view_books()
            elif ch == 3:
                search_book()
            elif ch == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

menu()