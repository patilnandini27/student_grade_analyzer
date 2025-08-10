import csv

def load_data(file_path):
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                'name': row['Name'],
                'marks': list(map(int, row['Marks'].split(',')))
            })
    return students

def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def analyze_students(students):
    for student in students:
        avg = calculate_average(student['marks'])
        print(f"{student['name']} - Average Marks: {avg:.2f}")

if __name__ == "__main__":
    file_path = 'students.csv'
    print("Loading student data...")
    students = load_data(file_path)
    print("Analyzing student grades...")
    analyze_students(students)
