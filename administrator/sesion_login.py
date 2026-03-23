from administrator.users import users

def validate_login(username, password):
    # Se valida  el login de usuario con el diccionario de datos de usuarios
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Bienvenido, {username}!")
            return True
    return False 

def show_users():
    # Se muestra la lista de usuarios
    for user in users:
        print(f"ID: {user['id']}, Username: {user['username']}")

def create_user(username, password):
    # Se crea un nuevo usuario y se agrega a la lista de usuarios
    new_user = {"id": len(users) + 1, "username": username, "password": password}
    users.append(new_user)
    print(f"Usuario {username} creado exitosamente.")

def delete_user(username):
    # Se elimina un usuario de la lista de usuarios
    global users
    users = [user for user in users if user["username"] != username]
    print(f"Usuario {username} eliminado exitosamente.")
