# File Encryption and Decryption Tool

This Python script uses the `pyAesCrypt` library to encrypt and decrypt files. It checks whether the input file exists and whether the output file does not exist before proceeding with the encryption or decryption process.

## Features

- Encrypts and decrypts files using AES encryption.
- Checks the existence of input and output files.
- Handles exceptions during the encryption and decryption process.

## Usage

To run the script, use command line arguments to specify the password, input file, output file, and decryption output file.

Example:

```bash
python main.py --password myPassword --input data.txt --output data.txt.aes --decrypt_output dataout.txt
```

This command will encrypt the `data.txt` file with the password `myPassword`, save the encrypted data to `data.txt.aes`, and then decrypt the `data.txt.aes` file back into `dataout.txt`.

## Installation

Ensure you have Python 3 and the `pyAesCrypt` library installed on your system. You can install `pyAesCrypt` using pip:

```bash
pip install pyAesCrypt
```

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or issues, feel free to reach out to the maintainer.

---
