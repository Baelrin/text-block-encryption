import os
import argparse
import pyAesCrypt

INPUT_FILE_DEFAULT = 'data.txt'
OUTPUT_FILE_DEFAULT = 'data.txt.aes'
DECRYPT_OUTPUT_DEFAULT = 'dataout.txt'

def ensure_file_exists(filename):
   """Ensure a file exists and raise an exception if it does not."""
   if not os.path.exists(filename):
       raise FileNotFoundError(f"{filename} does not exist.")

def ensure_file_does_not_exist(filename):
   """Ensure a file does not exist and raise an exception if it does."""
   if os.path.exists(filename):
       raise FileExistsError(f"{filename} already exists.")

def encrypt_file(input_filename, output_filename, password):
   """Encrypt a file using a password.

   Args:
   input_filename: The name of the file to encrypt.
   output_filename: The name of the file to write the encrypted data to.
   password: The password to use for encryption.

   Raises:
   FileNotFoundError: If the input file does not exist.
   FileExistsError: If the output file already exists.
   """
   try:
       ensure_file_exists(input_filename)
       ensure_file_does_not_exist(output_filename)
       pyAesCrypt.encryptFile(input_filename, output_filename, password)
   except FileNotFoundError as e:
       print(f"Input file error: {e}")
   except FileExistsError as e:
       print(f"Output file error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")

def decrypt_file(input_filename, output_filename, password):
   """Decrypt a file using a password.

   Args:
   input_filename: The name of the file to decrypt.
   output_filename: The name of the file to write the decrypted data to.
   password: The password to use for decryption.

   Raises:
   FileNotFoundError: If the input file does not exist.
   FileExistsError: If the output file already exists.
   """
   try:
       ensure_file_exists(input_filename)
       ensure_file_does_not_exist(output_filename)
       pyAesCrypt.decryptFile(input_filename, output_filename, password)
   except FileNotFoundError as e:
       print(f"Input file error: {e}")
   except FileExistsError as e:
       print(f"Output file error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('--password', required=True, help='The password to use for encryption and decryption')
   parser.add_argument('--input', default=INPUT_FILE_DEFAULT, help='The input file to encrypt')
   parser.add_argument('--output', default=OUTPUT_FILE_DEFAULT, help='The output file for encrypted data')
   parser.add_argument('--decrypt_output', default=DECRYPT_OUTPUT_DEFAULT, help='The output file for decrypted data')
   args = parser.parse_args()

   # encrypt
   encrypt_file(args.input, args.output, args.password)

   # decrypt
   decrypt_file(args.output, args.decrypt_output, args.password)
