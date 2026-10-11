import csv
import sqlite3

def import_csv_to_db(csv_filename, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    cursor.execute('DELETE FROM users')
    
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            
            users_data = [(row['name'], row['email']) for row in reader]
            
            cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users_data)
            conn.commit()
            print(f"Successfully inserted {len(users_data)} records into {db_filename}")
            
    except FileNotFoundError:
        print(f"Error: {csv_filename} not found.")
        return
        
    print("\n--- Users in Database ---")
    cursor.execute('SELECT * FROM users')
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")
        
    conn.close()

if __name__ == "__main__":
    import_csv_to_db('users.csv', 'users.db')
