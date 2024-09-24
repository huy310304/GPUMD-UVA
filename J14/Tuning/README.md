# J14 Model Tuning Conversion Script

## Overview

This Python script is designed to modify atomic compositions in XYZ models. It converts a J14 structure into new configurations by adjusting the atomic ratios of elements such as Mg, Co, Ni, Cu, and Zn. Specifically, the script handles conversions between the following models:

1. **Mg₀.₂Co₀.₂Ni₀.₁Cu₀.₂Zn₀.₃O**  
   In this model, 400 Ni atoms are randomly converted to Zn atoms.

2. **Mg₀.₂Co₀.₂Ni₀.₃Cu₀.₂Zn₀.₁O**  
   In this model, 400 Zn atoms are randomly converted to Ni atoms.

## Usage

### Input File

The script expects an XYZ file as input (e.g., `model.xyz`), which should be the J14 model and follow the standard XYZ format:
- The first two lines contain the header information.
- The subsequent lines contain atomic information (element symbol, coordinates, and group ID).

### Output File

The output file is generated with a new atomic composition. The default output file is `ni_01_zn_03.xyz`, containing the updated configuration after atomic replacements.

### Running the Script

To run the script:

1. Ensure the input file (`model.xyz`) of J14 is in the same directory as the script.
2. Run the script in your Python environment:
    ```bash
    python tuning_ni_0.1_zn_0.3.py
    ```
3. The output file (`ni_01_zn_03.xyz`) will be generated in the same directory with the updated atomic composition.

### Example

For the model `Mg₀.₂Co₀.₂Ni₀.₁Cu₀.₂Zn₀.₃O`, the script will:
- Randomly select 400 Ni atoms from each group and replace them with Zn atoms.
- All other elements (Mg, Co, Cu, and O) remain unchanged.

### Functions

- **`read_xyz(file_path)`**: Reads the content of the XYZ file.
- **`write_xyz(file_path, lines)`**: Writes the updated content to a new XYZ file.
- **`convert_atoms(lines, num_ni_to_zn)`**: Converts Ni atoms to Zn atoms or vice versa depending on the target model.

### Group Summary

For each group of atoms (Ni, Zn, Mg, Co, Cu, O), the script prints a summary of their counts before and after the conversion for each group, ensuring you can track changes in the atomic composition.

### Customization

You can adjust the number of Ni or Zn atoms to convert in each group by modifying the number in the `random.sample` call. By default, 40 Ni atoms per group are converted into Zn atoms. And we have a total of 10 groups, so 400 Ni atoms will be converted into 400 Zn atoms.

### Requirements

- Python 3.x
- model.xyz of J14
- No external libraries are required, as the script uses the built-in `random` and file handling functions.

### Additional Notes

- The script preserves the integrity of the atomic positions and groupings, only changing the element types.
- Ensure that the input file follows the correct XYZ format to avoid any parsing errors.
