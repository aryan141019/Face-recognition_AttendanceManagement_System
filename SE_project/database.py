import csv
import os
import numpy as np

filename = "database.csv"
admin_file = "admin_database.csv"

# Create the CSV file if it doesn't exist
def create_database_file():
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Gender", "Encoding"])
        file.close()
    print("Student database file created!")

# Create database for admins.
def create_admin_file():
    if not os.path.exists(admin_file):
        with open(admin_file, 'w', newline='') as f:
            write = csv.writer(f)
            write.writerow(["Name", "ID"])
        f.close()
    print("Admin database file created!")

# Add a new record to the CSV file
def add_record(name, gender, id, encoding):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, id, gender, encoding])


# Check existing records.
def record_exists(name, check_id, f):
    with open(f, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1]==check_id and row[0]==name:
                return True
    return False


# Delete existing records.
def delete_record(check_name, check_id):
    lines = list()
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]!=check_id and row[0]!=check_name:
                lines.append(row)
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lines)
        # Deleting the user's image from photos folder.
        os.remove(r'SE_project\photos\{}.jpg'.format(str(check_id)))
        print("Record deleted!!!")
    