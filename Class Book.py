class Book:
    def __init__(self, title=None, author=None, ISBN=None, price=None):
        """
        Constructor to initialize Book attributes. Default values are None.
        """
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def display_info(self):
        """
        Method to display book details.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Price: ${self.price:.2f}" if self.price else "Price: Not Available")
        print("-" * 30)

    def apply_discount(self, discount_percentage):
        """
        Method to apply discount to the book price.
        """
        if self.price:
            discount_amount = self.price * (discount_percentage / 100)
            self.price -= discount_amount
        else:
            print("Price is not set for this book.")


# Main function to test the Book class
def main():
    books = []
    n = int(input("Enter the number of books: "))

    for _ in range(n):
        print("\nEnter book details:")
        title = input("Title: ")
        author = input("Author: ")
        ISBN = input("ISBN: ")
        price = float(input("Price: "))

        book = Book(title, author, ISBN, price)
        books.append(book)

    print("\nBook Details:")
    for book in books:
        book.display_info()

    # Applying discount to the first book (example usage of additional method)
    if books:
        discount = float(input("Enter discount percentage for the first book: "))
        books[0].apply_discount(discount)
        print("\nAfter Discount:")
        books[0].display_info()


if __name__ == "__main__":
    main()
