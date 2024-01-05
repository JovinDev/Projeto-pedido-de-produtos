import json

class Item:
    def __init__(self, id, id_produto, id_pedido, preco, qtd ):
        if preco <= 0.00: raise ValueError("preco inválido")
        if qtd <= 0: raise ValueError("Quantidade inválida")
        self.set_id(id)
        self.set_preco(preco)
        self.set_qtd(qtd)
        self.__id_produto = id_produto
        self.__id_pedido = id_pedido
        

    def get_id(self): return self.__id
    def get_preco(self): return self.__preco
    def get_qtd(self): return self.__qtd
    def get_id_produto(self): return self.__id_produto
    def get_id_pedido(self): return self.__id_pedido
    def set_id(self, id): self.__id = id
    def set_preco(self, preco):
        if preco <= 0.00: raise ValueError("Preço inválido")
        self.__preco = preco 
    def set_qtd(self, qtd):
       if qtd <= 0: raise ValueError("Quantidade inválida")
       self.__qtd = qtd
    def set_id_produto(self, id_produto): self.__id_produto = id_produto
    def set_id_pedido(self, id_pedido): self.__id_produto = id_pedido

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
            with open("produtos.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    aux = Item(obj["Item_id"], 
                                  obj["Item_nome"],
                                  obj["Item_descricao"],
                                  obj["Item_preco"])
                    cls.__produtos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.__produtos, arquivo, default=vars)
