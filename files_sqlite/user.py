
class User:
    def __init__(self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf

    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self, email):
        return self.email

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_cpf(self, cpf):
        return self.cpf

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, CPF: {self.cpf}"