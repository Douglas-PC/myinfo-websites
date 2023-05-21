import sqlite3

class Bookmark:
    def __init__(self, title, url, notes):
        self.title = title
        self.url = url
        self.notes = notes

def add_bookmark(title, url, notes):
    connection = sqlite3.connect("bookmarks.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO bookmarks (title, url, notes) VALUES (?, ?, ?)", (title, url, notes))
    connection.commit()
    connection.close()

def list_bookmarks():
    connection = sqlite3.connect("bookmarks.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookmarks")
    bookmarks = cursor.fetchall()
    connection.close()
    return bookmarks

def remove_bookmark(title):
    connection = sqlite3.connect("bookmarks.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bookmarks WHERE title = ?", (title,))
    connection.commit()
    connection.close()

def search_bookmarks(title):
    connection = sqlite3.connect("bookmarks.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookmarks WHERE title LIKE ?", (title + "%",))
    bookmarks = cursor.fetchall()
    connection.close()
    return bookmarks

def main():
    while True:
        print("1. Add bookmark")
        print("2. List bookmarks")
        print("3. Remove bookmark")
        print("4. Search bookmarks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the bookmark: ")
            url = input("Enter the URL of the bookmark: ")
            notes = input("Enter any notes for the bookmark: ")
            add_bookmark(title, url, notes)

        elif choice == "2":
            bookmarks = list_bookmarks()
            for bookmark in bookmarks:
                print(bookmark.title, bookmark.url, bookmark.notes)

        elif choice == "3":
            title = input("Enter the title of the bookmark you want to remove: ")
            remove_bookmark(title)

        elif choice == "4":
            title = input("Enter the title of the bookmark you want to search for: ")
            bookmarks = search_bookmarks(title)
            for bookmark in bookmarks:
                print(bookmark.title, bookmark.url, bookmark.notes)

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
