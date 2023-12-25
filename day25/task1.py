# Credit: HyperNeutrino

import networkx as nx


component_graph = nx.Graph()

input_file = open("input.txt", "r")

for line in input_file:
    component, children_string = line.strip().split(": ")
    for child in children_string.split():
        component_graph.add_edge(component, child)

input_file.close()

component_graph.remove_edges_from(nx.minimum_edge_cut(component_graph))

comp1, comp2 = nx.connected_components(component_graph)

print(len(comp1) * len(comp2))
