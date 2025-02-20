import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# Set random seed for reproducibility
np.random.seed(42)

# Define the amino acids and their colors
amino_acids = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M"]
colors = plt.cm.jet(np.linspace(0, 1, len(amino_acids)))

# Create figure and axes
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133, projection='3d')

# Left: Amino acids as circles
for i, (aa, color) in enumerate(zip(amino_acids, colors)):
    ax1.scatter(0, i, color=color, s=300, edgecolor="black")
    ax1.text(0.5, i, aa, fontsize=10, verticalalignment='center')
ax1.set_xlim(-1, 2)
ax1.set_ylim(-1, len(amino_acids))
ax1.axis('off')
ax1.set_title("Amino Acids", y=-0.2)

# Middle: Polypeptide structure
G = nx.Graph()
for i in range(len(amino_acids)):
    G.add_node(i, color=colors[i])
    if i > 0:
        G.add_edge(i - 1, i)
node_colors = [G.nodes[n]["color"] for n in G.nodes()]
pos = nx.spring_layout(G, k=0.2, seed=42)
nx.draw(G, pos, ax=ax2, node_color=node_colors, node_size=300, edge_color="black", width=1)
ax2.set_title("Polypeptide", y=-0.2)

# Right: Protein structure
x = np.cumsum(np.random.uniform(-1, 1, len(amino_acids) * 3))
y = np.cumsum(np.random.uniform(-1, 1, len(amino_acids) * 3))
z = np.cumsum(np.random.uniform(-1, 1, len(amino_acids) * 3))
ax3.scatter(x, y, z, color=np.tile(colors, (3, 1)), s=300, edgecolor="black")
ax3.plot(x, y, z, color="black", linewidth=1)
ax3.set_box_aspect([1, 1, 1])  # Adjust aspect ratio
ax3.set_title("Protein Structure (Complex)", y=-0.2)
ax3.axis('off')

# Show the plot
plt.tight_layout()
plt.show()
