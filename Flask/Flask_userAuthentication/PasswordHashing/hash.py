from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "supersecretpassword"

hashed_password = bcrypt.generate_password_hash(password)

print(hashed_password)

login = bcrypt.check_password_hash(hashed_password, "supersecretpassword")

print("Login: " + str(login))