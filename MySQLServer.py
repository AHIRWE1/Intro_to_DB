import MySQLdb
from MySQLdb import Error

def create_database():
    try:
        # Connect to MySQL server (update user and password if needed)
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="g.abriella@1!"  # Use your password here if set
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Create database (will not fail if it already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
