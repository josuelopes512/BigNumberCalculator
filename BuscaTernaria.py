class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node is not None:
            for child in current_node.children:
                if value < child.value:
                    current_node = child
                    break
            else:
                current_node.children.append(new_node)
                return

    def remove(self, value):
        if self.root is None:
            return

        if self.root.value == value:
            if len(self.root.children) == 0:
                self.root = None
            else:
                self.root = self.root.children[0]
            return

        current_node = self.root
        while current_node is not None:
            for i, child in enumerate(current_node.children):
                if value == child.value:
                    if len(child.children) == 0:
                        del current_node.children[i]
                    else:
                        current_node.children[i] = child.children[0]
                    return
                elif value < child.value:
                    current_node = child
                    break
            else:
                return

    def count_nodes(self):
        if self.root is None:
            return 0

        count = 1
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            for child in current_node.children:
                count += 1
                stack.append(child)

        return count

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            for child in current_node.children:
                if value < child.value:
                    current_node = child
                    break
            else:
                return None
        return None
