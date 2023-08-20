create_table_user = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(45) NOT NULL,
        email VARCHAR(45) NOT NULL UNIQUE,
        cpf VARCHAR(11) NOT NULL UNIQUE
    );
    """

insert_user = """
    INSERT INTO user(name, email, cpf) VALUES("João", "jvctor23@gmail.com", "50196230837")
    """
