import random

def read_xyz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_xyz(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def convert_mg_to_co_and_ni(lines, num_mg_to_co=1000):
    atom_lines = lines[2:]  # Skip the first two lines (header)
    mg_indices = [i for i, line in enumerate(atom_lines) if line.startswith('Mg')]

    # Ensure we have enough Mg atoms to replace
    if len(mg_indices) < num_mg_to_co:
        raise ValueError("Not enough Mg atoms to replace")

    # Randomly select indices of Mg atoms to replace with Co
    mg_to_co_indices = random.sample(mg_indices, num_mg_to_co)
    remaining_mg_indices = set(mg_indices) - set(mg_to_co_indices)

    for i in mg_to_co_indices:
        atom_lines[i] = atom_lines[i].replace('Mg', 'Co', 1)

    for i in remaining_mg_indices:
        atom_lines[i] = atom_lines[i].replace('Mg', 'Ni', 1)

    return lines[:2] + atom_lines

# Paths to the input and output XYZ files
input_xyz_file = 'model.xyz'
output_xyz_file = 'conio.xyz'

# Read the original XYZ file
lines = read_xyz(input_xyz_file)

# Convert Mg atoms to Co and Ni atoms
updated_lines = convert_mg_to_co_and_ni(lines)

# Write the updated composition to the new XYZ file
write_xyz(output_xyz_file, updated_lines)

print(f"Converted {input_xyz_file} to {output_xyz_file} with 1000 Co, 3000 Ni, and 4000 O atoms.")
