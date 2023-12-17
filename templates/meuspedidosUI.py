import streamlit as st
import pandas as pd
from views import View

class VisualizarPedidosUI:
    def main():
        st.header("Buscar Meus Pedidos")
        VisualizarPedidosUI.listar_pedidos()

    def listar_pedidos():
        
        if st.button("Visualizar"):
            pedidos = View.meus_Pedidos(st.session_state["cliente_id"])
            
            if len(pedidos) == 0:
                st.write("Nenhuma Pedidos cadastrado")
            else:
                dic = [{"ID pedidos": pedido.get_id(), "Cliente": View.cliente_listar_id(pedido.get_id_cliente()).get_nome(), "produto": View.produto_listar_id(pedido.get_id_produto()).get_titulo()} for pedido in pedidos]
                df = pd.DataFrame(dic)
                st.dataframe(df)