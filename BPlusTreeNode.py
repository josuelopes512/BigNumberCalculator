class Node:
    def __init__(self, keys=[], leaf=False):
        self.leaf = leaf
        self.keys = keys
        self.pointers = []

class BPlusTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def insert(self, key):
        # Se a raiz da árvore estiver vazia, crie um novo nó raiz
        if not self.root:
            self.root = Node([key], leaf=True)
            return

        # Encontre o nó folha onde o valor deve ser inserido
        current_node = self.find_leaf_node(key)

        # Se o nó já estiver cheio, divida-o em dois nós
        if len(current_node.keys) == 2 * self.t - 1:
            self.split_node(current_node)

            # Depois de dividir o nó, encontre novamente o nó folha onde o valor deve ser inserido
            current_node = self.find_leaf_node(key)

        # Adicione a chave ao nó folha
        current_node.keys.append(key)
        current_node.keys.sort()

    def delete(self, key):
        # Encontre o nó folha onde a chave está localizada
        leaf_node = self.find_leaf_node(key)

        # Se a chave não estiver presente no nó, retorne um erro
        if key not in leaf_node.keys:
            return "Key not found"

        # Remova a chave do nó
        leaf_node.keys.remove(key)

        # Se o nó estiver vazio e não for a raiz da árvore, una-o com outro nó
        if len(leaf_node.keys) == 0 and leaf_node != self.root:
            self.merge_nodes(leaf_node)
        
        return False

    def search(self, key):
        # Encontre o nó folha onde a chave pode estar localizada
        leaf_node = self.find_leaf_node(key)

        # Verifique se a chave está presente no nó
        return key in leaf_node.keys

    def split_node(self, node):
        # Obtenha o índice da chave central do nó
        middle_index = len(node.keys) // 2

        # Crie dois novos nós com as chaves a esquerda e a direita da chave central
        left_node = Node(node.keys[:middle_index])
        right_node = Node(node.keys[middle_index + 1:])

        # Se o nó for um nó folha, atualize os apontadores para os novos nós
        if node.leaf:
            left_node.pointers = node.pointers[:middle_index + 1]
            right_node.pointers = node.pointers[middle_index + 1:]
        else:
            # Se o nó não for um nó folha, atualize os apontadores para os filhos dos novos nós
            left_node.pointers = node.pointers[:middle_index + 1]
            right_node.pointers = node.pointers[middle_index:]

        # Atualize os apontadores do nó pai para os novos nós
        if node.parent:
            node_index = node.parent.pointers.index(node)
            node.parent.pointers = node.parent.pointers[:node_index] + [
                left_node, right_node] + node.parent.pointers[node_index + 1:]

            # Adicione a chave central do nó original ao nó pai
            node.parent.keys.append(node.keys[middle_index])
            node.parent.keys.sort()
        else:
            # Se o nó não tiver um pai, crie um novo nó pai com a chave central do nó original
            self.root = Node([node.keys[middle_index]],
                             pointers=[left_node, right_node])

        # Atualize os pais dos novos nós
        left_node.parent = right_node.parent = self.root

    def merge_nodes(self, node):
        # Encontre o índice do nó na lista de filhos do pai
        node_index = node.parent.pointers.index(node)

        # Encontre o nó irmão a esquerda ou a direita do nó
        if node_index == 0:
            sibling_node = node.parent.pointers[node_index + 1]
        else:
            sibling_node = node.parent.pointers[node_index - 1]

        # Se o nó irmão tiver menos de t - 1 chaves, una-o com o nó
        if len(sibling_node.keys) < self.t - 1:
            # Adicione as chaves e os apontadores do nó ao nó irmão
            sibling_node.keys += node.keys
            sibling_node.keys.sort()

            if node.leaf:
                sibling_node.pointers += node.pointers
            else:
                sibling_node.pointers += node.pointers[1:]

            # Atualize os apontadores do pai para apontar para o nó irmão
            node.parent.pointers.remove(node)

            # Se o nó pai ficar vazio, una-o com o nó irmão
            if len(node.parent.keys) == 0:
                self.merge_nodes(node.parent)

    def find_leaf_node(self, key):
        # Inicie a busca na raiz da árvore
        current_node = self.root

        while not current_node.leaf:
            # Percorra os apontadores do nó até encontrar o nó mais adequado para a chave
            for i in range(len(current_node.keys)):
                if key < current_node.keys[i]:
                    current_node = current_node.pointers[i]
                    break
                else:
                    current_node = current_node.pointers[-1]

        # Retorne o nó folha encontrado
        return current_node

if __name__ == '__main__':
    tree = BPlusTree(3)
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.insert(2)

    assert tree.search(5) == True
    assert tree.search(4) == True
    assert tree.search(7) == True
    assert tree.search(2) == True

    tree.delete(5)
    assert tree.search(5) == False

    tree.delete(4)
    assert tree.search(4) == False

    tree.delete(7)
    assert tree.search(7) == False


# class BPlusTreeNode:
#     # inicializa um novo nó da árvore B+
#     def __init__(self, is_leaf=False):
#         self.is_leaf = is_leaf
#         self.keys = []
#         self.children = []

#     # insere um novo elemento na árvore B+
#     def insert(self, key, value):
#         # se o nó é uma folha, basta adicionar o elemento à lista de chaves
#         if self.is_leaf:
#             self.keys.append((key, value))
#             return

#         if not self.keys:
#             self.keys.append([])
#             self.keys[0].append([0])

#         # se o nó não é uma folha, encontre o filho apropriado para inserir o elemento
#         index = 0
#         while index < len(self.keys) and key > self.keys[index][0]:
#             index += 1
#         self.children[index].insert(key, value)

#     # recupera um elemento da árvore B+
#     def get(self, key):
#         # se o nó é uma folha, procura o elemento na lista de chaves
#         if self.is_leaf:
#             for k, v in self.keys:
#                 if k == key:
#                     return v
#             return None

#         # se o nó não é uma folha, encontra o filho apropriado para recuperar o elemento
#         index = 0
#         while index < len(self.keys) and key > self.keys[index][0]:
#             index += 1
#         return self.children[index].get(key)

#     # remove um elemento da árvore B+
#     def remove(self, key):
#         # se o nó é uma folha, basta remover o elemento da lista de chaves
#         if self.is_leaf:
#             for i, (k, v) in enumerate(self.keys):
#                 if k == key:
#                     del self.keys[i]
#                     return
#             return

#         # se o nó não é uma folha, encontra o filho apropriado para remover o elemento
#         index = 0
#         while index < len(self.keys) and key > self.keys[index][0]:
#             index += 1
#         self.children[index].remove(key)

#     # imprime a árvore B+
#     def __str__(self):
#         # se o nó é uma folha, imprime suas chaves
#         if self.is_leaf:
#             return "Leaf: " + str(self.keys)

#         # se o nó não é uma folha, imprime cada um de seus filhos
#         result = ""
#         for i, (key, value) in enumerate(self.keys):
#             result += str(self.children[i]) + " " + str(key) + " "
#         result += str(self.children[-1])
#         return result


# if __name__ == "__main__":
    # cria uma nova árvore B+
    # tree = BPlusTreeNode()

    # # insere alguns elementos na árvore
    # tree.insert(1, "Hello")
    # tree.insert(2, "World")
    # tree.insert(3, "!")

    # # imprime a árvore
    # print(tree)
