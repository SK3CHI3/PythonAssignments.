def main():
    try:
        # Ask the user for the filename to read
        source_file = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(source_file, "r") as file:
            content = file.read()
        
        # Modify the content (e.g., converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_file = "modified_" + source_file
        with open(new_file, "w") as file:
            file.write(modified_content)
        
        print(f"The modified content has been written to {new_file}")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{source_file}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
