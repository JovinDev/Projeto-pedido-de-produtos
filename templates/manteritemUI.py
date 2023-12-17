import streamlit as st
import pandas as pd
from views import View

class ManterItemUI:
  def main():
    st.header("Cadastro de itens")
    tab1, tab2 = st.tabs(["Inserir", "Excluir"])
    with tab1: ManterItemUI.inserir()
    with tab2: ManterItemUI.excluir()    

  def inserir():
    nome = st.text_input("Informe o nome do produto")
    descricao = st.text_input("Informe a descrição do produto")
    preco = st.text_input("Informe o valor do produto (R$)")
    quantidade = st.number_input("Quantas unidades desse produto existem?")
    if st.button("Inserir"):
      try:
        View.item_inserir(nome, descricao, float(preco), quantidade, False)
        st.success("produto inserido com sucesso")
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")

      
  def excluir():
    items = View.pedido_listar_str()
    if len(items) == 0:
      st.write("Nenhuma item disponível")
    else:  
      op = st.selectbox("Exclusão de Produtos", items)
      if st.button("Excluir"):
        id = int(op.split(" - ")[0])
        View.item_excluir(id)
        st.success("item excluído com sucesso")
        st.rerun()