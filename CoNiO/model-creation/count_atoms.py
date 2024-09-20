def read_xyz(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    num_atoms = int(lines[0].strip())
    lattice = lines[1].strip()
    atoms = [line.strip() for line in lines[2:]]
    
    return num_atoms, lattice, atoms

def count_atoms_per_group(atoms):
    # Initialize the group_counts dictionary for groups 0 to 9
    group_counts = {str(i): {'Co': 0, 'Ni': 0, 'O': 0} for i in range(10)}
    
    for atom in atoms:
        element, *coords, group = atom.split()
        if group in group_counts:
            group_counts[group][element] += 1
    
    return group_counts

def main():
    input_file_path = 'rearranged_conio.xyz'
    
    # Read the input file
    num_atoms, lattice, atoms = read_xyz(input_file_path)
    
    # Count atoms per group
    group_counts = count_atoms_per_group(atoms)
    
    # Print atom counts per group

    total_Co = 0
    total_Ni = 0
    total_O = 0
    print("Atom counts per group:")
    for group, counts in group_counts.items():
        print(f"Group {group}: {counts}")
        total_Co += counts["Co"]
        total_Ni += counts["Ni"]
        total_O += counts["O"]

    print(total_Co)
    print(total_Ni)
    print(total_O)


if __name__ == '__main__':
    main()
