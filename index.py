from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.manterpedidoUI import ManterPedidoUI
from templates.manteritemUI import ManterItemUI

from templates.loginUI import LoginUI
from templates.cadastroUI import CadastroUI
from templates.editarperfilUI import EditarPerfilUI

from templates.realizarpedidoUI import RealizarPedidoUI
from templates.meuspedidosUI import VisualizarPedidosUI
from templates.buscarusuarioUI import BuscarPedidoUsuarioUI

from views import View
import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": CadastroUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Pedido", "Manter Clientes", "Manter Produtos", "Manter Itens", "Editar Perfil", "Buscar Pedidos de Usuário"])
    if op == "Manter Pedido": ManterPedidoUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Produtos": ManterProdutoUI.main()
    if op == "Manter Itens": ManterItemUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Buscar Pedidos de Usuário": BuscarPedidoUsuarioUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", [ "Editar Perfil", "Realizar um Pedidos", "Meus Pedidos",])
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Realizar um Pedidos": RealizarPedidoUI.main()
    if op == "Meus Pedidos": VisualizarPedidosUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      clientes = View.cliente_listar()
      if st.session_state["cliente_nome"] == clientes[0].get_nome(): IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()



