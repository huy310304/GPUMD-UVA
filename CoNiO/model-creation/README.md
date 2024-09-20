# Co₀.₂₅Ni₀.₇₅O Model Conversion Script

## Overview

This Python script converts an XYZ file representing a Mg₀.₅Ni₀.₅O model into a Co₀.₂₅Ni₀.₇₅O model. The script randomly selects 1000 Mg atoms from the original structure and replaces them with Co atoms, while the remaining Mg atoms are converted into Ni atoms. This allows for the modification of the atomic composition while keeping the overall structure intact.

## Usage

1. **Input File**: The script expects an XYZ file as input (e.g., `mgnio.xyz`), which should follow the standard XYZ format:
   - The first two lines contain the header information.
   - The subsequent lines contain atomic information (element symbol and coordinates).

2. **Output File**: The script generates a new XYZ file (e.g., `conio.xyz`) with 1000 Co, 3000 Ni, and 4000 O atoms. The atomic composition is updated accordingly.

### Running the Script

To run the script, follow these steps:

1. Place the input file (`mgnio.xyz`) in the same directory as the script.
2. Run the script in your Python environment:
    ```bash
    python convert_model.py
    ```
3. The output file (`conio.xyz`) will be generated in the same directory with the updated atomic composition.

### Example

If the original `mgnio.xyz` file contains 2000 Mg atoms, 2000 Ni atoms, and 4000 O atoms, the script will:
- Randomly select 1000 Mg atoms and replace them with Co atoms.
- Replace the remaining 1000 Mg atoms with Ni atoms.
- The oxygen (O) atoms remain unchanged.

### Functions

- **`read_xyz(file_path)`**: Reads the content of the XYZ file.
- **`write_xyz(file_path, lines)`**: Writes the updated content to a new XYZ file.
- **`convert_mg_to_co_and_ni(lines, num_mg_to_co)`**: Converts Mg atoms to Co and Ni atoms.

### Customization

You can adjust the number of Mg atoms to convert into Co atoms by changing the `num_mg_to_co` parameter in the `convert_mg_to_co_and_ni` function. By default, it is set to `1000`.

### Requirements

- Python 3.x
- No external libraries are required, as the script uses the built-in `random` and `file` handling functions.