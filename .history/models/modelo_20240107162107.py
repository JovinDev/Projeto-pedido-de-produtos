from abc import ABC, abstractclassmethod

class Modelo(ABC):
  objetos = []

  @classmethod
  def Inserir(cls, obj):
    cls.Abrir()
    id = 0
    for aux in cls.objetos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.objetos.append(obj)
    cls.Salvar()

  @classmethod
  def listar(cls):
    cls.Abrir()
    return cls.objetos

  @classmethod
  def listar_Id(cls, id):
    cls.Abrir()
    for obj in cls.objetos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.Abrir()
    aux = cls.Listar_Id(obj.get_id())
    cls.objetos.remove(aux)
    cls.objetos.append(obj)
    cls.Salvar()

  @classmethod
  def excluir(cls, obj):
    cls.Abrir()
    aux = cls.Listar_Id(obj.get_id())
    cls.objetos.remove(aux)
    cls.Salvar()

  @abstractclassmethod
  def abrir(cls):
    pass

  @abstractclassmethod
  def salvar(cls):
    pass
