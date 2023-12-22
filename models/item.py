import json

class Item:
    def __init__(self, id, nome, descricao, preco, quantidade, id_produto, id_pedido):
        if nome == "": raise ValueError("Título inválido")
        if preco <= 0.00: raise ValueError("preco inválido")
        if descricao == "": raise ValueError("Descrição inválida")
        if quantidade <= 0: raise ValueError("Quantidade inválida")
        self.set_id(id)
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.__id_produto = id_produto
        self.__id_produto = id_pedido
        

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_preco(self): return self.__preco
    def get_descricao(self): return self.__descricao
    def get_quantidade(self): return self.__quantidade
    def get_id_produto(self): return self.__id_produto

    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_preco(self, preco):
        if preco <= 0.00: raise ValueError("Preço inválido")
        self.__preco = preco 
    def set_descricao(self, descricao): 
        if descricao == "": raise ValueError("Descrição inválido")
        self.__descricao = descricao
    def set_quantidade(self, quantidade): self.__quantidade = quantidade
    def set_id_produto(self, id_produto): self.__id_produto = id_produto

    def __eq__(self, x):
     if self.__id == x.__id and self.__nome == x.__titulo and self.__descricao == x.__descricao and self.__preco == x.__preco and self.__quantidade == x.__quantidade:
      return True
     return 
    
    def __str__(self):
     return f"{self.__id} - {self.__nome} - {self.__descricao} - {self.__preco} R$ - {self.__quantidade}"



class NItem:
    __produtos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__produtos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__produtos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
     cls.abrir()
     for obj in cls.__filmes:
      if obj.get_id() == id: return obj
     return None

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__produtos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__produtos = []
        try:
            with open("itens.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    aux = Item(obj["_Item__id"], 
                                  obj["_Item__id_produto"],
                                  obj["_Item__nome"],
                                  obj["_Item__descricao"],
                                  obj["_Item__preco"],
                                  obj["_Item__quantidade"]),
                    cls.__produtos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("itens.json", mode="w") as arquivo:
            json.dump(cls.__produtos, arquivo, default=vars)