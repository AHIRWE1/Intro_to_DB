import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
       
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='g.abriella@1!',
            database='alx_book_store'
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Server")
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")

            print("📋 Tables in the database:")
            for table in cursor.fetchall():
                print(f"  - {table[0]}")

    except Error as e:
        print(f"❌ Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("🔒 Connection closed.")

if __name__ == "__main__":
    connect_to_mysql()
