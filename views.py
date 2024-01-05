from models.cliente import Cliente, NCliente
from models.produto import Produto, NProduto
from models.pedido import Pedido, NPedido
from models.item import Item, NItem



class View:
  def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    if nome == "" or email == "" or fone == "" or senha == "": raise ValueError("Nome, e-mail, fone ou senha vazios")
    for obj in View.cliente_listar():
      if obj.get_email() == email: raise ValueError("E-mail repetido")
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    if nome == "" or email == "" or fone == "" or senha == "": raise ValueError("Nome, e-mail, fone ou senha vazios")
    for obj in View.cliente_listar():
      if obj.get_email() == email: raise ValueError("E-mail repetido")
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")  

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None

  def produto_listar():
    return NProduto.listar()

  def produto_listar_id(id):
    return NProduto.listar_id(id)
   
  def produto_inserir(id_produto, nome, descricao, preco, qtd):
    if nome == "": raise ValueError("Nome vazio")
    if descricao == "": raise ValueError("Descrição vazia")
    if preco == 0.00: raise ValueError("Preço invalido")
    if qtd <= 0.00: raise ValueError("Quantidade invalida")
    NProduto.inserir(Item(0, id_produto, nome, descricao, preco, qtd))

  def produto_excluir(id):
    NItem.excluir(Item(id, "", "", 0))

  def produto_atualizar(id, nome, descricao, preco, qtd):
    if nome == "": raise ValueError("Nome vazio")
    if descricao == "": raise ValueError("Descrição vazia")
    if preco <= 0.00: raise ValueError("Preço invalido")
    if qtd <= 0.00: raise ValueError("Quantidade invalida")
    NProduto.atualizar(Produto(id, nome, descricao, preco, qtd))

 

  def pedido_listar_normal():
    return NPedido.listar()

  def pedido_listar():
    pedidos = NPedido.listar()
    lista = []
    for pedido in pedidos:
      cliente = View.cliente_listar_id(pedido.get_id_cliente())
      Produto = View.produto_listar_id(pedido.get_id_produto())
      dic = {"ID Locação": pedido.get_id(), "Cliente": cliente.get_nome(), "Produto": Produto.get_nome()}
      lista.append(dic)

    return lista

  def pedido_listar_str():
    pedidos = NPedido.listar()
    lista = []
    for pedido in pedidos:
      cliente = View.cliente_listar_id(pedido.get_id_cliente())
      produto = View.produto_listar_id(pedido.get_id_produto())
      dicstr = pedido.to_str() + " - " + cliente.get_nome() + " - " + produto.get_nome()
      lista.append(dicstr)

    return lista

  def pedido_listar_id(id):
    return NPedido.listar_id(id)

  def pedido_inserir( id_cliente, id_Produto):
    produtos = NProduto.listar()
    for produto in produtos:
      if id_Produto == produto.get_id():
        if produto.get_disponivel() == False:
          produto.set_disponivel(True)
          NProduto.atualizar(produto) 
          NPedido.inserir(Pedido(0, id_cliente, id_Produto))
          return
        else:
          raise ValueError("Produto indisponivel")

  def pedido_atualizar(id, id_cliente, id_Produto):
    produtos = NProduto.listar()
    for produto in produtos:
      if id_Produto == produto.get_id():
        if produto.get_disponivel() == False:
          produto.set_disponivel(True)
          NProduto.atualizar(produto)
          NPedido.atualizar(Pedido(id, id_cliente, id_Produto))
          return
        else:
          raise ValueError("Produto indisponivel")
        
  def pedido_excluir(id):
    NPedido.excluir(Pedido(id, "", "", 0, 0))

  def editar_perfil(id, nome, email, fone, senha):
    NCliente.atualizar(Cliente(id, nome, email, fone, senha))

  def meus_pedidos( idcliente):
    pedidos = []
    
    for pedido in View.pedido_listar_normal():
        if pedido.get_id_cliente() == idcliente:
                pedidos.append(Pedido)
    
    return pedidos
  
  def listar_produtos_nao_disponiveis():
    nao_disponivel = []
    for produto in View.produto_listar():
      if produto.get_disponivel() == False:
        nao_disponivel.append(produto)
    
    return nao_disponivel
  
  def buscar_produto(titulo):
        produtos_encontrados = []

        for produto in NProduto.listar():
            if produto.get_titulo().lower() == titulo.lower():
                produtos_encontrados.append(produto)

        return produtos_encontrados
  
  def buscar_pedido_usuario(pedido_cliente):
      pedidos = View.pedido_listar_normal()
      resultado = []
      for pedido in pedidos:
        if pedido.get_id_cliente() == pedido_cliente.get_id():
          resultado.append(pedido)
        
      return resultado

        
  def meus_produtos_de_agora(id_cliente):
     produtos = []
     for pedido in View.pedido_listar_normal():
       if pedido.get_id_cliente() == id_cliente:
         for produto in View.produto_listar():
           if produto.get_id() == pedido.get_id_produto() and produto.get_disponivel() == True:
             produtos.append(produto)

     return produtos
  
