import openpyxl
from faker import Faker
import pandas as pd

# Initialize Faker object
fake = Faker()


# Function to generate fake data based on the provided data type
def generate_fake_data(data_type, rows=10):
    if data_type == 'name':
        return [fake.name() for _ in range(rows)]
    elif data_type == 'email':
        return [fake.email() for _ in range(rows)]
    elif data_type == 'address':
        return [fake.address() for _ in range(rows)]
    elif data_type == 'phone_number':
        return [fake.phone_number() for _ in range(rows)]
    else:
        raise ValueError(
            f"Invalid data type: {data_type}. Supported types: 'name', 'email', 'address', 'phone_number'.")


# Function to read user-provided column names and data types from Excel
def read_excel_input(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    columns = {}

    # Read each row starting from the second row (assuming the first row contains headers)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        column_name, data_type = row

        # Error validation for missing column names or data types
        if not column_name:
            raise ValueError("Column name cannot be empty.")
        if not data_type:
            raise ValueError(f"Data type for column '{column_name}' cannot be empty.")

        columns[column_name] = data_type

    return columns


# Main function to generate mock data and write to Excel
def generate_mock_data(input_file, output_file, rows=10):
    # Read the columns and their data types from the input Excel file
    try:
        columns = read_excel_input(input_file)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Generate data
    data = {}
    for column, data_type in columns.items():
        try:
            data[column] = generate_fake_data(data_type, rows)
        except ValueError as e:
            print(f"Error: {e}")
            return

    # Create a DataFrame and write the data to a new Excel file
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

    print(f"Excel file '{output_file}' generated successfully!")


# Example usage:
input_excel_file = 'user_input.xlsx'  # Input file with column names and data types
output_excel_file = 'generated_mock_data.xlsx'  # Output file for generated data
rows_to_generate = 20

generate_mock_data(input_excel_file, output_excel_file, rows_to_generate)
