import socket

def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 8000))

    client.send(request.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')

    client.close()

    return response

def menu():
    while True:
        print("Welcome to the Forum! All rights are protected.\n1) Register\n2) Login\n3) Exit")
        selection = int(input())
        login = ''
        response = ''
        if selection == 1:
            while response != "The registration was successful!":
                print("Please, enter your registration credentials.")
                login = input("Enter your login:\nLogin can't have any of the banned symbols (';','@','.',',',':')\n")
                password = input("Enter your password:\nPassword can't have any of the banned symbols (';','@','.',',',':')\nand has to be at least 8 characters long.\n")
                response = send_request(f'register,{login},{password}')
                print(response)
            print('You have registered. Use the 2nd option to log in.')
        elif selection == 2:
            while response != f"Successful authentification. Welcome {login}!":
                print("Please, enter your authentification credentials.")
                login = input("Enter your login: ")
                password = input("Enter your password: ")
                response = send_request(f'authentification,{login},{password}')
                print(response)
            print('The Forum. To exit, use 3rd option')
        else:
            print("Logging off...")
            break
def main():
    menu()
if __name__ == '__main__':
    main()