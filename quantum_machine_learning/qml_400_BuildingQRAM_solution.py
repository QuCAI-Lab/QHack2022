#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def qRAM(thetas):
    """Function that generates the superposition state explained above given the thetas angles.

    Args:
        - thetas (list(float)): list of angles to apply in the rotations.

    Returns:
        - (list(complex)): final state.
    """

    # QHACK #

    # Use this space to create auxiliary functions if you need it.

    def CCCRY(theta, i):
      
      '''
      Function that returns the CCCRY gate using qml.ControlledQubitUnitary().
      '''

      ry  = np.array([[np.cos(theta/2), -np.sin(theta/2)],
                      [np.sin(theta/2), np.cos(theta/2)]])     
       
      lst=[str(j) for j in basis[i]] 
      gate = qml.ControlledQubitUnitary(ry, control_wires=[0, 1, 2], wires=3, control_values=str(''.join(lst)))
      return gate

    n=3   
    basis=[]
    for i in range(2**n):
      arr = []
      for j in list(f'{i:0{n}b}'):    
        arr.append(int(j))  
      basis.append(arr)

    # QHACK #

    dev = qml.device("default.qubit", wires=range(4))
    global circuit
    @qml.qnode(dev)
    def circuit():

        # QHACK #

        # Create your circuit: the first three qubits will refer to the index, the fourth to the RY rotation.
        for i in range (3):
          qml.Hadamard(wires=i)
        for i in range(len(thetas)):
          CCCRY(thetas[i], i)

        # QHACK #

        return qml.state()

    return circuit()

'''
if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    thetas = np.array(inputs, dtype=float)

    output = qRAM(thetas)
    output = [float(i.real.round(6)) for i in output]
    print(*output, sep=",")
'''
