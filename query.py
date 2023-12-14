import sqlite3

connection = sqlite3.connect("industry_division_db.db")  # Updated database name

cursor = connection.cursor()

# Fetch data from the 'industries' table
cursor.execute("SELECT IndustryID, Company, Headquarter FROM industries")
industry_rows = list(cursor.fetchall())

# Fetch data from the 'divisions' table
cursor.execute("SELECT DivisionID, DivisionName, IndustryID FROM divisions")
division_rows = list(cursor.fetchall())

print("Industries:")
print(industry_rows)

print("\nDivisions:")
print(division_rows)

# Combine the data into a single list of dictionaries
industry_data = [{'IndustryID': row[0], 'Company': row[1], 'Headquarter': row[2]} for row in industry_rows]
division_data = [{'DivisionID': row[0], 'DivisionName': row[1], 'IndustryID': row[2]} for row in division_rows]

print("\nCombined Data:")
combined_data = []

for industry in industry_data:
    related_divisions = [division for division in division_data if division['IndustryID'] == industry['IndustryID']]
    industry_copy = industry.copy()
    industry_copy['Divisions'] = related_divisions
    combined_data.append(industry_copy)

print(combined_data)
