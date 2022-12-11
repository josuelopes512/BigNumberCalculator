import sys
from BPlusTreeNode import BPlusTree
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QLineEdit, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import QTimer


class BPlusTreeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.tree = BPlusTree(t=3)

        self.init_ui()

    def init_ui(self):
        # Crie os widgets da interface gráfica
        self.insert_label = QLabel("Inserir chave:")
        self.key_input = QLineEdit()
        
        self.insert_button = QPushButton("Inserir")
        
        self.delete_label = QLabel("Deletar chave:")
        self.delete_button = QPushButton("Delete")
        
        self.search_label = QLabel("Pesquisar chave:")
        self.search_button = QPushButton("Search")
        self.key_input = QLineEdit()
        
        # Defina as ações para os botões de inserção, remoção e busca
        self.insert_button.clicked.connect(self.insert_key)
        self.delete_button.clicked.connect(self.delete_key)
        self.search_button.clicked.connect(self.search_key)
        
        # Crie o layout da janela
        layout = QVBoxLayout()
        layout.addWidget(self.key_input)
        layout.addWidget(self.insert_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.search_button)
        layout.addWidget(self.search_button)
        self.setLayout(layout)

    def insert_key(self):
        # Obtenha o valor da chave a ser inserida
        key = self.key_input.text()

        # Inserir a chave na árvore
        self.tree.insert(key)

        # Limpe o campo de entrada de texto
        self.key_input.clear()
        
        self.on_button_clicked(f"Key {key} is insert")

    def delete_key(self):
        # Obtenha o valor da chave a ser removida
        key = self.key_input.text()

        # Remova a chave da árvore
        if self.tree.delete(key):
            self.on_button_clicked(f"Key {key} is deleted")
        else:
            self.on_button_clicked(f"Key {key} not found")

        # Limpe o campo de entrada de texto
        self.key_input.clear()

    def search_key(self):
        # Obtenha o valor da chave a ser buscada
        key = self.key_input.text()

        # Busque a chave na árvore
        if self.tree.search(key):
            self.on_button_clicked(f"Key {key} found in the tree")
        else:
            self.on_button_clicked(f"Key {key} not found in the tree")

        # Limpe o campo de entrada de texto
        self.key_input.clear()
    
    def on_button_clicked(self, message):
        alert = QMessageBox()
        alert.setText(message)
        alert.exec()

app = QApplication(sys.argv)
window = BPlusTreeGUI()
window.show()
app.exec()


# QTimer.singleShot(1, window) # call startApp only after the GUI is ready
# sys.exit(app.exec_())