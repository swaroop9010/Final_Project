import sqlite3

connection = sqlite3.connect("industry_division_db.db")  # Updated database name

def get_industries_and_divisions(industry_id=None, search_term=None):  # Updated function parameters
    cursor = connection.cursor()
    if industry_id is None:
        if search_term:
            # Updated SQL query with search functionality
            rows = cursor.execute(
                f"SELECT divisions.DivisionName, industries.IndustryID, industries.Company, industries.Headquarter "
                f"FROM industries LEFT JOIN divisions ON industries.IndustryID = divisions.IndustryID "
                f"WHERE industries.Company LIKE '%{search_term}%' OR divisions.DivisionName LIKE '%{search_term}%'"
            )
        else:
            # Original SQL query
            rows = cursor.execute(
                "SELECT divisions.DivisionName, industries.IndustryID, industries.Company, industries.Headquarter "
                "FROM industries LEFT JOIN divisions ON industries.IndustryID = divisions.IndustryID"
            )
    else:
        rows = cursor.execute(
            f"SELECT divisions.DivisionName, industries.IndustryID, industries.Company, industries.Headquarter "
            f"FROM industries LEFT JOIN divisions ON industries.IndustryID = divisions.IndustryID "
            f"WHERE industries.IndustryID={industry_id}"
        )
    rows = list(rows)
    rows = [{'DivisionName': row[0], 'IndustryID': row[1], 'Company': row[2], 'Headquarter': row[3]} for row in rows]

    return rows

def search_industries_and_divisions(search_term):  # New function for search functionality
    return get_industries_and_divisions(search_term=search_term)

# Rest of the code remains unchanged

# Static Routes
# ...

if __name__ == "__main__":
    # Update test calls accordingly
    print("done.")
