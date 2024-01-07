import json


class Item:
  def __init__(self, id, id_pedido, preco, id_produto, qtd):
    self.set_id(id)
    self.set_id_pedido(id_pedido)
    self.set_preco(preco)
    self.set_id_produto(id_produto)
    self.set_qtd(qtd)

  def get_id(self): return self.__id
  def get_id_pedido(self): return self.__id_pedido
  def get_preco(self): return self.__preco
  def get_id_produto(self): return self.__id_produto
  def get_qtd(self): return self.__qtd

  def set_id(self, id): self.__id = id
  def set_id_pedido(self, id_pedido):
    self.__id_pedido = id_pedido
  def set_preco(self, preco):
    self.__preco = preco 
  def set_id_produto(self, id_produto): 
    self.__id_produto = id_produto
  def set_qtd(self, qtd):
    self.__qtd = qtd
    
    def __str__(self):
     return f"{self.__id} - {self.__id_pedido} - {self.__id_produto} - R${self.__preco} - {self.__qtd}"



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
                                  obj["Item_id_pedido"],
                                  obj["Item_preco"],
                                  obj["Item_qtd"])
                    cls.__produtos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.__produtos, arquivo, default=vars)
