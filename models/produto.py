import json

class Produto:
  def __init__(self, id, nome, preco, descricao, qtd, disponivel):
    if nome == "": raise ValueError(" inválido")
    if preco <= 0.00: raise ValueError("preco inválido")
    if descricao == "": raise ValueError("Descrição inválida")
    if qtd <= 0: raise ValueError("Quantidade inválido")
    self.set_id(id)
    self.set_nome(nome)
    self.set_preco(preco)
    self.set_descricao(descricao)
    self.set_qtd(qtd)
    self.set_disponivel(disponivel)

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_preco(self): return self.__preco
  def get_descricao(self): return self.__descricao
  def get_qtd(self): return self.__qtd
  def get_disponivel(self): return self.__disponivel

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
  def set_qtd(self, qtd):
    if qtd <= 0.00: raise ValueError("quantidade inválida")
    self.__qtd = qtd
  def set_disponivel(self, disponivel): self.__disponivel = disponivel

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__preco == x.__preco and self.__descricao == x.__descricao and self.__qtd == x.__qtd and self.__disponivel == x.__disponivel:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__preco} - {self.__descricao} - {self.__qtd} - {self.__disponivel}"

class NProduto:
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
  def listar(cls):
    cls.abrir()
    return cls.__produtos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__produtos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_preco(obj.get_preco())
      aux.set_descricao(obj.get_descricao())
      aux.set_qtd(obj.get_qtd())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__produtos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__produto = []
    try:
      with open("produto.json", mode="r") as arquivo:
        produto_json = json.load(arquivo)
        for obj in produto_json:
          aux = Produto(obj["_produto__id"], obj["_produto__nome"], obj["_produto__descricao"], obj["_produto__preco"], obj["_produto__disponivel"])
          cls.__produto.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("produtos.json", mode="w") as arquivo:
      json.dump(cls.__produtos, arquivo, default=vars)
