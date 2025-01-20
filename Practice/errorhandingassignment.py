def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()  # Read all contents of the file

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as file:
            file.write(modified_content)  # Write modified content to the new file

        print(f"Successfully written modified content to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "input.txt"  # Name of the file you want to read
output_file = "output.txt"  # Name of the file to write modified content to

read_and_write_file(input_file, output_file)
