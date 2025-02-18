import csv
import random

def generate_random_name():
  """Generates a random first and last name."""
  first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
  last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson']
  return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_marks():
  """Generates random marks between 0 and 100."""
  return random.randint(0, 100)

def create_csv(filename):
  """Creates a CSV file with 100 random student records."""
  with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Roll No', 'English', 'Math', 'Hindi', 'Science', 'SST']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(100):
      writer.writerow({
        'Name': generate_random_name(),
        'Roll No': f"R{i+1:03d}",  # Format roll number as R001, R002, ...
        'English': generate_random_marks(),
        'Math': generate_random_marks(),
        'Hindi': generate_random_marks(),
        'Science': generate_random_marks(),
        'SST': generate_random_marks()
      })

# Create the CSV file
create_csv('student_data.csv')
