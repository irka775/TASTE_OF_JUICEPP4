import os
import psycopg2
from psycopg2 import sql
from pathlib import Path

if os.path.isfile("env.py"):
    import env

# Get database URL from environment variables
DATABASE_URL = os.environ.get("DATABASE_URL")

# Parse the database URL
connection = psycopg2.connect(DATABASE_URL)
connection.autocommit = True

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# SQL command to terminate all active connections
terminate_query = sql.SQL(
    """
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = %s
      AND pid <> pg_backend_pid();
    """
)

# Get database name from the database URL
database_name = connection.get_dsn_parameters()["dbname"]

# Execute the SQL command
cursor.execute(terminate_query, (database_name,))

# Close the cursor and connection
cursor.close()
connection.close()

print("All active connections have been terminated.")
