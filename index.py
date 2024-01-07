from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.manterpedidoUI import ManterPedidoUI

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
    op = st.sidebar.selectbox("Menu", ["Manter pedido", "Manter clientes", "Manter produtos", "Editar perfil", "Buscar pedidos de usuário"])
    if op == "Manter pedido": ManterPedidoUI.main()
    if op == "Manter clientes": ManterClienteUI.main()
    if op == "Manter produtos": ManterProdutoUI.main()
    if op == "Editar perfil": EditarPerfilUI.main()
    if op == "Buscar pedidos de usuário": BuscarPedidoUsuarioUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", [ "Editar perfil", "Realizar um pedido", "Meus pedidos",])
    if op == "Editar perfil": EditarPerfilUI.main()
    if op == "Realizar um pedido": RealizarPedidoUI.main()
    if op == "Meus pedidos": VisualizarPedidosUI.main()

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



