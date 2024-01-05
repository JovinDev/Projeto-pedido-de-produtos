import streamlit as st
import pandas as pd
from views import View

class ManterPedidoUI:
  def main():
    st.header("Gerenciamento de pedidos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterPedidoUI.listar()
    with tab2: ManterPedidoUI.inserir()
    with tab3: ManterPedidoUI.atualizar()
    with tab4: ManterPedidoUI.excluir()    

  def listar():
    pedidos = View.pedido_listar()
    if len(pedidos) == 0:
      st.write("Nenhuma pedido cadastrado")
    else:
      df = pd.DataFrame(pedidos)
      st.dataframe(df)

  def inserir():
    clientes = View.cliente_listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    produtos = View.produto_listar()
    produto = st.selectbox("Selecione o produto", produtos)
    produtos = View.produto_listar()
    produto = st.write("Selecione a quantidade de produtos que você quer")
    if st.button("Inserir"):
      try:
        View.pedido_inserir( "", cliente.get_id(), produto.get_id(), produto.get_qtd())
        st.success("pedido inserido com sucesso")
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")

  def atualizar():
    pedidos = View.pedido_listar_normal()
    if len(pedidos) == 0:
      st.write("Nenhuma pedido disponível")
    else:  
      op = st.selectbox("Atualização de Produtos", pedidos)
      clientes = View.cliente_listar()
      cliente_atual = View.cliente_listar_id(op.get_id_cliente())
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:  
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      produtos = View.produto_listar()
      produto_atual = View.produto_listar_id(op.get_id_produto())
      if produto_atual is not None:
        produto = st.selectbox("Selecione o novo produto", produtos, produtos.index(produto_atual))
      else:
        produto = st.selectbox("Selecione o novo produto", produtos)
      if st.button("Atualizar"):
        try:
          View.pedido_atualizar(op.get_id(),"", cliente.get_id(), produto.get_id())
          st.success("pedido atualizado com sucesso")
          st.rerun()
        except ValueError as error:
          st.error(f"Erro: {error}")

  def excluir():
    pedidos = View.pedido_listar_str()
    if len(pedidos) == 0:
      st.write("Nenhuma pedido disponível")
    else:  
      op = st.selectbox("Exclusão de Produtos", pedidos)
      if st.button("Excluir"):
        id = int(op.split(" - ")[0])
        View.pedido_excluir(id)
        st.success("pedido excluído com sucesso")
        st.rerun()
