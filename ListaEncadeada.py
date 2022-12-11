class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def to_list(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return result

    def remove(self, value):
        # Caso especial se o valor estiver no nó inicial
        if self.head.value == value:
            self.head = self.head.next
            return

        # Procure o valor na lista
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.value == value:
                # Remova o valor
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

        # Se o valor não foi encontrado, lança um erro
        raise ValueError("Value not found in the list.")

    def insert(self, value, position):
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_position = 0
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_position == position:
                new_node.next = current_node
                previous_node.next = new_node
                return
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

        # Se a posição não foi encontrada, adicione o novo nó no final da lista
        previous_node.next = new_node

if __name__ == '__main__':
    # Criar uma nova lista encadeada
    linked_list = LinkedList()

    # Adicionar alguns elementos
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Inserir um valor em uma posição específica
    linked_list.insert(0, 1)

    # Converter a lista encadeada em uma lista
    print(linked_list.to_list())  # [1, 3]
