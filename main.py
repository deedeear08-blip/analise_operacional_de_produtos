import matplotlib.pyplot as plt
import numpy as np


produtos = ["Arroz", "Óleo", "Feijão", "Açúcar", "Leite"]

stock = [500, 1000, 300, 900, 200]

vendas = [450, 100, 280, 150, 190]

clientes = [300, 80, 250, 120, 180]

x = np.arange(len(produtos))
plt.bar(x - 0.25, stock, width=0.25, label="Stocks" )
plt.bar(x , vendas, width=0.25, label="Vendas")
plt.bar(x + 0.25, clientes, width=0.25, label="Clientes")



plt.xticks(x, produtos,rotation=30)
plt.title("Análise de produto:Stocks vs Vendas vs Clientes",fontsize=10)
plt.xlabel(" Produtos")
plt.ylabel("Quantidade")

plt.legend()
plt.grid(axis="y")
plt.show()
