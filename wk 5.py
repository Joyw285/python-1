def read_and_modify_file():
    try:
     
        source_file = input("joy_resume: ")
        with open(source_file, "r") as f:
            content = f.read()

        # Modify the content (example: uppercase it)
        modified_content = content.upper()

        # Ask for output filename
        output_file = input("joy.plp ")

        # Write modified content to new file
        with open(output_file, "joy.plp") as f:
            f.write(modified_content)

        print(f"Success! Modified content written to '{output_file}'.")

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the program
read_and_modify_file()
