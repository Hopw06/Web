from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash("mypassword")

print(hashed_password)

login = check_password_hash(hashed_password, "wrongpassword")

print("Login: " + str(login))

login = check_password_hash(hashed_password, "mypassword")

print("Login: " + str(login))