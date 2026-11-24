# Análise de Faturamento Mensal
# Projeto demonstrativo desenvolvido com Python, Pandas e Matplotlib.
# Execução prevista no Google Colab.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from google.colab import files


def formatar_moeda(valor):
    """Formata um número no padrão brasileiro de moeda."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def extrair_faturamento(nome_arquivo):
    """Lê cada aba do Excel e procura a célula 'Total Bruto:'."""
    excel = pd.ExcelFile(nome_arquivo)
    resultados = []

    for mes in excel.sheet_names:
        df = pd.read_excel(nome_arquivo, sheet_name=mes, header=None)
        encontrou_total = False

        for _, linha in df.iterrows():
            valores = linha.tolist()

            for indice, valor in enumerate(valores):
                if (
                    isinstance(valor, str)
                    and valor.strip().lower() == "total bruto:"
                ):
                    if indice + 1 >= len(valores):
                        raise ValueError(
                            f"A aba '{mes}' contém 'Total Bruto:', "
                            "mas não há um valor na célula seguinte."
                        )

                    valor_bruto = pd.to_numeric(
                        valores[indice + 1], errors="coerce"
                    )

                    if pd.isna(valor_bruto):
                        raise ValueError(
                            f"Não foi possível converter o faturamento "
                            f"da aba '{mes}' para número."
                        )

                    resultados.append(
                        {
                            "Mês": mes,
                            "Faturamento bruto": float(valor_bruto),
                        }
                    )
                    encontrou_total = True
                    break

            if encontrou_total:
                break

    if not resultados:
        raise ValueError(
            "Nenhuma aba apresentou o texto 'Total Bruto:' "
            "seguido de um valor numérico."
        )

    return pd.DataFrame(resultados)


def criar_grafico(faturamento):
    """Gera um gráfico do faturamento por mês e do total geral."""
    total_geral = faturamento["Faturamento bruto"].sum()

    fig, (ax1, ax2) = plt.subplots(
        1,
        2,
        figsize=(13, 6),
        gridspec_kw={"width_ratios": [4, 1]},
    )

    barras = ax1.bar(
        faturamento["Mês"],
        faturamento["Faturamento bruto"],
    )

    ax1.set_title("Faturamento Bruto Mensal")
    ax1.set_xlabel("Mês")
    ax1.set_ylabel("Faturamento (R$)")
    ax1.tick_params(axis="x", rotation=30)

    ax1.bar_label(
        barras,
        labels=[
            formatar_moeda(valor)
            for valor in faturamento["Faturamento bruto"]
        ],
        padding=3,
        fontsize=8,
    )

    ax1.yaxis.set_major_formatter(
        FuncFormatter(
            lambda valor, _: "R$ "
            + f"{valor:,.0f}".replace(",", ".")
        )
    )

    barra_total = ax2.bar(["Total Bruto"], [total_geral], width=0.6)
    ax2.set_title("Total Geral")
    ax2.set_ylabel("Valor (R$)")

    ax2.bar_label(
        barra_total,
        labels=[formatar_moeda(total_geral)],
        padding=5,
        fontsize=10,
    )

    ax2.set_ylim(0, total_geral * 1.15 if total_geral > 0 else 1)
    plt.tight_layout()

    caminho_grafico = "grafico_faturamento.png"
    fig.savefig(caminho_grafico, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    return caminho_grafico, total_geral


def main():
    print("Envie uma planilha Excel (.xlsx) para analisar o faturamento.")
    arquivos = files.upload()

    if not arquivos:
        print("Nenhum arquivo foi enviado.")
        return

    nome_arquivo = next(iter(arquivos))

    try:
        faturamento = extrair_faturamento(nome_arquivo)
        print("\nFaturamento encontrado por aba:")
        display(faturamento)

        caminho_grafico, total_geral = criar_grafico(faturamento)
        print(f"\nFaturamento bruto total: {formatar_moeda(total_geral)}")

        files.download(caminho_grafico)

    except Exception as erro:
        print(f"Não foi possível concluir a análise: {erro}")


if __name__ == "__main__":
    main()
