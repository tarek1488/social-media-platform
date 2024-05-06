import pymysql
from datetime import date

# Establishing a connection to the database
try:
    my_db = pymysql.connect(
        host="reunion.mysql.database.azure.com",
        user="trmb",
        password="$$BASMOTESH123",
        database='reunion'
    )
except Exception as e:
    print("Error in connection:", e)

# Creating a cursor object to interact with the database
my_cursor = my_db.cursor()

# Defining the SQL INSERT statement for the 'user' table
sql = "INSERT INTO user (username, FirstName, email, password_hash, lastname, Gender, Birthdate, FamilyID, FamilyRole) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


# Example data to insert
# Note: Modify the values accordingly. Ensure dates and other types are correctly formatted.
data = (
    "johnsmith",          # username
    "John",             # FirstName
    "john.smith@example.com",  # email
    "1234",    # password_hash
    "smith",              # lastname
    True,               # Gender (True for male, False for female)
    date(1990, 1, 1),   # Birthdate
    1,                  # FamilyID (assumes a valid ID from the 'family' table)
    True                # FamilyRole (True for admin, False for normal member)
)

try:
    # Executing the SQL statement
    my_cursor.execute(sql, data)

    # Committing the changes
    my_db.commit()

    print("User data inserted successfully. Inserted ID:", my_cursor.lastrowid)

except pymysql.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Closing the cursor and database connection
    if my_cursor:
        my_cursor.close()
    if my_db:
        my_db.close()
