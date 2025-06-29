import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Step 1: Connect to MySQL server WITHOUT specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='g.abriella@1!'
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Server (no database specified)")

            cursor = connection.cursor()

            # Step 2: Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("🗃️ Database 'alx_book_store' ensured to exist.")

            cursor.close()
            connection.close()
            print("🔒 Initial connection closed.")

        # Step 3: Now reconnect, this time specifying the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='g.abriella@1!',
            database='alx_book_store'
        )

        if connection.is_connected():
            print("✅ Connected to MySQL Server with 'alx_book_store' database")

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
