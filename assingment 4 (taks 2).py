def write_and_read_file():
    usr_input = input("Enter text to write to the file: ")
    
    with open ("asign4.txt",'w') as file:
        file.write(usr_input + "\n")
        
    print("Data written successsfully.")
    
    addition_input = input("Enter extra text to append: ")
    with open("asign4.txt",'a') as file:
        file.write(addition_input + "\n")
        
    print("Extra data appended successfully.")
    
    print("\nFinal context of the file:")
    with open("asign4.txt",'r') as file:
        for line in file:
            print(line.strip())
            
            
#calling the funciton
write_and_read_file()