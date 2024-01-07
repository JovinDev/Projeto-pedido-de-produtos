import streamlit as st
import pandas as pd
from views import View

class RealizarPedidoUI:
  def main():
    st.header("Produtos disponiveis")
    RealizarPedidoUI.listar_produtos()
    RealizarPedidoUI.realizar_pedido()

  def listar_produtos():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum produto disponivel")
    else:
      dic = []
      for obj in produtos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def realizar_pedido():
    id = st.session_state["cliente_id"]
    produtos = View.produto_listar()
    produto = st.selectbox("Selecione o produto", produtos)
    if produto is not None:
      st.write(f"Quantidade disponível: {produto.get_qtd()}")
      quantidadest.number_input("Quantidade para pedido:")
    
    if st.button("Realizar Pedido"):
      try:
        View.pedido_inserir(0, id, produto.get_id())
        st.success("Pedido realizado com sucesso")
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")
