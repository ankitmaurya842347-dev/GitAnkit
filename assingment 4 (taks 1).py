def read_file():
    try:
        # try to open and read file
        with open("asign4.txt",'r') as file:
            for data in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file asign4.txt does not exists")
    
    except Exception as f_data:
        print(f"An unexpected error occurred: {f_data}")
        
#calling the function
read_file()