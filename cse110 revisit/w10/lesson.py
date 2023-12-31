books = ["f", "g", "h"]

for i in range(len(books)):
    book = books[i]
    print(book)  # print each book to the screen.

num_books = len(books)
print(num_books) 


for index in range(len(books)):
    index = int(input("enter index: "))
    book = books[index]
    print(f"{index}. {book}") # print each book to the screen.

    