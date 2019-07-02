from Milestone2.utils.DB_conn import DatabaseConnection

HOST = 'my_lib.db'


def print_menu():
    return "1. Add New Book\n2. List All Books\n3. Mark Book as Read\n4. Delete Book\n5. Exit\t"


def add_book(book):
    with DatabaseConnection(HOST) as db:

        query = f"""INSERT INTO myLib(name, author, read) values( '{book[0]}', '{book[1]}', {0 if book[2] == 'n' else 1 })"""
        db.execute(query)


def get_all():
    books = []
    with DatabaseConnection(HOST) as db:
        query = "SELECT name, author, read FROM myLib"
        myLib = db.execute(query)
        for book in myLib:
            books.append(book)
    return books


def print_my_books(books):
    if books is not None and len(books) > 0:
        print("\tMy Books:")
        for book in books:
            print(f'\t\tTitle: {book[0]}, Author: {book[1]}, have I read this book: {bool(book[2])}')
    else:
        print("No Books")


def mark_book_read(book_name):
    with DatabaseConnection(HOST) as db:
        db.execute("""UPDATE TABLE myLib SET READ = 1 WHERE NAME = %s""" % book_name)


def delete_book(book_name):
    with DatabaseConnection(HOST) as db:
        query = """DELETE FROM myLib where name = '%s'""" % book_name
        db.execute(query)
    print(f"Deleted book: {book_name}")



def main():
    while True:
        user_input = input(print_menu())
        if user_input == '1':
            add_book((input("Book Name:"),input("Author:"), input("Have your read the book? [y/n]")))
        elif user_input == '2':
            print_my_books(get_all())
        elif user_input == '3':
            mark_book_read(input("Select book to update:"))
        elif user_input == '4':
            delete_book(input("Select book to delete:"))
        elif user_input == '5':
            break
        else:
            print("Bad Input, try again")
    print("Good Bye!")


def init():
    with DatabaseConnection(HOST) as db:
        query = "CREATE TABLE IF NOT EXISTS myLib(name TEXT, author TEXT, read INTEGER )"
        db.execute(query)


if __name__ == '__main__':
    init()
    main()
