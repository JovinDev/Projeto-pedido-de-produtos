import streamlit as st
import pandas as pd
from views import View
import time

class RealizarPedidoUI:
  def main():
    st.header("Produtos disponiveis")
    RealizarPedidoUI.listar_produto()
    RealizarPedidoUI.realizar_pedido()

  def produtos_produtos():
    agendas = View.listar_produtos_nao_alugados()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def realizar_pedido():
    id = st.session_state['cliente_id']
    produtos = View.listar_produtos_nao_disponiveis()
    produto = st.selectbox("Selecione o produto", produtos)
    if st.button("Realizar Pedido"):
      try:
        View.Pedido_inserir( "", id, produto.get_id())
        st.success("Pedido realizado com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")