import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo no dirigido
G = nx.Graph()

# Añadir vértices
vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'I', 'G', 'X']
G.add_nodes_from(vertices)

# Añadir aristas (no dirigidas)
aristas = [
    ('S', 'A'), ('S', 'B'), ('C', 'S'), ('S', 'D'),
    ('A', 'G'), ('A', 'B'), ('C', 'B'), ('C', 'I'),
    ('F', 'C'), ('D', 'C'), ('D', 'E'), ('E', 'X'),
    ('F', 'I'), ('D', 'F')
]
G.add_edges_from(aristas)

# ------------------- DIBUJAR EL GRAFO -------------------
pos = nx.spring_layout(G, seed=42)  # Para que siempre se vea igual y bonito

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=2000, font_size=16, font_weight='bold',
        edge_color='gray', width=2)

# Resaltar S (inicio) y X (final)
nx.draw_networkx_nodes(G, pos, nodelist=['S'], node_color='lightgreen', node_size=2500)
nx.draw_networkx_nodes(G, pos, nodelist=['X'], node_color='salmon', node_size=2500)

plt.title("Grafo G = (V, E)\nInicio: S (verde) | Final: X (rojo)", fontsize=18)
plt.axis('off')
plt.tight_layout()
plt.show()

# ------------------- ENCONTRAR CAMINOS DE S A X -------------------
def encontrar_todos_caminos(grafo, inicio, fin, camino_actual=[]):
    camino_actual = camino_actual + [inicio]
    if inicio == fin:
        return [camino_actual]
    if inicio not in grafo:
        return []
    
    caminos = []
    for vecino in grafo[inicio]:
        if vecino not in camino_actual:  # Evitar ciclos
            nuevos_caminos = encontrar_todos_caminos(grafo, vecino, fin, camino_actual)
            for nuevo in nuevos_caminos:
                caminos.append(nuevo)
    return caminos

# Convertir a diccionario de adyacencia para la búsqueda
adyacencia = {nodo: list(G.neighbors(nodo)) for nodo in G.nodes()}

todos_los_caminos = encontrar_todos_caminos(adyacencia, 'S', 'X')

print(f"\nSe encontraron {len(todos_los_caminos)} caminos desde S hasta X:\n")
print("="*70)

for i, camino in enumerate(todos_los_caminos, 1):
    print(f"Camino {i}: {' → '.join(camino)}")
    print("Detalles de movimientos:")
    for j in range(len(camino) - 1):
        actual = camino[j]
        siguiente = camino[j+1]
        print(f"   Salida de {actual} → {siguiente} (arista {{ {actual},{siguiente} }})")
    print("-" * 50)