import os

def main():
    directory_input = input("Please provide the directory where you would like to store the file: ")
    file_name_input = input("Please provide the name of the file you wish to create: ")
    text_file = f"{file_name_input}.txt"
    full_path = os.path.join(directory_input, text_file)

    if not os.path.isdir(directory_input):
        os.makedirs(directory_input)

    name_input = input("Please provide your full name: ")
    address_input = input("Please provide your address: ")
    phone_number_input = input("Please provide your phone number: ")

    with open(full_path, 'w') as file:
        file.write(f'{name_input}, {address_input}, {phone_number_input}')

    with open(full_path, 'r') as file:
        file_read = file.read()
        # i wanted to print the file read into a more user friendly way but that's not a requirement 
        print(file_read)
if __name__=="__main__":
    main()