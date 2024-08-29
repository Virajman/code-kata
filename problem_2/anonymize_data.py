import pandas as pd
import hashlib
from faker import Faker

# Initialize Faker for generating random data
faker = Faker()


# Anonymize function
def anonymize_column(column):
    return column.apply(lambda x: hashlib.md5(x.encode()).hexdigest())


# Process the CSV file
chunk_size = 1000000  # tested for 2.08 GB data
input_file = 'sample_data.csv'
output_file = 'anonymized_data.csv'

with pd.read_csv(input_file, chunksize=chunk_size) as reader:
    for chunk in reader:
        # Anonymize sensitive columns
        chunk['first_name'] = chunk['first_name'].apply(lambda x: faker.first_name())
        chunk['last_name'] = chunk['last_name'].apply(lambda x: faker.last_name())
        chunk['address'] = chunk['address'].apply(lambda x: faker.address())

        # Append anonymized data to a new file
        chunk.to_csv(output_file, mode='a', header=False, index=False)

print("Anonymization complete.")
