import numpy as np

def avg_deg(n, m):
    r"""Computes average degree of G that is defined as :math:`frac{2m}{n}` for
    undirected networks and :math:`frac{m}{n}` for directed networks
    """
    
    return m / n
    
def preferential_attachment(N_current, PrefAry, G, Nlinks):
    """Preferentially attach InComing_Nodes with Nlinks source nodes to update
    G and PrefAry and returns incremented N_current
    """            
    # Get the source nodes from PrefAry uniformly at random (preferential attachment)
    sources = np.random.choice( PrefAry, size = Nlinks, replace = False ).tolist()

    for s in sources:
        # Update the graph and PrefAry list 
        G.add_edge(s, N_current)
        PrefAry.extend([s, N_current])
