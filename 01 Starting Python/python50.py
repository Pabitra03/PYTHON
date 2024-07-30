# Open a file in read and write mode
with open('myfile.txt', 'w+') as file:
    # Write some data to the file
    file.write('Hello, World!')

    # Print the current position of the file pointer
    print('Current position:', file.tell())

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Print the current position of the file pointer
    print('Current position after seek(0):', file.tell())

    # Read the data from the file
    data = file.read()

    # Print the data
    print('Data:', data)

    # Move the file pointer to the 7th character in the file
    file.seek(7)

    # Print the current position of the file pointer
    print('Current position after seek(7):', file.tell())

    # Read the data from the current position to the end of the file
    data = file.read()

    # Print the data
    print('Data after seek(7):', data)

    # Move the file pointer to the end of the file
    file.seek(0, 2)

    # Print the current position of the file pointer
    print('Current position after seek(0, 2):', file.tell())

    # Move the file pointer 5 characters before the end of the file
    # file.seek(-5, 2)

    # Print the current position of the file pointer
    print('Current position after seek(-5, 2):', file.tell())

    # Read the data from the current position to the end of the file
    data = file.read()

    # Print the data
    print('Data after seek(-5, 2):', data)