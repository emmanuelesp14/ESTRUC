from queue import Queue

class NumberManager:
    def __init__(self):
        self.unique_numbers = set()
        self.number_queue = Queue()
        self.number_stack = []

    def add_number(self, number):
        if number not in self.unique_numbers:
            self.unique_numbers.add(number)
            self.number_queue.put(number)
            self.number_stack.append(number)

    def display_numbers(self):
        print("Números únicos en la cola:")
        while not self.number_queue.empty():
            print(self.number_queue.get())

        print("\nNúmeros únicos en la pila:")
        for num in reversed(self.number_stack):
            print(num)

if __name__ == "__main__":
    number_manager = NumberManager()

    while True:
        try:
            input_number = int(input("Ingrese un número (0 para salir): "))
            if input_number == 0:
                break
            number_manager.add_number(input_number)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    number_manager.display_numbers()