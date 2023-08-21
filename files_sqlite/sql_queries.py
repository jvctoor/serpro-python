create_table_user = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(45) NOT NULL,
        email VARCHAR(45) UNIQUE,
        cpf VARCHAR(11) NOT NULL
    );
    """

drop_table_user = """
DROP TABLE IF EXISTS user;
"""

insert_user = """
    INSERT INTO user(name, email, cpf) VALUES("João", "jvctor23@gmail.com", "50196230837")
    """
