#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de contrasenas seguras
con base en entrada de longitud
de contrasena provista por el usuario.
"""

# Importar librerias requeridas
import secrets, string

# Funcion que genera la contrasena con base la longitud definido por usuario
def generate_password(length):
    # La variable chars almacena caracteres mayusculas, minusculas, digitos y simbolos especiales
    # provisto por la lib. string
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # La variable password almacena provisto por la lib. secrets 
    # desde variable chars y asegura la longitud recibida
    password = ''.join(secrets.choice(chars) for i in range(length))
    # Retorna la variable passwordcuando finaliza la funcion 
    return password

# Funcion main para dsplegar menu y recibir datos del usuario
def main():
    # Muestra un menu muy basico al usuario
    print("\n +-Generador de Contrasenas Seguras-+")
    print("\n Seleccione la longitud de contrasena requerida: ")
    print("\t\t 1. 12 caracteres (por defecto) ")
    print("\t\t 2. 15 caracteres ")
    print("\t\t 3. 20 caracteres ")
    # La variable option almacena el valor emitido por el usuario
    option = int(input("\n Ingrese la opcion deseada [1-2-3]: ").strip())
    
    # Valida condiciones para determinar la longitud 
    if option == 2:
        longitud = 15
    elif option == 3:
        longitud = 20
    else:
        longitud = 12
        
    # Se invoca la funcion previa y se remite la longitud recibida
    passwd = generate_password(longitud)
    # Mostramos la contrasena generada
    print("\n La Contrasena generada es: ", passwd)

# Invocacion de funcion main
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
