import streamlit as st
from views import View
import pandas as pd

class BuscarPedidoUsuarioUI:

    def main():
        st.header("Buscar Pedido de Usuário")
        BuscarPedidoUsuarioUI.buscar_pedido_usuario()

    def buscar_pedido_usuario():
        clientes = View.cliente_listar()
        cliente = st.selectbox("Selecione o cliente", clientes)

        if st.button("Buscar Pedidos"):
            pedidos_encontrados = View.buscar_pedido_usuario(cliente)

            if not pedidos_encontrados:
                st.write("Nenhuma pedido encontrado para o cliente informado.")
            else:
                dic = [{"ID Pedido": pedido.get_id(), "Cliente": View.cliente_listar_id(pedido.get_id_cliente()).get_nome(), "Produto": View.produto_listar_id(pedido.get_id_filme()).get_nome()} for pedido in pedidos_encontrados]
                df = pd.DataFrame(dic)
                st.dataframe(df)