import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

from dash import Dash, html

# ===============================
# Leitura do arquivo
# ===============================
df = pd.read_csv("ecommerce_estatistica.csv")

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# ===============================
# Função para converter gráfico em imagem
# ===============================
def fig_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()
    plt.close()
    return f"data:image/png;base64,{image_base64}"

# ===============================
# 1. Histograma
# ===============================
plt.figure()
sns.histplot(df["Nota"], bins=10, kde=True)
plt.title("Distribuição das Notas dos Produtos")
plt.xlabel("Nota")
plt.ylabel("Frequência")
histograma = fig_to_base64()

# ===============================
# 2. Dispersão
# ===============================
plt.figure()
sns.scatterplot(data=df, x="Preço", y="Qtd_Vendidos_Cod")
plt.title("Preço vs Quantidade Vendida")
plt.xlabel("Preço")
plt.ylabel("Quantidade Vendida")
dispersao = fig_to_base64()

# ===============================
# 3. Mapa de Calor
# ===============================
plt.figure()
correlacao = df.select_dtypes(include="number").corr()
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor - Correlação")
heatmap = fig_to_base64()

# ===============================
# 4. Gráfico de Barra
# ===============================
plt.figure()
sns.barplot(data=df, x="Gênero", y="Preço", estimator="mean")
plt.title("Preço Médio por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Preço Médio")
plt.xticks(rotation=45)
barra = fig_to_base64()

# ===============================
# 5. Gráfico de Pizza
# ===============================
plt.figure()
df["Temporada"].value_counts().plot.pie(
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição por Temporada")
plt.ylabel("")
pizza = fig_to_base64()

# ===============================
# 6. Densidade
# ===============================
plt.figure()
sns.kdeplot(df["Preço"], fill=True)
plt.title("Densidade dos Preços")
plt.xlabel("Preço")
plt.ylabel("Densidade")
densidade = fig_to_base64()

# ===============================
# 7. Regressão
# ===============================
plt.figure()
sns.regplot(data=df, x="Desconto", y="Preço")
plt.title("Regressão: Desconto vs Preço")
plt.xlabel("Desconto")
plt.ylabel("Preço")
regressao = fig_to_base64()

# ===============================
# Aplicação Dash
# ===============================
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Estatísticas E-commerce", style={"textAlign": "center"}),

    html.H2("Histograma"),
    html.Img(src=histograma),

    html.H2("Gráfico de Dispersão"),
    html.Img(src=dispersao),

    html.H2("Mapa de Calor"),
    html.Img(src=heatmap),

    html.H2("Gráfico de Barra"),
    html.Img(src=barra),

    html.H2("Gráfico de Pizza"),
    html.Img(src=pizza),

    html.H2("Gráfico de Densidade"),
    html.Img(src=densidade),

    html.H2("Gráfico de Regressão"),
    html.Img(src=regressao),
])

# ===============================
# Execução
# ===============================
if __name__ == "__main__":
    app.run_server(debug=True)
