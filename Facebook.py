# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:19:51 2018

@author: Mihir
"""

import networkx as nx
import matplotlib.pyplot as plt

fb_graph = nx.Graph(name='facebook')

# -----------------------------------------------------------------------------------------------------
# ADDING NODES

fb_graph.add_node('Manoj', sec='A', gen='M')
fb_graph.add_node('Johanna', sec='A', gen='F')
fb_graph.add_node('Ramya', sec='A', gen='F')
fb_graph.add_node('Shalini', sec='A', gen='F')
fb_graph.add_node('Balasubramaniyan', sec='A', gen='M')
fb_graph.add_node('Pooja', sec='A', gen='F')
fb_graph.add_node('Harish', sec='A', gen='M')
fb_graph.add_node('Sumeet', sec='A', gen='M')
fb_graph.add_node('Abdul', sec='A', gen='M')
fb_graph.add_node('Abhishek', sec='A', gen='M')
fb_graph.add_node('Akhil', sec='A', gen='M')
fb_graph.add_node('Ajith', sec='A', gen='M')
fb_graph.add_node('Akash', sec='A', gen='M')
fb_graph.add_node('Amit', sec='A', gen='M')
# fb_graph.add_node('Amritha',sec='A',gen='F')
# fb_graph.add_node('Nupur',sec='A',gen='F')
fb_graph.add_node('Arun', sec='A', gen='M')
fb_graph.add_node('Beenu', sec='A', gen='F')
fb_graph.add_node('Sarthak', sec='A', gen='M')
fb_graph.add_node('Bishal', sec='A', gen='M')
fb_graph.add_node('Bhavya', sec='A', gen='F')
fb_graph.add_node('Toshi', sec='A', gen='F')
fb_graph.add_node('Darshan', sec='A', gen='M')
fb_graph.add_node('Sravya', sec='A', gen='F')
fb_graph.add_node('Vedant', sec='A', gen='M')
fb_graph.add_node('Pruthvi', sec='A', gen='F')
# fb_graph.add_node('Nidhi',sec='A',gen='F')
# fb_graph.add_node('Devadithya',sec='B',gen='M')
fb_graph.add_node('Ashim', sec='B', gen='M')
fb_graph.add_node('Bimal', sec='B', gen='M')
# fb_graph.add_node('Ashish',sec='B',gen='M')
# fb_graph.add_node('Nissi',sec='B',gen='F')
fb_graph.add_node('Mihir', sec='B', gen='M')
fb_graph.add_node('Prashant', sec='B', gen='M')
fb_graph.add_node('Prathiksha', sec='B', gen='F')
# fb_graph.add_node('Raja',sec='B',gen='M')
fb_graph.add_node('Rakshith', sec='B', gen='M')
fb_graph.add_node('Harshita', sec='B', gen='F')
# fb_graph.add_node('Sanjana',sec='B',gen='F')
fb_graph.add_node('Apeksha', sec='C', gen='F')
fb_graph.add_node('Vignesh', sec='C', gen='M')
fb_graph.add_node('Gaurav', sec='C', gen='M')
fb_graph.add_node('Akansha', sec='C', gen='F')
fb_graph.add_node('Santosh', sec='C', gen='M')
fb_graph.add_node('Nitish', sec='C', gen='M')
fb_graph.add_node('Badri', sec='C', gen='M')
fb_graph.add_node('Tejaswini', sec='C', gen='F')
fb_graph.add_node('Purvaj', sec='C', gen='M')
fb_graph.add_node('Rahul', sec='C', gen='M')
fb_graph.add_node('Sam', sec='C', gen='M')
fb_graph.add_node('Vishwajeet', sec='C', gen='M')
fb_graph.add_node('Aroon', sec='C', gen='M')
# fb_graph.add_node('Shimna',sec='C',gen='F')
fb_graph.add_node('Shreyas', sec='C', gen='M')
fb_graph.add_node('Joshua', sec='C', gen='M')
fb_graph.add_node('Soundarya', sec='C', gen='F')
fb_graph.add_node('Vedika', sec='C', gen='F')
fb_graph.add_node('Aishwarya', sec='C', gen='F')
fb_graph.add_node('Atharv', sec='All', gen='M')

# --------------------------------------------------------------------
fb_edge_list = [('Manoj', 'Ramya'), ('Manoj', 'Shalini'), ('Manoj', 'Sumeet'), ('Manoj', 'Bishal'),
                ('Manoj', 'Darshan'), ('Manoj', 'Vedant'), ('Manoj', 'Gaurav'),
                ('Johanna', 'Ramya'), ('Johanna', 'Beenu'),
                ('Ramya', 'Johanna'), ('Ramya', 'Shalini'), ('Ramya', 'Balasubramaniyan'), ('Ramya', 'Sumeet'),
                ('Ramya', 'Beenu'), ('Ramya', 'Bhavya'), ('Ramya', 'Toshi'), ('Ramya', 'Darshan'), ('Ramya', 'Atharv'),
                ('Shalini', 'Manoj'), ('Shalini', 'Johanna'), ('Shalini', 'Ramya'), ('Shalini', 'Pooja'),
                ('Shalini', 'Toshi'),
                ('Pooja', 'Manoj'), ('Pooja', 'Johanna'), ('Pooja', 'Ramya'), ('Pooja', 'Shalini'),
                ('Harish', 'Sumeet'), ('Harish', 'Abdul'), ('Harish', 'Akhil'), ('Harish', 'Ajith'),
                ('Harish', 'Akash'), ('Harish', 'Toshi'), ('Harish', 'Sravya'), ('Harish', 'Vedant'),
                ('Harish', 'Pruthvi'),
                ('Sumeet', 'Manoj'), ('Sumeet', 'Johanna'), ('Sumeet', 'Balasubramaniyan'),
                ('Sumeet', 'Harish'), ('Sumeet', 'Abdul'), ('Sumeet', 'Abhishek'), ('Sumeet', 'Akhil'),
                ('Sumeet', 'Ajith'), ('Sumeet', 'Akash'), ('Sumeet', 'Amit'), ('Sumeet', 'Arun'),
                ('Sumeet', 'Beenu'), ('Sumeet', 'Sarthak'), ('Sumeet', 'Bishal'), ('Sumeet', 'Bhavya'),
                ('Sumeet', 'Toshi'), ('Sumeet', 'Darshan'), ('Sumeet', 'Sravya'), ('Sumeet', 'Vedant'),
                ('Sumeet', 'Pruthvi'), ('Sumeet', 'Prathiksha'), ('Sumeet', 'Rakshith'), ('Sumeet', 'Harshita'),
                ('Sumeet', 'Badri'), ('Sumeet', 'Rahul'), ('Sumeet', 'Sam'), ('Sumeet', 'Shreyas'),
                ('Sumeet', 'Atharv'),
                ('Abdul', 'Shalini'), ('Abdul', 'Balasubramaniyan'), ('Abdul', 'Pooja'), ('Abdul', 'Harish'),
                ('Abdul', 'Sumeet'), ('Abdul', 'Abhishek'), ('Abdul', 'Akhil'), ('Abdul', 'Akash'),
                ('Abdul', 'Amit'), ('Abdul', 'Arun'), ('Abdul', 'Sravya'), ('Abdul', 'Vedant'),
                ('Abhishek', 'Balasubramaniyan'), ('Abhishek', 'Harish'), ('Abhishek', 'Sumeet'),
                ('Abhishek', 'Ajith'), ('Abhishek', 'Akash'), ('Abhishek', 'Amit'), ('Abhishek', 'Sarthak'),
                ('Abhishek', 'Bishal'), ('Abhishek', 'Vedant'),
                ('Akhil', 'Harish'), ('Akhil', 'Sumeet'), ('Akhil', 'Ajith'), ('Akhil', 'Toshi'),
                ('Akhil', 'Darshan'), ('Akhil', 'Vedant'), ('Akhil', 'Pruthvi'), ('Akhil', 'Prathiksha'),
                ('Akhil', 'Harshita'), ('Akhil', 'Nitish'), ('Akhil', 'Sam'),
                ('Ajith', 'Sumeet'), ('Ajith', 'Akhil'), ('Ajith', 'Arun'), ('Ajith', 'Sarthak'),
                ('Ajith', 'Toshi'), ('Ajith', 'Darshan'), ('Ajith', 'Vedant'), ('Ajith', 'Pruthvi'),
                ('Amit', 'Sumeet'), ('Amit', 'Abdul'), ('Amit', 'Bishal'), ('Amit', 'Bhavya'), ('Amit', 'Sravya'),
                ('Amit', 'Bimal'),
                ('Arun', 'Balasubramaniyan'), ('Arun', 'Harish'), ('Arun', 'Abdul'), ('Arun', 'Sumeet'),
                ('Arun', 'Sarthak'), ('Arun', 'Bishal'), ('Arun', 'Bhavya'), ('Arun', 'Darshan'), ('Arun', 'Vedant'),
                ('Arun', 'Sam'), ('Arun', 'Aroon'),
                ('Beenu', 'Johanna'), ('Beenu', 'Ramya'), ('Beenu', 'Harish'), ('Beenu', 'Sumeet'),
                ('Beenu', 'Akhil'), ('Beenu', 'Sarthak'), ('Beenu', 'Bhavya'), ('Beenu', 'Toshi'),
                ('Beenu', 'Sravya'), ('Beenu', 'Vedant'), ('Beenu', 'Atharv'),
                ('Sarthak', 'Manoj'), ('Sarthak', 'Johanna'), ('Sarthak', 'Ramya'), ('Sarthak', 'Balasubramaniyan'),
                ('Sarthak', 'Harish'), ('Sarthak', 'Sumeet'), ('Sarthak', 'Abdul'), ('Sarthak', 'Abhishek'),
                ('Sarthak', 'Akhil'), ('Sarthak', 'Ajith'), ('Sarthak', 'Akash'), ('Sarthak', 'Arun'),
                ('Sarthak', 'Bishal'), ('Sarthak', 'Bhavya'), ('Sarthak', 'Toshi'), ('Sarthak', 'Darshan'),
                ('Sarthak', 'Sravya'), ('Sarthak', 'Vedant'), ('Sarthak', 'Pruthvi'), ('Sarthak', 'Vignesh'),
                ('Sarthak', 'Gaurav'), ('Sarthak', 'Nitish'), ('Sarthak', 'Purvaj'), ('Sarthak', 'Rahul'),
                ('Sarthak', 'Sam'), ('Sarthak', 'Vishwajeet'), ('Sarthak', 'Aroon'), ('Sarthak', 'Shreyas'),
                ('Bishal', 'Manoj'), ('Bishal', 'Harish'), ('Bishal', 'Sumeet'), ('Bishal', 'Abdul'),
                ('Bishal', 'Abhishek'), ('Bishal', 'Akhil'), ('Bishal', 'Akash'), ('Bishal', 'Amit'),
                ('Bishal', 'Beenu'), ('Bishal', 'Sarthak'), ('Bishal', 'Darshan'), ('Bishal', 'Vedant'),
                ('Bishal', 'Ashim'), ('Bishal', 'Bimal'),
                ('Bhavya', 'Ramya'), ('Bhavya', 'Pooja'), ('Bhavya', 'Harish'), ('Bhavya', 'Akash'),
                ('Bhavya', 'Darshan'), ('Bhavya', 'Sravya'), ('Bhavya', 'Pruthvi'),
                ('Toshi', 'Ramya'), ('Toshi', 'Harish'), ('Toshi', 'Sumeet'), ('Toshi', 'Abhishek'),
                ('Toshi', 'Akhil'), ('Toshi', 'Beenu'), ('Toshi', 'Bhavya'), ('Toshi', 'Sravya'),
                ('Toshi', 'Vedant'), ('Toshi', 'Pruthvi'), ('Toshi', 'Prathiksha'), ('Toshi', 'Sam'),
                ('Darshan', 'Balasubramaniyan'), ('Darshan', 'Sumeet'), ('Darshan', 'Akhil'), ('Darshan', 'Ajith'),
                ('Darshan', 'Arun'), ('Darshan', 'Sarthak'), ('Darshan', 'Bishal'), ('Darshan', 'Vedant'),
                ('Sravya', 'Ramya'), ('Sravya', 'Harish'), ('Sravya', 'Amit'), ('Sravya', 'Beenu'),
                ('Sravya', 'Bhavya'), ('Sravya', 'Toshi'), ('Sravya', 'Vedant'), ('Sravya', 'Pruthvi'),
                ('Sravya', 'Tejaswini'),
                ('Vedant', 'Manoj'), ('Vedant', 'Balasubramaniyan'), ('Vedant', 'Harish'), ('Vedant', 'Sumeet'),
                ('Vedant', 'Abdul'), ('Vedant', 'Abhishek'), ('Vedant', 'Akhil'), ('Vedant', 'Ajith'), ('Vedant', 'Akash'),
                ('Vedant', 'Arun'), ('Vedant', 'Beenu'), ('Vedant', 'Bishal'), ('Vedant', 'Toshi'), ('Vedant', 'Pruthvi'),
                ('Vedant', 'Prathiksha'), ('Vedant', 'Badri'), ('Vedant', 'Purvaj'), ('Vedant', 'Rahul'),
                ('Vedant', 'Sam'), ('Vedant', 'Shreyas'), ('Vedant', 'Vedika'), ('Vedant', 'Atharv'),
                ('Pruthvi', 'Harish'), ('Pruthvi', 'Sumeet'), ('Pruthvi', 'Akhil'), ('Pruthvi', 'Ajith'),
                ('Pruthvi', 'Beenu'), ('Pruthvi', 'Sarthak'), ('Pruthvi', 'Toshi'), ('Pruthvi', 'Sravya'),
                ('Pruthvi', 'Vedant'), ('Pruthvi', 'Prathiksha'), ('Pruthvi', 'Rahul'),
                ('Ashim', 'Bimal'), ('Ashim', 'Prashant'),
                ('Bimal', 'Sumeet'), ('Bimal', 'Ashim'), ('Bimal', 'Prashant'), ('Bimal', 'Rakshith'),
                ('Mihir', 'Prashant'), ('Mihir', 'Rakshith'), ('Mihir', 'Harshita'), ('Mihir', 'Vishwajeet'),
                ('Prashant', 'Sumeet'), ('Prashant', 'Ashim'), ('Prashant', 'Bimal'), ('Prashant', 'Mihir'),
                ('Prashant', 'Prathiksha'), ('Prashant', 'Rakshith'), ('Prashant', 'Harshita'), ('Prashant', 'Sam'),
                ('Prashant', 'Vedika'),
                ('Prathiksha', 'Sumeet'), ('Prathiksha', 'Abhishek'), ('Prathiksha', 'Toshi'),
                ('Prathiksha', 'Vedant'), ('Prathiksha', 'Pruthvi'), ('Prathiksha', 'Prashant'),
                ('Prathiksha', 'Rakshith'), ('Prathiksha', 'Harshita'), ('Prathiksha', 'Gaurav'), ('Prathiksha', 'Atharv'),
                ('Rakshith', 'Manoj'), ('Rakshith', 'Sumeet'), ('Rakshith', 'Mihir'), ('Rakshith', 'Prashant'),
                ('Rakshith', 'Prathiksha'),
                ('Harshita', 'Sumeet'), ('Harshita', 'Akhil'), ('Harshita', 'Pruthvi'), ('Harshita', 'Mihir'),
                ('Harshita', 'Prashant'), ('Harshita', 'Prathiksha'), ('Harshita', 'Rakshith'),
                ('Apeksha', 'Johanna'), ('Apeksha', 'Balasubramaniyan'), ('Apeksha', 'Vignesh'), ('Apeksha', 'Gaurav'),
                ('Apeksha', 'Akansha'), ('Apeksha', 'Tejaswini'), ('Apeksha', 'Rahul'), ('Apeksha', 'Sam'),
                ('Apeksha', 'Vishwajeet'), ('Apeksha', 'Aroon'),
                ('Santosh', 'Vignesh'), ('Santosh', 'Gaurav'), ('Santosh', 'Nitish'), ('Santosh', 'Purvaj'),
                ('Santosh', 'Sam'), ('Santosh', 'Aroon'), ('Santosh', 'Joshua'),
                ('Nitish', 'Vignesh'), ('Nitish', 'Gaurav'), ('Nitish', 'Santosh'), ('Nitish', 'Vedika'),
                ('Nitish', 'Atharv'),
                ('Tejaswini', 'Apeksha'),
                ('Rahul', 'Sarthak'), ('Rahul', 'Vedant'), ('Rahul', 'Pruthvi'), ('Rahul', 'Vignesh'),
                ('Rahul', 'Gaurav'), ('Rahul', 'Badri'), ('Rahul', 'Purvaj'), ('Rahul', 'Sam'), ('Rahul', 'Shreyas'),
                ('Aishwarya', 'Arun'), ('Aishwarya', 'Apeksha'), ('Aishwarya', 'Gaurav'), ('Aishwarya', 'Purvaj'),
                ('Aishwarya', 'Rahul'), ('Aishwarya', 'Sam'), ('Aishwarya', 'Vishwajeet'), ('Aishwarya', 'Aroon'),
                ('Aishwarya', 'Soundarya'), ('Aishwarya', 'Vedika'), ('Aishwarya', 'Atharv'),
                ('Sam', 'Balasubramaniyan'), ('Sam', 'Sumeet'), ('Sam', 'Arun'), ('Sam', 'Toshi'),
                ('Sam', 'Vedant'), ('Sam', 'Prashant'), ('Sam', 'Apeksha'), ('Sam', 'Vignesh'),
                ('Sam', 'Gaurav'), ('Sam', 'Akansha'), ('Sam', 'Santosh'), ('Sam', 'Nitish'),
                ('Sam', 'Badri'), ('Sam', 'Purvaj'), ('Sam', 'Rahul'), ('Sam', 'Vishwajeet'), ('Sam', 'Aroon'),
                ('Sam', 'Shreyas'), ('Sam', 'Joshua'), ('Sam', 'Soundarya'), ('Sam', 'Vedika'),
                ('Sam', 'Aishwarya'),
                ('Vishwajeet', 'Toshi'), ('Vishwajeet', 'Darshan'), ('Vishwajeet', 'Mihir'), ('Vishwajeet', 'Apeksha'),
                ('Vishwajeet', 'Vignesh'), ('Vishwajeet', 'Gaurav'), ('Vishwajeet', 'Santosh'), ('Vishwajeet', 'Nitish'),
                ('Vishwajeet', 'Badri'), ('Vishwajeet', 'Purvaj'), ('Vishwajeet', 'Rahul'), ('Vishwajeet', 'Aroon'),
                ('Vishwajeet', 'Shreyas'), ('Vishwajeet', 'Joshua'), ('Vishwajeet', 'Soundarya'), ('Vishwajeet', 'Vedika'),
                ('Vishwajeet', 'Aishwarya'), ('Vishwajeet', 'Sam'),
                ('Vedika', 'Amit'), ('Vedika', 'Bishal'), ('Vedika', 'Sravya'), ('Vedika', 'Vedant'), ('Vedika', 'Pruthvi'),
                ('Vedika', 'Bimal'), ('Vedika', 'Prashant'), ('Vedika', 'Prathiksha'), ('Vedika', 'Apeksha'),
                ('Vedika', 'Vignesh'), ('Vedika', 'Gaurav'), ('Vedika', 'Nitish'), ('Vedika', 'Tejaswini'),
                ('Vedika', 'Purvaj'), ('Vedika', 'Rahul'), ('Vedika', 'Vishwajeet'), ('Vedika', 'Aroon'), ('Vedika', 'Joshua'),
                ('Vedika', 'Soundarya'), ('Vedika', 'Aishwarya'),
                ('Soundarya', 'Purvaj'), ('Soundarya', 'Sam'), ('Soundarya', 'Vishwajeet'), ('Soundarya', 'Joshua'),
                ('Soundarya', 'Atharv')]
# ---------------------------------------------------------------------------------------
fb_graph.add_edges_from(fb_edge_list)
# ---------------------------------------------------------------
nodesizelist = [75 * fb_graph.degree(node) for node in fb_graph]
nodecolorlist = []
nodecolorlist2 = [fb_graph.degree(student) for student in fb_graph]
for person in fb_graph:
    if fb_graph.nodes[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif fb_graph.nodes[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif fb_graph.nodes[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

# pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20, 12.6))
nx.draw_networkx(fb_graph, pos, node_color=nodecolorlist, node_size=nodesizelist, edge_color='0.7')
plt.savefig('fb_graph0.4_spring.pdf', format='pdf')
# nx.draw_networkx(fb_graph,pos,node_color = nodecolorlist2, node_size = nodesizelist,cmap = plt.cm.Reds)

pos = nx.circular_layout(fb_graph)
plt.figure(figsize=(20, 20))
nx.draw_networkx(fb_graph, pos, node_color=nodecolorlist, node_size=nodesizelist, edge_color='0.7')
# plt.savefig('fb_graph0.4_circular.pdf',format='pdf')
# ----------------------------------------------------------

# for male-female bipartite:
# for male-female bipartite:
# for male-female bipartite:
from networkx.algorithms import bipartite

B = nx.Graph()
nodecolorlistb = []
for (u, v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] == 'M' and fb_graph.nodes[u]['gen'] != fb_graph.nodes[v]['gen']:
        B.add_node(u, gen='M')

for (u, v) in fb_edge_list:
    if fb_graph.nodes[v]['gen'] == 'M' and fb_graph.nodes[u]['gen'] != fb_graph.nodes[v]['gen']:
        B.add_node(v, gen='M')

for (u, v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[u]['gen'] != fb_graph.nodes[v]['gen']:
        B.add_node(u, gen='F')

for (u, v) in fb_edge_list:
    if fb_graph.nodes[v]['gen'] == 'F' and fb_graph.nodes[u]['gen'] != fb_graph.nodes[v]['gen']:
        B.add_node(v, gen='F')

for (u, v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] != fb_graph.nodes[v]['gen']:
        B.add_edge(u, v)
for person in B:
    if fb_graph.nodes[person]['gen'] == 'M':
        nodecolorlistb.append('#6495ED')
    else:
        nodecolorlistb.append('#F3CD05')
nodesizelistbip = [100 * B.degree(node) for node in B]
plt.figure(figsize=(11, 11))
pos = nx.circular_layout(B)
nx.draw_networkx(B, pos, node_color=nodecolorlistb, edge_color='0.4', node_size=nodesizelistbip)
plt.savefig('fbbipcirc.pdf', format='pdf')

X, Y = bipartite.sets(B)
pos = dict()
pos.update((n, (1, i)) for i, n in enumerate(X))  # put nodes from X at x=1
pos.update((n, (2, i)) for i, n in enumerate(Y))  # put nodes from Y at x=2
plt.figure(figsize=(15, 25))
plt.title('Bipartite Boys-Girls Graph')
nx.draw_networkx(B, pos=pos, node_color=nodecolorlistb, edge_color='0.4', node_size=nodesizelistbip)
plt.savefig('fbbipst.pdf', format='pdf')

nx.degree(B)
# ---------------------------------------------------------------------------
# Projected Graph for BOYS (common female friends)

x = set([node for node in B if B.nodes[node]['gen'] == 'M'])
# y = set([node for node in B if B.nodes[node]['gen'] == 'F']) - if you want to ddo it for girls - common male friends

Pboys = bipartite.weighted_projected_graph(B, x)
edge_width = [1 * Pboys[u][v]['weight'] for u, v in Pboys.edges()]
labels_greater_than_5 = {edge: weight for edge, weight in nx.get_edge_attributes(Pboys, 'weight').items() if weight > 5}
plt.figure(figsize=(8, 8))
plt.title('Common Female Friends')
pos = nx.circular_layout(Pboys)
nx.draw_networkx(Pboys, pos, edge_color='0.4', width=edge_width, node_color='#6495ED', node_size=400)
nx.draw_networkx_edge_labels(Pboys, pos, edge_labels=labels_greater_than_5)
plt.savefig('fbcommonfemfrds.pdf', format='pdf')

edgelist_grt_than_5 = [x for x in Pboys.edges(data=True) if x[2]['weight'] > 5]
edge_width = [x[2]['weight'] for x in Pboys.edges(data=True)]
edge_widthblue = [x[2]['weight'] for x in Pboys.edges(data=True) if x[2]['weight'] > 5]
plt.figure(figsize=(9, 9))
plt.title('Common Female Friends - >5')
nx.draw_networkx(Pboys, pos, edge_color='0.7', width=edge_width, node_color='#6495ED', node_size=400)
nx.draw_networkx_edges(Pboys, pos, edgelist=edgelist_grt_than_5, edge_color='blue', width=edge_widthblue)
nx.draw_networkx_edge_labels(Pboys, pos, edge_labels=labels_greater_than_5)
plt.savefig('fbcommonfemfrdsg5.pdf', format='pdf')

# Make it better by adding weights to the edges, and changing edge size accordingly. - use weighted_projected_graph(B,x) and print P.edges(data = True)
# ------------------------------------------------------------------------------------------
# Projected Graph for GIRLS (common male friends)
y = set([node for node in B if B.nodes[node]['gen'] == 'F'])

Pgirls = bipartite.weighted_projected_graph(B, y)
edge_width = [1 * Pgirls[u][v]['weight'] for u, v in Pgirls.edges()]
labels_greater_than_5 = {edge: weight for edge, weight in nx.get_edge_attributes(Pgirls, 'weight').items() if
                         weight > 5}
plt.figure(figsize=(9, 9))
plt.title('Common Male Friends')
pos = nx.circular_layout(Pgirls)
nx.draw_networkx(Pgirls, pos, edge_color='0.4', width=edge_width, node_color='#D2691E', node_size=300)
nx.draw_networkx_edge_labels(Pgirls, pos, edge_labels=labels_greater_than_5)
plt.savefig('fbcommonmalfrds.pdf', format='pdf')

edgelist_grt_than_5 = [x for x in Pgirls.edges(data=True) if x[2]['weight'] > 5]

plt.figure(figsize=(9, 9))
plt.title('Common Male Friends - >5')
edge_width = [x[2]['weight'] for x in Pgirls.edges(data=True)]
edge_widthyellow = [x[2]['weight'] for x in Pgirls.edges(data=True) if x[2]['weight'] > 5]
pos = nx.circular_layout(Pgirls)
nx.draw_networkx(Pgirls, pos, edge_color='0.7', width=edge_width, node_color='#D2691E', node_size=300)
nx.draw_networkx_edges(Pgirls, pos, edgelist=edgelist_grt_than_5, edge_color='#FFA500', width=edge_widthyellow)
nx.draw_networkx_edge_labels(Pgirls, pos, edge_labels=labels_greater_than_5)
plt.savefig('fbcommonmalfrdsg5.pdf', format='pdf')
# -------------------------------------------------------------------------------------------
# fb_graph coloured according to gender
'''nodesizelist = [100*fb_graph.degree(node) for node in fb_graph]
nodecolorlistg = []
#nodecolorlist2 = [fb_graph.degree(student) for student in fb_graph]

for person in fb_graph:
    if fb_graph.nodes[person]['gen'] == 'M':
        nodecolorlistg.append('#36688D')
    elif fb_graph.nodes[person]['gen'] == 'F':
        nodecolorlistg.append('#BDA589');
    else:
        nodecolorlistg.append('c')

#pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(fb_graph,pos,node_color = nodecolorlistg, node_size = nodesizelist,edge_color='0.5')
'''
# ------------------------------------------------------------------------------------------
# Boy-Boy Friendship graph
b2b = nx.Graph()
for (u, v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] == 'M' and fb_graph.nodes[v]['gen'] == 'M':
        b2b.add_edge(u, v)

b2bnodeclrlist = []
b2bnodesizelist = [2000 * nx.degree_centrality(fb_graph)[node] for node in b2b]
b2bnodecolorlist2 = [1000 * nx.closeness_centrality(fb_graph)[node] for node in b2b]
for person in b2b:
    if fb_graph.nodes[person]['sec'] == 'A':
        b2bnodeclrlist.append('#36688D')
    elif fb_graph.nodes[person]['sec'] == 'B':
        b2bnodeclrlist.append('#BDA589')
    elif fb_graph.nodes[person]['sec'] == 'C':
        b2bnodeclrlist.append('#F3CD05')
    else:
        b2bnodeclrlist.append('c')

pos = nx.spring_layout(b2b)
plt.figure(figsize=(19.8, 10.2))
plt.title('Male- Male Friendships')
nx.draw_networkx(b2b, pos, edge_color='0.7', node_size=b2bnodesizelist, node_color=b2bnodeclrlist)
plt.savefig('fbb2b.pdf', format='pdf')

# --------------------------------------------------------------------------------------------
# Girl-Girl Friendship

'''for (u,v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[u]['sec'] == 'A':
        b2b.add_node(u,gen = 'F',sec='A')
    elif fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[u]['sec'] == 'B':
        b2b.add_node(u,gen = 'F',sec='B')
    elif fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[u]['sec'] == 'C':
        b2b.add_node(u,gen = 'F',sec='C')
    else:
        b2b.add_node(u,gen = 'F', sec = 'All')

for (u,v) in fb_edge_list:
    if fb_graph.nodes[v]['gen'] == 'F' and fb_graph.nodes[v]['sec'] == 'A':
        b2b.add_node(v,gen = 'F',sec='A')
    elif fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[v]['sec'] == 'B':
        b2b.add_node(v,gen = 'F',sec='B')
    elif fb_graph.nodes[v]['gen'] == 'F' and fb_graph.nodes[v]['sec'] == 'C':
        b2b.add_node(v,gen = 'F',sec='C')
    else:
        b2b.add_node(v,gen = 'F', sec = 'All')'''

g2g = nx.Graph()
for (u, v) in fb_edge_list:
    if fb_graph.nodes[u]['gen'] == 'F' and fb_graph.nodes[v]['gen'] == 'F':
        g2g.add_edge(u, v)

g2gnodeclrlist = []
for person in g2g:
    if fb_graph.nodes[person]['sec'] == 'A':
        g2gnodeclrlist.append('#36688D')
    elif fb_graph.nodes[person]['sec'] == 'B':
        g2gnodeclrlist.append('#BDA589')
    elif fb_graph.nodes[person]['sec'] == 'C':
        g2gnodeclrlist.append('#F3CD05')
    else:
        g2gnodeclrlist.append('c')

pos = nx.spring_layout(g2g)
plt.figure(figsize=(12, 12))
plt.title('Female-Female Friendships')
nx.draw_networkx(g2g, pos, edge_color='0.5', node_color=g2gnodeclrlist)
# ---------------------------------------------------------------------------------------------
bfs_t = nx.bfs_tree(fb_graph, 'Sumeet')
bfsnodecolorlist = []
pos = nx.shell_layout(bfs_t)
# nx.draw(G, pos, with_labels=False, arrows=True)
plt.figure(figsize=(15, 15));

for person in bfs_t:
    if nx.shortest_path_length(bfs_t, 'Sumeet', person) == 1:
        bfsnodecolorlist.append('r')
    elif nx.shortest_path_length(bfs_t, 'Sumeet', person) == 2:
        bfsnodecolorlist.append('b')
    elif nx.shortest_path_length(bfs_t, 'Sumeet', person) == 3:
        bfsnodecolorlist.append('g')
    else:
        bfsnodecolorlist.append('y')

'''for person in bfs_t:
    if fb_graph.has_edge(person,'Sumeet'):
        bfsnodecolorlist.append('r')
    else:
        bfsnodecolorlist.append('c')'''
nx.draw_networkx(bfs_t, pos, node_color=bfsnodecolorlist)
# shows bfs tree with starting node Mihir. Very interesting Tree structure.
# ---------------------------------------------------------------------------------
# dfs-tree
# plt.figure(figsize=(18,18))
# nx.draw_networkx(nx.dfs_tree(fb_graph,'Mihir'))

'''disc = nx.Graph()
disc.add_edges_from(fb_edge_list)
disc.remove_edges_from([('Mihir', ' Nupur'),
 ('Mihir', 'Toshi'),
 ('Mihir', 'Atharv'),
 ('Mihir', 'Nissi'),
 ('Mihir', 'Prashant'),
 ('Mihir', 'Prathiksha'),
 ('Mihir', 'Sam'),
 ('Mihir', 'Vishwajeet'),
 ('Mihir', 'Sanjana'),
 ('Mihir', 'Soundarya')])
plt.figure(figsize=(15,15));
pos = nx.spring_layout(disc)
nx.draw_networkx(disc,pos,node_conlor = nodecolorlist) '''
# ---------------------------------------------------------------------------------
# Given 2 friends, connect them by seeing how many mutual friends they have
mfg = nx.Graph()
# MORE THAN 8 MUTUAL FRIENDS.
for u in fb_graph.nodes:
    for v in fb_graph.nodes:
        if mfg.has_edge(u, v) or u == v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(fb_graph, u, v):
                cn.append(i)
            if len(cn) > 9:
                mfg.add_edge(u, v, MF=len(cn))

nodecolorlist = []
for person in mfg:
    if fb_graph.nodes[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif fb_graph.nodes[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif fb_graph.nodes[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

plt.figure(figsize=(19.2, 10.8))
nx.draw_networkx(mfg, node_size=200, node_color=nodecolorlist, cmap='coolwarm', edge_color='0.7')
plt.savefig('fbmfg.pdf', format='pdf')

# ---------------------------------------------------------------------------------
# MUTUAL FRIENDS, NOT CONNECTED. - POTENTIAL FRIENDS
mfgnc = nx.Graph()
# MORE THAN 8 MF, NOT CONNECTED
for u in fb_graph.nodes:
    for v in fb_graph.nodes:
        if mfgnc.has_edge(u, v) or u == v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(fb_graph, u, v):
                cn.append(i)
            if len(cn) > 7 and not (fb_graph.has_edge(u, v)):
                mfgnc.add_edge(u, v, MF=len(cn))

nodecolorlist = []
for person in mfgnc:
    if fb_graph.nodes[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif fb_graph.nodes[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif fb_graph.nodes[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

plt.figure(figsize=(10, 10))
nx.draw_networkx(mfgnc, node_size=200, node_color=nodecolorlist, cmap='coolwarm', edge_color='0.5')
plt.savefig('fbmfgnc.pdf', format='pdf')
# ---------------------------------------------------------------------------------
# Degree Centrality

degcentgraph = nx.Graph(fb_graph)

nodesizelistdeg = [70 * fb_graph.degree(node) for node in fb_graph]
nodecolorlist2 = [fb_graph.degree(student) for student in fb_graph]
pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20, 12.6))
nx.draw_networkx(degcentgraph, node_size=nodesizelistdeg, node_color=nodecolorlist2, cmap='coolwarm', edge_color='0.7')
plt.savefig('fbdegcent.pdf', format='pdf')

plt.figure(figsize=(15, 15))
nx.draw_networkx(degcentgraph, node_size=nodesizelistdeg, node_color=nodecolorlist2, cmap='RdYlBu')

'''Colormap values:
    Possible values are: Accent, Accent_r, Blues, Blues_r, 
    BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2,
    Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, 
    OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1,
    Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r,
    PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r,
    RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, 
    Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, 
    Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r,
    Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd,
    YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r,
    brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, 
    cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
    gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, 
    gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, 
    gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, 
    magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma,
    plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, 
    spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, 
    tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r

    https://matplotlib.org/tutorials/colors/colormaps.html

    '''
# -------------------------------------------------------------------------------------------------
# Closeness Centrality
nodesizelistclo = [1500 * nx.closeness_centrality(fb_graph, node) for node in fb_graph]
nodecolorlistclo = [nx.closeness_centrality(fb_graph, student) for student in fb_graph]

# pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20, 12.6))
nx.draw_networkx(fb_graph, node_size=nodesizelistclo, node_color=nodecolorlistclo, cmap='RdYlGn', edge_color='0.8')
plt.savefig('fbcc.pdf', format='pdf')
# plt.figure(figsize=(15,15))
# nx.draw_networkx(fb_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='RdYlBu')

import operator

sorted(nx.closeness_centrality(fb_graph).items(), key=operator.itemgetter(1), reverse=True)

# ----------------------------------------------------------------------------------
# Betweenness Centrality

nodesizelistbet = [25000 * nx.betweenness_centrality(fb_graph)[node] for node in fb_graph]
nodecolorlistbet = [nx.betweenness_centrality(fb_graph)[student] for student in fb_graph]
pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20, 12.6))
nx.draw_networkx(fb_graph, node_size=nodesizelistbet, node_color=nodecolorlistbet, cmap='YlOrBr', edge_color='0.7')
plt.savefig('fbbtwcent.pdf', format='pdf')
# ----------------------------------------------------------------------------------
# Edge-betweenness centrality

edgesizelistbete = [200 * nx.edge_betweenness_centrality(fb_graph)[(u, v)] for u, v in
                    nx.edge_betweenness_centrality(fb_graph).keys()]
# nodecolorlistbete = [nx.betweenness_centrality(fb_graph)[node] for node in fb_graph]
edgecolorlistbete = [nx.edge_betweenness_centrality(fb_graph)[(u, v)] for u, v in
                     nx.edge_betweenness_centrality(fb_graph).keys()]
pos = nx.spring_layout(fb_graph, k=1, iterations=150)
# pos = nx.spring_layout(fb_graph)
plt.figure(figsize=(20, 20))
nx.draw_networkx(fb_graph, pos, edge_color=edgecolorlistbete, width=edgesizelistbete, node_size=500,
                 node_color='#BDA589')
# nx.draw_networkx_edges(Pgirls,pos,edgelist = edgelist_grt_than_5,edge_color = 'green',width=edge_width)
# nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)
# plt.figure(figsize=(20,20))
# nx.draw_networkx(fb_graph,node_size=20,node_color = nodecolorlistbete,cmap='coolwarm')

# nx.draw_networkx(fb_graph,node_size=20,node_color = nodecolorlistbete,cmap='YlOrBr',edge)


# ------------------------------------------------------------------------------------
# CLIQUES

clqlist = []
clqlist = list(nx.find_cliques(fb_graph))
for i in range(len(clqlist)):
    if len(clqlist[i]) > 8:
        print(clqlist[i])

# show how a clique looks like- just some random 6 node example, and then show the graph's cliques
c = nx.subgraph(fb_graph, ['Beenu', 'Nupur',
                           'Sumeet', 'Toshi', 'Pruthvi',
                           'Bhavya', ' '])
# highlight those nodes and edges in the graph.


clqgraph = nx.Graph(fb_graph)
edgeclrlist = []
clq1colorlist = []
clq2colorlist = []
nodelist = ['Rakshith', 'Harshita', 'Mihir', 'Prashant']
for node in clqgraph:
    if node in nodelist:
        clq1colorlist.append('#4169E1')
    else:
        clq1colorlist.append('#DCDCDC')

for u, v in clqgraph.edges():
    if u in nodelist and v in nodelist:
        edgeclrlist.append('#191970')
    else:
        edgeclrlist.append('0.85')

plt.figure(figsize=(20, 16))
pos = nx.spring_layout(clqgraph)
nx.draw_networkx_edges(clqgraph, pos, edge_color=edgeclrlist)
nx.draw_networkx_nodes(clqgraph, pos, node_size=300, node_color=clq1colorlist)
nx.draw_networkx_labels(clqgraph, pos)
plt.savefig('fbclqc.pdf', format='pdf')

# -------------------------------------------------------------------------------------
# SHORTEST PATH
shortpgraph = nx.Graph(fb_graph)
edgeclrlist = []
clq1colorlist = []
clq2colorlist = []
for node in shortpgraph:
    if node in ['Vishwajeet', 'Sarthak', 'Johanna']:
        clq1colorlist.append('#483D8B')
    else:
        clq1colorlist.append('#DCDCDC')

for u, v in shortpgraph.edges():
    if u in ['Vishwajeet', 'Sarthak', 'Johanna'] and v in ['Vishwajeet', 'Sarthak', 'Johanna']:
        edgeclrlist.append('#483D8B')
    else:
        edgeclrlist.append('0.85')

plt.figure(figsize=(20, 12.6))
pos = nx.spring_layout(shortpgraph, k=0.5)
nx.draw_networkx_edges(shortpgraph, pos, edge_color=edgeclrlist)
nx.draw_networkx_nodes(shortpgraph, pos, node_size=300, node_color=clq1colorlist)
nx.draw_networkx_labels(shortpgraph, pos)
plt.savefig('fbshortp.pdf', format='pdf')

# ------------------------------------------------------------------------------------
# Degree distribution graph

# import seaborn as sns
import collections

deg_dict = dict(fb_graph.degree)

degree_sequence = sorted([d for n, d in fb_graph.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.35, color='#4682B4')

plt.title("Degree Histogram")
plt.ylabel("Number of People")
plt.xlabel("Number of Friends")
ax.set_xticks([d + 0.5 for d in deg])
ax.set_xticklabels(deg)
# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
#Gcc = sorted(nx.connected_component_subgraphs(fb_graph), key=len, reverse=True)[0]
pos = nx.spring_layout(fb_graph)
plt.axis('off')
nx.draw_networkx_nodes(fb_graph, pos, node_size=20, node_color='Blue')
nx.draw_networkx_edges(fb_graph, pos, alpha=0.4, edge_color='0.5')
# plt.show()
plt.savefig('ddg-fb0.1.pdf', format='pdf')

# ----------------------------------------------------------------------------------
# VARYING CENTRALITY GRAPhs - nodesize = DEG CEN, nodecolor = CLO cen

nodesizelistclo = [100 * fb_graph.degree(node) for node in fb_graph]
nodecolorlistclo = [nx.closeness_centrality(fb_graph, student) for student in fb_graph]

# pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
# plt.figure(figsize=(20,20))

# plt.figure(figsize=(15,15))
# nx.draw_networkx(fb_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20, 20))
nx.draw_networkx(fb_graph, node_size=nodesizelistclo, node_color=nodecolorlistclo, cmap='coolwarm', edge_color='0.7')
# ---------------------------------------------------------------------------------
# VARYING CENTRALITY GRAPHS - NODESIZE = DEG CEN, COLOR = BTW CEN

nodesizelistclo = [100 * fb_graph.degree(node) for node in fb_graph]
nodecolorlistclo = [nx.betweenness_centrality(fb_graph)[student] for student in fb_graph]

# pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
# plt.figure(figsize=(20,20))

# plt.figure(figsize=(15,15))
# nx.draw_networkx(fb_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20, 20))
nx.draw_networkx(fb_graph, node_size=nodesizelistclo, node_color=nodecolorlistclo, cmap='coolwarm', edge_color='0.75')

# ---------------------------------------------------------------------------------
# VARYING CENTRALITIES - NODESIZE = BETW CEN, COLOR = CLOSE CEN

nodesizelistclo = [30000 * nx.betweenness_centrality(fb_graph)[student] for student in fb_graph]
nodecolorlistclo = [nx.closeness_centrality(fb_graph, student) for student in fb_graph]

# pos = nx.spring_layout(fb_graph,k=1,iterations=150)
pos = nx.spring_layout(fb_graph)
# plt.figure(figsize=(20,20))

# plt.figure(figsize=(15,15))
# nx.draw_networkx(fb_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20, 20))
nx.draw_networkx(fb_graph, node_size=nodesizelistclo, node_color=nodecolorlistclo, cmap='coolwarm', edge_color='0.8')

# ---------------------------------------------------------------------------------
alist = []
blist = []
clist = []
for node in fb_graph:
    if fb_graph.nodes[node]['sec'] == 'A':
        alist.append(node)
    elif fb_graph.nodes[node]['sec'] == 'B':
        blist.append(node)
    elif fb_graph.nodes[node]['sec'] == 'C':
        clist.append(node)
    else:
        pass
# ---------------------------------------------------------------------------------
# A-sec graph
'''
asec = nx.subgraph(fb_graph,alist)

nodesizelistclo = [2000*nx.closeness_centrality(asec,node) for node in asec]
nodecolorlistclo = [nx.closeness_centrality(asec,student) for student in asec]
plt.figure(figsize=(15,15))
nx.draw_networkx(asec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#B-sec graph

bsec = nx.subgraph(fb_graph,blist) 
nodesizelistclo = [2000*nx.closeness_centrality(bsec,node) for node in bsec]
nodecolorlistclo = [nx.closeness_centrality(bsec,student) for student in bsec]
plt.figure(figsize=(15,15))
nx.draw_networkx(bsec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#C-sec graph

csec = nx.subgraph(fb_graph,clist)
nodesizelistclo = [2000*nx.closeness_centrality(csec,node) for node in csec]
nodecolorlistclo = [nx.closeness_centrality(csec,student) for student in csec]
plt.figure(figsize=(15,15))
nx.draw_networkx(csec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')
'''
# -------------------------------------------------------------------------------------------------