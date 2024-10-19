"""
@author Camila Cabezas
@author Felipe Morera
@about main.py -> simple Python script
@version 1.0
@since 10/18/2024
"""

def hello_user(user_name):
    return f"HELLO {user_name} HOW ARE YOU DOING?"

def main():
    user_name = "CAMILA"
    print(hello_user(user_name))

if __name__ == "__main__":
    main()