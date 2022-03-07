#! /usr/bin/python3
import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.
    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'
    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    import queue
    def minEdgeBFS(edges, u, v, n):

        # visited[n] for keeping track
        # of visited node in BFS
        visited = [0] * n

        # Initialize distances as 0
        distance = [0] * n

        # queue to do BFS.
        Q = queue.Queue()
        distance[u] = 0

        Q.put(u)
        visited[u] = True
        while (not Q.empty()):
            x = Q.get()

            for i in range(len(edges[x])):
                if (visited[edges[x][i]]):
                    continue

                # update distance for i
                distance[edges[x][i]] = distance[x] + 1
                Q.put(edges[x][i])
                visited[edges[x][i]] = 1
        return distance[v] - 1    
    return 2*minEdgeBFS(graph, cnot.wires[0], cnot.wires[1], len(graph.keys()))
    # QHACK #

if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
