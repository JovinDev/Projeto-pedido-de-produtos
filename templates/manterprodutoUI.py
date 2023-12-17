import streamlit as st
import pandas as pd
from views import View

class ManterProdutoUI:
  def main():
    st.header("Gestão de Produtos")
    tab1, tab2, = st.tabs(["Listar", "Atualizar",])
    with tab1: ManterProdutoUI.listar()
    with tab2: ManterProdutoUI.atualizar()
  

  def listar():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum Produto cadastrado")
    else:  
      dic = [{"ID produto": produto.get_id(), "nome": produto.get_nome(), "preco": produto.get_preco(), "Descrição" : produto.get_descricao(), "Estoque": produto.get_estoque(), "disponibilidade" : produto.get_disponivel()} for produto in produtos]
      df = pd.DataFrame(dic)
      st.dataframe(df)
 

  def atualizar():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum Produto cadastrado")
    else:  
      op = st.selectbox("Atualização de Produtos", produtos)
      nome = st.text_input("Informe o novo nome do Produto", op.get_nome())
      descricao = st.text_input("Informe o novo descricao do Produto", op.get_descricao())
      preco = st.text_input("Informe a nova preço do Produto", op.get_preco())
      if st.button("Atualizar"):
        try:
          id = op.get_id()
          View.produto_atualizar(id, nome, descricao, float(preco), False)
          st.success("Produto atualizado com sucesso")
          st.rerun()
        except ValueError as error:
          st.error(f"Erro: {error}")