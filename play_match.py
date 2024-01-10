# Author: Phil Aufdencamp, 8840

# This file will contain the main method which runs the match, and it defines the field

import networkx as nx
import matplotlib.pyplot as plt


def create_field():
    # Create a graph to represent the field
    G = nx.Graph() # It's convention to use capital G to denote 
    # a graph object when working with the networkX library

    # Add nodes with string names for each node
    G.add_node("Loading_Station") # Left half of the field
    G.add_node("Amplifier") # Right half of the field

    # Add an edge between the two nodes
    G.add_edge("Loading_Station","Amplifier")
    return G

def show_field(G):
    # Use matplot lib to show the field
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, 
        node_color="skyblue", font_size=10, font_color="black", 
        font_weight="bold", font_family="sans-serif")

    # Display the graph
    plt.show()

# The code below will run when this is the main method
if __name__ == "__main__":
    
    time = list(range(150)) # define the time vector that the match will take place over
    
    G = create_field()
    show_field(G)

    


