import socket

registered_users = {}

def register(username, password):
    if login_check(username) == password_check(password) == True:
        pass
    else:
        return "Given credentials are illegal, try again!"
    if username in registered_users:
        return "The entered username is already taken. Please try another one!"
    else:
        registered_users[username] = password
        return "The registration was successful!"

def authentification(username, password):
    if username in registered_users and registered_users[username] == password:
        return f"Successful authentification. Welcome {username}!"
    else:
        return f"Please enter correct username!"

def lenght_check(password):
    if len(password) < 8 or len(password) > 25:
        return False
    else:
        return True
def hazardous_symbol_check(string):
    hazard_list = [';','@','.',',',':']
    for x in hazard_list:
        if x in string:
            return False
    return True
def password_check(password):
    if lenght_check(password) == hazardous_symbol_check(password) == True:
        return True
    else:
        return False
    
def login_check(login):
    if hazardous_symbol_check(login) == True:
        return True
    else:
        return False

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost",8000))
    server_socket.listen()
    print("Server is up and runnin!")

    while True:
        client_socket, address = server_socket.accept()
        print(f"The connection established with {address}")

        reqv = client_socket.recv(1024).decode('utf-8')
        reqv_type, username, password = reqv.split(",")

        if reqv_type == 'register':
            response = register(username,password)
        elif reqv_type == "authentification":
            response = authentification(username,password)
        else:
            response = "The request is invalid. Try again!"
        client_socket.send(response.encode('utf-8'))

        print(f"Recieved request is {reqv_type}, given response is {response}")

        client_socket.close()
if __name__ == "__main__":
    main()

