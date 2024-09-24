import random
from collections import defaultdict

# File paths
input_file = 'model.xyz'
output_file = 'ni_03_zn_01.xyz'

# Read the original data from the file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Initialize group-based storage
group_data = defaultdict(list)

# Header line (if exists), and atom lines
header = lines[:2]  # Assuming the first two lines are header lines
atom_lines = lines[2:]  # The rest are the atomic data

# Process and classify atoms by groups
for line in atom_lines:
    elements = line.split()
    atom_type = elements[0]
    group_id = int(elements[-1])
    
    group_data[group_id].append(line)

# This list will store the modified lines
modified_lines = []

# Add the header back to the modified file
modified_lines.extend(header)

# Process each group
total_ni = 0
total_zn = 0
total_mg = 0
total_co = 0
total_cu = 0
total_o = 0

for group_id, lines in group_data.items():
    # Separate Zn lines and other lines
    zn_lines = [line for line in lines if line.startswith("Zn")]
    other_lines = [line for line in lines if not line.startswith("Zn")]

    # Randomly select 40 Zn atoms to convert to Ni
    zn_to_convert = random.sample(zn_lines, 40)
    zn_to_keep = [line for line in zn_lines if line not in zn_to_convert]

    # Add the converted Zn lines and the kept Ni lines
    for line in zn_to_convert:
        modified_lines.append(line.replace("Zn", "Ni", 1))
        total_zn += 1

    for line in zn_to_keep:
        modified_lines.append(line)
        total_ni += 1

    # Add other element lines
    for line in other_lines:
        modified_lines.append(line)
        if line.startswith("Zn"):
            total_zn += 1
        elif line.startswith("Mg"):
            total_mg += 1
        elif line.startswith("Co"):
            total_co += 1
        elif line.startswith("Cu"):
            total_cu += 1
        elif line.startswith("O"):
            total_o += 1
