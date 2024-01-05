import streamlit as st
import pandas as pd
from views import View

class ManterProdutoUI:
  def main():
    st.header("Gestão de Produtos")
    tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Excluir", "Listar", "Atualizar",])
    with tab1: ManterProdutoUI.inserir()
    with tab2: ManterProdutoUI.excluir()
    with tab3: ManterProdutoUI.listar()
    with tab4: ManterProdutoUI.atualizar()
    
  
  def inserir():
    nome = st.text_input("Informe o nome do produto")
    descricao = st.text_input("Informe a descrição do produto")
    preco = st.number_input("Informe o valor do produto (R$)")
    qtd = st.text_input("Quantas unidades desse produto existem?")
    if st.button("Inserir"):
      try:
        View.produto_inserir(nome, descricao, float(preco), int(qtd), False)
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

  def listar():
    produtos = View.produto_listar()
    if len(produtos) == 0:
      st.write("Nenhum Produto cadastrado")
    else:  
      dic = [{"ID produto": produto.get_id(), "nome": produto.get_nome(), "preco": produto.get_preco(), "Descrição" : produto.get_descricao(), "quantidade": produto.get_qtd()} for produto in produtos]
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
      qtd = st.text_input("Quantas unidades desse produto existem?", op.get_qtd())
      if st.button("Atualizar"):
        try:
          id = op.get_id()
          View.produto_atualizar(id, nome, descricao, float(preco),int(qtd), False)
          st.success("Produto atualizado com sucesso")
          st.rerun()
        except ValueError as error:
          st.error(f"Erro: {error}")
