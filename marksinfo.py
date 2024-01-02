from flask import Flask, render_template
from prettytable import PrettyTable
import mysql.connector

app = Flask(__name__)

# Replace these values with your actual database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Manisha@143567890',
    'database': 'database1',
}

@app.route('/')
def display_table():
    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Adjusted query without the deleted column
    query = 'SELECT SlNo, ` semester`, result, credits, sgpa, cgpa FROM studentmarks;'

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    data = cursor.fetchall()

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["SlNo", "Semester", "Result", "Credits", "SGPA", "CGPA"]

    # Populate the table with data
    for row in data:
        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Calculate the overall percentage (you might need to adjust this based on your data model)
    overall_percentage = calculate_overall_percentage(data)

    # Render the HTML template with the table data, name, and percentage
    return render_template('table_template.html', table_data=data, name='Debbati Sudheer', percentage=71.69)

def calculate_overall_percentage(data):
    # Your logic to calculate the overall percentage goes here
    # This is just a placeholder, you need to adjust it based on your data model
    total_sgpa = sum(row[5] for row in data)
    total_credits = sum(row[4] for row in data)
    overall_percentage = (total_sgpa / total_credits) * 10  # Adjust the formula based on your requirements
    return overall_percentage

if __name__ == '__main__':
    app.run(debug=True)