import sqlite3
import requests

def fetch_and_store_books():
    print("Fetching data from API...")
    url = "https://openlibrary.org/search.json?q=python&limit=5"
    response = requests.get(url)
    data = response.json()
    
    books = []
    for doc in data.get('docs', []):
        title = doc.get('title', 'Unknown Title')
        author = ', '.join(doc.get('author_name', ['Unknown Author']))
        pub_year = doc.get('first_publish_year', 0)
        books.append((title, author, pub_year))
        
    print("Storing data in SQLite database...")
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    ''')
    cursor.execute('DELETE FROM books')
    cursor.executemany('INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)', books)
    conn.commit()
    
    print("--- Retrieved Books from Database ---")
    cursor.execute('SELECT title, author, publication_year FROM books')
    for row in cursor.fetchall():
        print(f"Title: {row[0]} | Author: {row[1]} | Year: {row[2]}")
        
    conn.close()

if __name__ == "__main__":
    fetch_and_store_books()
