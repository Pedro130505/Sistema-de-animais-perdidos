def password_hash(senha):

    import bcrypt
    senha_bytes = senha.encode('utf-8')

    salt = bcrypt.gensalt()  # Gera um salt aleatório e seguro

    # Hashing Password
    hashed = bcrypt.hashpw(password=senha_bytes, salt=salt)  # Gera o hash da senha usando o salt
    return hashed 
    # Hashed Password
    #print(f"Hashed Password: {hashed.decode('utf-8')}")
