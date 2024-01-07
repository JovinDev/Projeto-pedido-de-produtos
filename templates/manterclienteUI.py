import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    tab1, tab2, = st.tabs(["Listar", "Excluir"])
    with tab1: ManterClienteUI.listar()
    with tab2: ManterClienteUI.excluir()

  def listar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      dic = [{"ID Cliente": cliente.get_id(), "Nome": cliente.get_nome(), "E-mail" : cliente.get_email(), "Fone": cliente.get_fone()} for cliente in clientes]
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def excluir():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Exclusão de Clientes", clientes)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Cliente excluído com sucesso")
        time.sleep(2)
        st.rerun()
