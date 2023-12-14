import sqlite3

connection = sqlite3.connect("industry_division_db.db")  # Updated database name

cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS industries")
    cursor.execute("DROP TABLE IF EXISTS divisions")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'industries' table
try:
    cursor.execute("CREATE TABLE industries (IndustryID INTEGER PRIMARY KEY, Company TEXT, Headquarter TEXT)")
except Exception as e:
    print(f"Error creating 'industries' table: {e}")

# Create the 'divisions' table
try:
    cursor.execute("CREATE TABLE divisions (DivisionID INTEGER PRIMARY KEY, DivisionName TEXT, IndustryID INTEGER, FOREIGN KEY (IndustryID) REFERENCES industries(IndustryID))")
except Exception as e:
    print(f"Error creating 'divisions' table: {e}")

# Insert sample data into 'industries' table
industries_data = [('Apollo', 'Silicon Valley'),
                   ('google', 'Wall Street'),
                   ('Holiday Inn', 'London'),
                   ('tesla', 'Cambridge')]

for industry_data in industries_data:
    try:
        cursor.execute("INSERT INTO industries (Company, Headquarter) VALUES (?, ?)", industry_data)
    except Exception as e:
        print(f"Error inserting data into 'industries' table: {e}")

# Insert sample data into 'divisions' table
divisions_data = [('Healthcare', 1),
                  ('Information Technology', 2),
                  ('hospitality', 3),
                  ('manufacturing', 4)]

for division_data in divisions_data:
    try:
        cursor.execute("INSERT INTO divisions (DivisionName, IndustryID) VALUES (?, ?)", division_data)
    except Exception as e:
        print(f"Error inserting data into 'divisions' table: {e}")

connection.commit()
connection.close()
print("Divisions and Company")  # Updated print statement
