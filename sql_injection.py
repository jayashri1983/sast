import sqlite3

def insecure_query(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🚨 This is a vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'" 
    cursor.execute(query) 

    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.close()

if __name__ == "__main__":
    user_input = input("Enter username: ")
    insecure_query(user_input)
