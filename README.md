# Turing Machine 



This project is a Python implementation of a Turing Machine emulator. It allows users to define, execute, and simulate the behavior of a Turing Machine based on custom-defined rules. The program reads its configuration and instructions from a text file and processes inputs accordingly.

## Features

- **Customizable Rules:** Define the Turing Machine's transitions and states using a clear syntax.
- **Flexible Input:** Accepts user-provided input for processing by the Turing Machine.
- **Text-Based Configuration:** Configure the Turing Machine using the `skladnia.txt` file.
- **Educational Tool:** Learn about the fundamentals of Turing Machines by experimenting with different configurations.

## Technology Stack

- **Programming Language:** Python

## Getting Started

Follow these steps to set up and run the Turing Machine emulator on your local system.

### Prerequisites

- Python 3.7 or higher installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WWasilew/Turing-Machine.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Turing-Machine
   ```

### Running the Emulator

1. Prepare your Turing Machine configuration in a `.txt` file, adhering to the syntax described in `skladnia.txt`.
2. Execute the emulator with the following command:
   ```bash
   python maszyna_t.py <path-to-configuration-file>
   ```
   Replace `<path-to-configuration-file>` with the path to your Turing Machine configuration file.

### Syntax Description

The syntax for defining the Turing Machine configuration is detailed in the `skladnia.txt` file. The rules must include:

- **States**: Defined states of the machine.
- **Alphabet**: Input and tape symbols the machine can process.
- **Transitions**: Rules dictating state changes and tape movements.
- **Start State**: The initial state of the Turing Machine.
- **Accept State(s)**: State(s) where the machine halts and accepts the input.
- **Reject State(s)**: State(s) where the machine halts and rejects the input.

### Example Configuration

Below is a simple example of a configuration file:
```
no
```

## Project Structure

```
Turing-Machine/
├── maszyna_t.py    # Main script to execute the Turing Machine
├── skladnia.txt    # Syntax guide for the configuration file
├── examples/       # Example configuration files
├── README.md       # Project documentation
└── LICENSE         # License information
```

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, feel free to fork the repository and submit a pull request.

1. Fork the project.
2. Create your feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [WWasilew](https://github.com/WWasilew). Feel free to contact me for any questions, suggestions, or feedback!

---

Experiment, learn, and explore the power of Turing Machines! ⚛

