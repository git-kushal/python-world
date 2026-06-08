books =[]

def add_book():
    title=input("book title: ")
    author=input("Author name: ")
    book.append({"title":title,"author":author})

def viwe_book():
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
