'''
Author: wang w1838978548@126.com
Date: 2025-01-17 14:25:20
LastEditors: wang w1838978548@126.com
LastEditTime: 2025-01-17 14:28:44
FilePath: \Automation\peptide.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
import networkx as nx

# Define the polypeptide sequence and amino acid colors (Somatoliberin sequence)
sequence = ["H", "S", "D", "T", "F", "T", "S", "Y", "R", "K", "Q", "E", "H", "N", "S", "S", "G", "Y", "L"]  # Somatoliberin sequence
amino_acid_colors = {
    "A": "red", "R": "blue", "N": "green", "D": "orange", "C": "purple",
    "E": "pink", "Q": "brown", "G": "cyan", "H": "magenta",
    "I": "yellow", "L": "teal", "K": "lime", "M": "grey", "F": "darkblue",
    "S": "gold", "T": "olive", "Y": "peru"
}

# Create a graph to represent the polypeptide
G = nx.Graph()
for i in range(len(sequence)):
    G.add_node(i, amino_acid=sequence[i], color=amino_acid_colors[sequence[i]])
    if i > 0:
        G.add_edge(i - 1, i)

# Extract node colors for plotting
node_colors = [data["color"] for _, data in G.nodes(data=True)]

# Draw the graph
plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G, k=0.15)  # Further shorten the edge length
nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=800, edge_color="black")
labels = {i: sequence[i] for i in range(len(sequence))}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color="white")

plt.title("Polypeptide Visualization (Somatoliberin)")
plt.show()
