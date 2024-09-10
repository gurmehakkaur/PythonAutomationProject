import subprocess

def main():
    # Ask user if they want to upload an Excel file
    user_choice = input("Do you want to add an Excel file? (yes/no): ").strip().lower()

    if user_choice == 'yes':
        # Open Flask app to allow file upload
        print("Opening the webpage to upload an Excel file...")
        subprocess.run(["python", "acceptExcel.py"])  # This will block execution until the Flask server is closed

# Run validation and data representation scripts
subprocess.run(["python", "validation.py"])
#subprocess.run(["python", "dataRep.py"])

if __name__ == '__main__':
    main()
