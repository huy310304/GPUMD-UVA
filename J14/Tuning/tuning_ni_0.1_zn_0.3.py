import random
from collections import defaultdict

# File paths
input_file = 'model.xyz'
output_file = 'ni_01_zn_03.xyz'

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
    # Separate Ni lines and other lines
    ni_lines = [line for line in lines if line.startswith("Ni")]
    other_lines = [line for line in lines if not line.startswith("Ni")]

    # Randomly select 40 Ni atoms to convert to Zn
    ni_to_convert = random.sample(ni_lines, 40)
    ni_to_keep = [line for line in ni_lines if line not in ni_to_convert]

    # Add the converted Zn lines and the kept Ni lines
    for line in ni_to_convert:
        modified_lines.append(line.replace("Ni", "Zn", 1))
        total_zn += 1

    for line in ni_to_keep:
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

    # Output group summary
    print(f"Group {group_id}: Ni = {len(ni_to_keep)}, Zn = {40 + sum(1 for line in other_lines if line.startswith('Zn'))}, "
          f"Mg = {sum(1 for line in other_lines if line.startswith('Mg'))}, Co = {sum(1 for line in other_lines if line.startswith('Co'))}, "
          f"Cu = {sum(1 for line in other_lines if line.startswith('Cu'))}, O = {sum(1 for line in other_lines if line.startswith('O'))}")

# Write the modified data back to a new file
with open(output_file, 'w') as file:
    file.writelines(modified_lines)

# Output total summary
print("\nTotal counts across all groups:")
print(f"Ni = {total_ni}, Zn = {total_zn}, Mg = {total_mg}, Co = {total_co}, Cu = {total_cu}, O = {total_o}")
