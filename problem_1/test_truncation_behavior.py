import unittest

# The function that handles the fixed-width file generation
def generate_fixed_width_file(data, spec):
    output = []
    for record in data:
        line = ''
        for i, (field, length) in enumerate(spec):
            # Left-justify and trim the value to fit the field width
            value = str(record[i]).ljust(length)[:length]
            line += value
        output.append(line)
    return output

class TestFixedWidthFileGeneration(unittest.TestCase):
    def test_truncation_behavior(self):
        # Define the fixed-width specification for the test
        test_spec = [
            ('f1', 5),  # Student ID
            ('f2', 10), # Full Name
            ('f3', 8)   # Subject
        ]

        # Test data with a value that exceeds the offset
        test_data = [
            ['12345', 'Christopher', 'Mathematics'],  # 'Christopher' exceeds 10 characters
            ['67890', 'Alice', 'Science']             # No truncation needed
        ]

        # Expected fixed-width output
        expected_output = [
            '12345ChristopheMathemati',  # 'Christopher' is truncated to 'Christophe'
            '67890Alice     Science  '   # No truncation
        ]

        # Generate the actual output
        actual_output = generate_fixed_width_file(test_data, test_spec)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
