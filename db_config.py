# db_config.py

import mysql.connector
from mysql.connector import Error
import os

def create_connection():
    """
    Create and return a MySQL database connection using environment variables.
    Returns:
        connection (mysql.connector.connection.MySQLConnection): Connection object if successful, else None.
    """
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "be9h1kqjuuxzkpadgkcc-mysql.services.clever-cloud.com"),
            user=os.environ.get("DB_USER", "uqj0qig3bsto59oh"),
            password=os.environ.get("DB_PASSWORD", "3OToj4A94CqH5EZgMj7P"),
            database=os.environ.get("DB_NAME", "be9h1kqjuuxzkpadgkcc"),
            port=int(os.environ.get("DB_PORT", 3306))
        )
        if connection.is_connected():
            print("✅ Connected to Clever Cloud MySQL database")
            return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

