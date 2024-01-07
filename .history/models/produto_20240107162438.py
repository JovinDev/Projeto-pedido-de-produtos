import json
from models.modelo import Modelo

class Produto:
  def __init__(self, id, nome, preco, descricao, qtd):
    self.set_id(id)
    self.set_nome(nome)
    self.set_preco(preco)
    self.set_descricao(descricao)
    self.set_qtd(qtd)

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_preco(self): return self.__preco
  def get_descricao(self): return self.__descricao
  def get_qtd(self): return self.__qtd

  def set_id(self, id): self.__id = id
  def set_nome(self, nome):
    self.__nome = nome
  def set_preco(self, preco):
    self.__preco = preco 
  def set_descricao(self, descricao): 
    self.__descricao = descricao
  def set_qtd(self, qtd):
    self.__qtd = qtd
    
  def __str__(self):
     return f"{self.__id} - {self.__nome} - R${self.__preco} - {self.__descricao} - {self.__qtd}"

class NProduto(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("produtos.json", mode="r") as arquivo:
        produto_json = json.load(arquivo)
        for obj in produto_json:
          aux = Produto(obj["_Produto__id"], obj["_Produto__nome"], obj["_Produto__preco"], obj["_Produto__descricao"],  obj["_Produto__qtd"] )
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("produtos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
