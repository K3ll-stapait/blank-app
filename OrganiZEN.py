import streamlit as st


def organizar_financas():
    st.title("💰 Organizador de Dívidas")

    renda = st.number_input("Informe sua renda líquida mensal (R$):", min_value=0.0, step=10.0)

    st.subheader("📌 Despesas Fixas")
    despesas_fixas = {}
    with st.form("form_despesas_fixas"):
        while True:
            nome = st.text_input("Nome da despesa fixa", key=f"fixa_{len(despesas_fixas)}")
            if nome:
                valor = st.number_input(f"Valor de {nome} (R$)", min_value=0.0, step=10.0, key=f"valor_{nome}")
                despesas_fixas[nome] = valor
            if st.form_submit_button("Adicionar despesa fixa"):
                st.rerun()
            break

    st.subheader("📌 Dívidas ou Despesas Variáveis")
    dividas_variaveis = {}
    with st.form("form_dividas_variaveis"):
        while True:
            nome = st.text_input("Nome da dívida ou despesa variável", key=f"var_{len(dividas_variaveis)}")
            if nome:
                valor = st.number_input(f"Valor de {nome} (R$)", min_value=0.0, step=10.0, key=f"val_{nome}")
                dividas_variaveis[nome] = valor
            if st.form_submit_button("Adicionar despesa variável"):
                st.rerun()
            break

    if st.button("📊 Calcular"):
        total_fixo = sum(despesas_fixas.values())
        total_variavel = sum(dividas_variaveis.values())
        total_comprometido = total_fixo + total_variavel
        sobra = renda - total_comprometido
        comprometimento = (total_comprometido / renda) * 100 if renda > 0 else 0

        st.markdown("## 📈 Resumo Financeiro")
        st.write(f"**Renda mensal:** R$ {renda:.2f}")
        st.write(f"**Despesas fixas:** R$ {total_fixo:.2f}")
        st.write(f"**Dívidas/variáveis:** R$ {total_variavel:.2f}")
        st.write(f"**Total comprometido:** R$ {total_comprometido:.2f}")
        st.write(f"**Sobra mensal:** R$ {sobra:.2f}")
        st.write(f"**% da renda comprometida:** {comprometimento:.1f}%")

        st.markdown("## 💡 Sugestão")
        if sobra < 0:
            st.warning("Suas despesas estão acima da sua renda. Priorize renegociar ou reduzir dívidas variáveis.")
        elif total_variavel > (renda * 0.3):
            st.info("Suas dívidas variáveis comprometem mais de 30% da renda. Considere renegociação ou parcelamento com menores juros.")
        else:
            st.success("Sua situação está relativamente controlada. Continue acompanhando seus gastos!")

# Executar o app
organizar_financas()
