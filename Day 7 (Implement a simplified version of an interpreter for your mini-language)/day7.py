class MiniInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, command):
        command = command.strip()
        if command.startswith("print"):
            var_name = self.extract_variable_from_print(command)
            if var_name in self.variables:
                print(self.variables[var_name])
            else:
                raise ValueError(f"Variabile '{var_name}' non definita")
        elif "=" in command:
            var_name, expression = command.split("=", 1)
            var_name = var_name.strip()
            expression = expression.strip()
            value = self.evaluate_expression(expression.split())
            self.variables[var_name] = value
        else:
            raise ValueError(f"Comando non riconosciuto: {command}")

    def extract_variable_from_print(self, command):
        if command.startswith("print(") and command.endswith(")"):
            return command[6:-1].strip()  # Rimuove 'print(' e ')'
        raise ValueError(f"Comando print non valido: {command}")

    def evaluate_expression(self, tokens):
        if len(tokens) == 1:
            return self.get_value(tokens[0])
        elif len(tokens) == 3:
            left = self.get_value(tokens[0])
            operator = tokens[1]
            right = self.get_value(tokens[2])
            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right
            elif operator == "/":
                return left / right
            else:
                raise ValueError(f"Operatore non valido: {operator}")
        else:
            raise ValueError(f"Espressione non valida: {' '.join(tokens)}")

    def get_value(self, token):
        if token.isdigit():
            return int(token)
        elif token in self.variables:
            return self.variables[token]
        else:
            raise ValueError(f"Token non riconosciuto: {token}")


if __name__ == "__main__":
    interpreter = MiniInterpreter()
    commands = [
        "x = 5",
        "y = x + 3",
        "print(x)",
        "print(y)"
    ]
    for command in commands:
        interpreter.execute(command)
