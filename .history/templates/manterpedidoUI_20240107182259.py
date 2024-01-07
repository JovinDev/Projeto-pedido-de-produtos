import streamlit as st
import pandas as pd
from views import View

class ManterPedidoUI:
  def main():
    st.header("Gerenciamento de pedidos")
    tab1, tab2 = st.tabs(["Listar", "Excluir"])
    with tab1: ManterPedidoUI.listar()
    with tab2: ManterPedidoUI.excluir()    

  def listar():
    pedidos = View.pedido_listar_normal()
    if len(pedidos) == 0:
      st.write("Nenhuma pedido cadastrado")
    else:
      df = pd.DataFrame(pedidos)
      st.dataframe(df)

  def excluir():
    pedidos = View.pedido_listar_str()
    if len(pedidos) == 0:
      st.write("Nenhuma pedido disponível")
    else:  
      op = st.selectbox("Exclusão de Produtos", pedidos)
      if st.button("Excluir"):
        id = op.get_id()
        View.pedido_excluir(id)
        st.success("pedido excluído com sucesso")
        st.rerun()
