import re

def check_lines(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(r'[ab]ab', line):
                print(f"Ligne {line_number}: {line.strip()}")

check_lines('./router.unix')