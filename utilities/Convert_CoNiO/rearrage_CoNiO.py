def read_xyz(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    num_atoms = int(lines[0].strip())
    lattice = lines[1].strip()
    atoms = [line.strip() for line in lines[2:]]
    
    return num_atoms, lattice, atoms

def write_xyz(file_path, num_atoms, lattice, atoms):
    with open(file_path, 'w') as f:
        f.write(f"{num_atoms}\n")
        f.write(f"{lattice}\n")
        for atom in atoms:
            f.write(f"{atom}\n")

def rearrange_atoms(atoms):
    grouped_atoms = {str(i): [] for i in range(10)}
    
    for atom in atoms:
        element, *coords, group = atom.split()
        grouped_atoms[group].append((element, coords, group))
    
    rearranged_atoms = []
    for group in grouped_atoms:
        # Separate Co, Ni, and O atoms
        co_atoms = [f"Co {' '.join(coords)} {group}" for element, coords, group in grouped_atoms[group] if element == 'Co']
        ni_atoms = [f"Ni {' '.join(coords)} {group}" for element, coords, group in grouped_atoms[group] if element == 'Ni']
        o_atoms = [f"O {' '.join(coords)} {group}" for element, coords, group in grouped_atoms[group] if element == 'O']
        
        # Append Co atoms first, then Ni, then O
        rearranged_atoms.extend(co_atoms + ni_atoms + o_atoms)
    
    return rearranged_atoms

def main():
    input_file_path = 'conio.xyz'
    output_file_path = 'rearranged_conio.xyz'
    
    # Read the input file
    num_atoms, lattice, atoms = read_xyz(input_file_path)
    
    # Rearrange atoms so that Co comes before Ni in each group
    rearranged_atoms = rearrange_atoms(atoms)
    
    # Write the output file
    write_xyz(output_file_path, num_atoms, lattice, rearranged_atoms)

if __name__ == '__main__':
    main()
