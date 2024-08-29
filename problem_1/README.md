What the Script Does:

1. Generate a Fixed-Width File:
The script first creates a fixed-width file named output.txt based on the provided data and specification.
2. Parse the Fixed-Width File:
It then parses the generated fixed-width file and converts it into a CSV file named output.csv.
3. Implement a Parser for the Fixed-Width File
4. Output
output.txt: The fixed-width file.
output.csv: The CSV file generated from the fixed-width file.
5. Write a dockerfile

How to run the script:
1. python solution_problem1.py
2. Build the Docker Image:
    docker build -t fixed-width-parser 
3. Run the Docker Container:
    docker run -v $(pwd):/app fixed-width-parser

How to run the test case:
1. python test_truncation_behavior.py
