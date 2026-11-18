import os
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print("file Name {filename} : Created successfully!")
    except FileExistsError:
        print(F'File name {filename} already exists')
    except Exception as E:
        print('An error occured')
def view_all_files():
    files = os.listdir()
    if not files:
        print('No files found')
    else:
        print('Files in directory')
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileExistsError:
        print(f'file not found')
    except Exception as e:
        print('An error occured')
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")
    except FileExistsError:
        print(f"{filename} does not exist")
    except Exception as e:
        print("An error occured")
def  edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print('Content added to {filename} successfully')
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as e:
        print('An error occured')
def main():
    while True:
        print('File Management app')
        print('1: Create file')
        print('2: view all files')
        print('3: delete file')
        print('4: update file')
        print('5: read file')
        print('6: exit')

        choice = input('Enter your choice(1-6) = ')

        if choice == '1':
            filename = input("Enter the file-name to create = ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input('Enter the file you want to delete')
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read = ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name to edit = ")
            edit_file(filename)
        elif choice == "6":
            print('clocing the app...')
            break
        else:
            print('In-valid syntax')

      
if __name__ == "__main__":
    main()


