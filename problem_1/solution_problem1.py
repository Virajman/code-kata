# The provided spec file in the problem statement
spec = {
    "ColumnNames": [
        "f1", "f2", "f3", "f4", "f5",
        "f6", "f7", "f8", "f9", "f10"
    ],
    "Offsets": [
        "5", "12", "3", "2", "13",
        "7", "10", "13", "20", "13"
    ],
    "FixedWidthEncoding": "windows-1252",
    "IncludeHeader": "True",
    "DelimitedEncoding": "utf-8"
}

# Convert offsets to integers
offsets = [int(offset) for offset in spec["Offsets"]]

# Combine column names and offsets into a spec list
fixed_width_spec = list(zip(spec["ColumnNames"], offsets))

# Function to generate a fixed-width file
def generate_fixed_width_file(data, spec, filename, encoding):
    with open(filename, 'w', encoding=encoding) as f:
        for record in data:
            line = ''
            for i, (field, length) in enumerate(spec):
                # Left-justify and trim the value to fit the field width
                value = str(record[i]).ljust(length)[:length]
                line += value
            f.write(line + '\n')

# Function to parse the fixed-width file into a CSV file
def parse_fixed_width_file(spec, input_filename, output_filename, fixed_width_encoding, delimited_encoding, include_header):
    with open(input_filename, 'r', encoding=fixed_width_encoding) as infile, \
         open(output_filename, 'w', encoding=delimited_encoding) as outfile:

        # Write CSV header if required
        if include_header:
            header = ','.join([field for field, _ in spec])
            outfile.write(header + '\n')

        for line in infile:
            parsed_line = []
            start = 0
            for _, length in spec:
                # Extract field value based on its length and strip leading/trailing whitespace
                field_value = line[start:start+length].strip()
                parsed_line.append(field_value)
                start += length
            outfile.write(','.join(parsed_line) + '\n')

# Example data to be written to the fixed-width file

"""The data includes:

f1: Student ID (5 characters)
f2: Full Name (12 characters)
f3: Age (3 characters)
f4: Gender (2 characters)
f5: Subject (13 characters)
f6: Marks (7 characters)
f7: Grade (10 characters)
f8: School Name (13 characters)
f9: Address (20 characters)
f10: City (13 characters)
"""

data = [
    ['10001', 'Alice Brown', '15', 'F', 'Mathematics', '95', 'A', 'Sunrise High', '123 Maple St.', 'New York'],
    ['10002', 'Bob Smith', '16', 'M', 'Science', '88', 'B+', 'Central High', '456 Oak Ave.', 'Los Angeles'],
    ['10003', 'Charlie Tan', '15', 'M', 'History', '92', 'A-', 'Eastside High', '789 Pine Rd.', 'Chicago'],
    ['10004', 'Diana Lee', '17', 'F', 'Chemistry', '85', 'B', 'Westview High', '101 Elm St.', 'Houston'],
    ['10005', 'Eve Green', '16', 'F', 'Physics', '89', 'B+', 'Sunrise High', '234 Cedar St.', 'Phoenix'],
    ['10006', 'Frank White', '15', 'M', 'Biology', '93', 'A-', 'Central High', '567 Birch Rd.', 'Philadelphia'],
    ['10007', 'Grace Kim', '16', 'F', 'English', '87', 'B', 'Eastside High', '890 Walnut Dr.', 'San Antonio'],
    ['10008', 'Hank Zhou', '17', 'M', 'Geography', '90', 'A-', 'Westview High', '321 Maple St.', 'San Diego'],
    ['10009', 'Ivy Patel', '15', 'F', 'Art', '92', 'A', 'Sunrise High', '654 Pine Ave.', 'Dallas'],
    ['10010', 'Jack Lee', '16', 'M', 'Mathematics', '94', 'A', 'Central High', '987 Oak Dr.', 'San Jose']
]
"""
ASSUMPTION: The value is cut off at the maximum length allowed by the offset. Any characters beyond this limit are discarded.

Example: If the field is 5 characters wide (offset), and the value is "Mathematics", it will be truncated to "Mathe".

"""
# Filenames for the fixed-width file and the resulting CSV file
fixed_width_filename = 'output.txt'
csv_filename = 'output.csv'

# Generate the fixed-width file with the specified encoding
generate_fixed_width_file(data, fixed_width_spec, fixed_width_filename, spec["FixedWidthEncoding"])

# Parse the fixed-width file into a CSV file with the specified encodings
parse_fixed_width_file(fixed_width_spec, fixed_width_filename, csv_filename, spec["FixedWidthEncoding"], spec["DelimitedEncoding"], spec["IncludeHeader"] == "True")

print(f"Fixed-width file '{fixed_width_filename}' generated and parsed to CSV '{csv_filename}'.")
