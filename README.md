			AccuKnox Assignment
Name: Kothapuli Vishnu Vardhan Reddy 
Mobile : 9346048323
Email: Kothapuli.vishnureddy@gmail.com
Problem Statement- 1

1.	API Data Retrieval and Storage: You are tasked with fetching data from an external REST API, storing it in a local SQLite database, and displaying the retrieved data. The API provides a list of books in JSON format with attributes like title, author, and publication year.

2.	import sqlite3
3.	import requests
4.	
5.	def fetch_and_store_books():
6.	    print("Fetching data from API...")
7.	    url = "https://openlibrary.org/search.json?q=python&limit=5"
8.	    response = requests.get(url)
9.	    data = response.json()
10.	    
11.	    books = []
12.	    for doc in data.get('docs', []):
13.	        title = doc.get('title', 'Unknown Title')
14.	        author = ', '.join(doc.get('author_name', ['Unknown Author']))
15.	        pub_year = doc.get('first_publish_year', 0)
16.	        books.append((title, author, pub_year))
17.	        
18.	    print("Storing data in SQLite database...")
19.	    conn = sqlite3.connect('books.db')
20.	    cursor = conn.cursor()
21.	    cursor.execute('''
22.	        CREATE TABLE IF NOT EXISTS books (
23.	            id INTEGER PRIMARY KEY AUTOINCREMENT,
24.	            title TEXT,
25.	            author TEXT,
26.	            publication_year INTEGER
27.	        )
28.	    ''')
29.	    cursor.execute('DELETE FROM books')
30.	    cursor.executemany('INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)', books)
31.	    conn.commit()
32.	    
33.	    print("--- Retrieved Books from Database ---")
34.	    cursor.execute('SELECT title, author, publication_year FROM books')
35.	    for row in cursor.fetchall():
36.	        print(f"Title: {row[0]} | Author: {row[1]} | Year: {row[2]}")
37.	        
38.	    conn.close()
39.	
40.	if __name__ == "__main__":
41.	    fetch_and_store_books()
42.	
Output: 
python book_api_db.py
Fetching data from API...
Storing data in SQLite database...
--- Retrieved Books from Database ---
Title: Learning Python | Author: Mark Lutz, David Ascher | Year: 1999
Title: Python For Data Analysis | Author: Wes McKinney | Year: 2012
Title: Fluent Python | Author: Luciano Ramalho | Year: 2015
Title: Black Hat Python | Author: Justin Seitz, Tim Arnold | Year: 2014
Title: Python Cookbook | Author: Alex Martelli, David Ascher, David M. Beazley, Brian K. Jones | Year: 2002


















2. Data Processing and Visualization: Given a dataset containing information about students' test scores, fetch the data from an API, calculate the average score, and create a bar chart to visualize the data.
43.	import matplotlib.pyplot as plt
44.	
45.	def process_and_visualize_scores():
46.	    sample_data = [
47.	        {"name": "Vishnu", "score": 85},
48.	        {"name": "Akhila", "score": 92},
49.	        {"name": "Rahul", "score": 78},
50.	        {"name": "Arjun", "score": 90},
51.	        {"name": "Eva", "score": 88}
52.	    ]
53.	    
54.	    scores = [student["score"] for student in sample_data]
55.	    names = [student["name"] for student in sample_data]
56.	    
57.	    average_score = sum(scores) / len(scores) if scores else 0
58.	    print(f"Average Student Score: {average_score:.2f}")
59.	    
60.	    plt.figure(figsize=(8, 5))
61.	    bars = plt.bar(names, scores, color='skyblue')
62.	    
63.	    plt.axhline(y=average_score, color='r', linestyle='--', label=f'Average ({average_score:.2f})')
64.	    
65.	    plt.title('Student Test Scores')
66.	    plt.xlabel('Student Name')
67.	    plt.ylabel('Score')
68.	    plt.ylim(0, 100)
69.	    plt.legend()
70.	    
71.	    filename = 'student_scores_chart.png'
72.	    plt.savefig(filename)
73.	    print(f"Bar chart successfully saved to '{filename}'")
74.	
75.	if __name__ == "__main__":
76.	    process_and_visualize_scores()
77.	


Output: 
python student_scores_chart.py
Average Student Score: 86.60 

 3.	CSV Data Import to a Database: Write a Python script that reads data from a CSV file containing user information (e.g., name, email) and inserts it into a SQLite database.

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
        with open(csv_filename, mode='r', encoding='utf-8') as file:
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

Output:
python csv_to_sqlite.py
Successfully inserted 5 records into users.db

--- Users in Database ---
ID: 1 | Name: Vishnu Reddy | Email: vishnureddy@example.com
ID: 2 | Name: Akhila Kothapuli | Email: akhila@example.com
ID: 3 | Name: Kl Rahul | Email: rahulkl@example.com
ID: 4 | Name: Vijay D | Email: vijaydev@example.com
ID: 5 | Name: Evaarah KL | Email: eva@example.com

 4.	Send a link to the most complex Python code you have written 

RepoScribe : https://github.com/VishnuVardhanReddyKothapuli/RepoScribe-with-RAG

The above reposcribe is the most complex python code I have written. it involves Python, RAG, repository processing, LLM integration, and multiple components.

5.	Send a link to the most complex database code you have written
https://github.com/VishnuVardhanReddyKothapuli/Sentinal
this is the most complex database code I have written.






 Problem Statement- 2

1.	I would rate myself on B ( where I can code comfortably under supervision)
{I am good in building things using LLMs, RAG, but I need assistance for deep learning}

2.	What are the key architectural components to create a chatbot based on LLM? Please explain the approach on a high-level
Ans. The key architectural components to create a chat bot based on LLMs are:
•	Proper UI/UX where a user can search for their desired question.
•	Next user requests through APIs
•	Prompt or question asked by the user sent to the LLM
•	The llm searches in the memory (uses previous chats and user data as context window)
•	Then  LLM generates response based on the prompt – if RAG {first doc are chunked first -> embeddings->stores in vectordb like chroma, qdrant}
•	Then stores in Database
•	Safety – for example prompt injection{if a user asks to reveal all the system arch and secrets, our chatbot must terminate that request}
•	Returns the response

3.	Please explain vector databases. If you were to select a vector database for a hypothetical problem (you may define the problem) which one will you choose, and why?
Ans.  Vector databases stores the data as numerical embeddings, we can use these embeddings for semnatic search (nearest meaning)
Machine cant understand human language so we convert human lang to numerical embeddings.
If I want to create a chat bot ill choose chromadb , because it is easy to setup and has good Langchain env.

# AccuKnox-Assignment
