import os

def file_processing():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the output file: ")
    
    try:
        # Verify input file exists before trying to open
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
            
        # Check if output file is in a valid directory
        output_dir = os.path.dirname(output_filename)
        if output_dir and not os.path.exists(output_dir):
            raise IOError(f"Output directory '{output_dir}' does not exist.")
            
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Try to write to the output file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
            print(f"Success! Modified content written to {output_filename}")
            
        except PermissionError:
            print(f"Error: Permission denied when trying to write to {output_filename}")
        except IOError as e:
            print(f"Error writing to file: {str(e)}")
            
    except FileNotFoundError as e:
        print(str(e))
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It may not be a text file.")
    except IOError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    file_processing()
    