import json


class Pedido:
  def __init__(self, id, id_cliente, id_produto, qt):
    self.set_id(id)
    self.set_id_cliente(id_cliente)
    self.set_id_produto(id_produto)

  def get_id(self): return self.__id
  def get_id_cliente(self): return self.__id_cliente
  def get_id_produto(self): return self.__id_produto

  def set_id(self, id): self.__id = id
  def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
  def set_id_produto(self, id_produto): self.__id_produto = id_produto
  
  def __str__(self):
    return f"{self.__id} - {self.__id_cliente} - {self.__id_produto}"
  
  def to_json(self):
     return {
        "id": self.__id,
        "id_cliente": self.__id_cliente,
        "id_produto": self.__id_produto
     }

class NPedido:
  __Pedidos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__Pedidos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__Pedidos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__Pedidos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__Pedidos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_id_cliente(obj.get_id_cliente())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__Pedidos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
        cls.__Pedidos = []
        try:
            with open("pedidos.json", mode="r") as arquivo:
                pedidos_json = json.load(arquivo)
                for obj in pedidos_json:
                    aux = Pedido( obj["id"], 
                                  obj["id_produto"],
                                  obj["id_cliente"])
                    cls.__Pedidos.append(aux)
        except FileNotFoundError:
            pass

  @classmethod
  def salvar(cls):
    with open("pedidos.json", mode="w") as arquivo:
      json.dump(cls.__Pedidos, arquivo, default=Pedido.to_json)
