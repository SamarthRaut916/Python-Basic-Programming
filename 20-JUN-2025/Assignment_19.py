

def read_student_file(file_path):
    student_dict = {}

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Line {line_number}: Invalid format → '{line}'")
                    continue

                name, age_str, grade = parts

                if not name or not grade:
                    print(f"Line {line_number}: Missing name or grade → '{line}'")
                    continue

                try:
                    age = int(age_str)
                except ValueError:
                    print(f"Line {line_number}: Invalid age '{age_str}' → '{line}'")
                    continue

                # Add to dictionary
                student_dict[name] = {'age': age, 'grade': grade.upper()}

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"⚠️ Unexpected error while reading file: {e}")

    return student_dict


def write_student_dict(student_dict, output_file):
    try:
        with open(output_file, 'w') as file:
            for name, data in student_dict.items():
                file.write(f"{name},{data['age']},{data['grade']}\n")
        print(f"✅ Student records written to: {output_file}")
    except Exception as e:
        print(f"⚠️ Error writing to file: {e}")


# -------------------------
# ✅ Run the program
# -------------------------
input_file = 'students.txt'
output_file = 'students_output.txt'

students = read_student_file(input_file)

if students:
    print("\n📘 Valid Student Records:")
    for name, info in students.items():
        print(f"{name} → Age: {info['age']}, Grade: {info['grade']}")

    write_student_dict(students, output_file)
else:
    print("⚠️ No valid student records found.")
