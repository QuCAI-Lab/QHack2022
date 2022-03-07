import sys
import pennylane as qml
from pennylane import numpy as np


def second_renyi_entropy(rho):
    """Computes the second Renyi entropy of a given density matrix."""
    # DO NOT MODIFY anything in this code block
    rho_diag_2 = np.diagonal(rho) ** 2.0
    return -np.real(np.log(np.sum(rho_diag_2)))


def compute_entanglement(theta):
    """Computes the second Renyi entropy of circuits with and without a tardigrade present.

    Args:
        - theta (float): the angle that defines the state psi_ABT

    Returns:
        - (float): The entanglement entropy of qubit B with no tardigrade
        initially present
        - (float): The entanglement entropy of qubit B where the tardigrade
        was initially present
    """

    dev = qml.device("default.qubit", wires=3)

    # QHACK #
    @qml.qnode(dev)
    def circuits(theta, tartigrade):
      if not tartigrade:
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        qml.PauliX(wires=0)
        return qml.density_matrix(wires=[0])     

    def partial_trace(rho, qubit_2_keep): # Credits: GitHub @neversakura.
        num_qubit = int(np.log2(rho.shape[0]))
        qubit_axis = [(i, num_qubit + i) for i in range(num_qubit)
                      if i not in qubit_2_keep]
        minus_factor = [(i, 2 * i) for i in range(len(qubit_axis))]
        minus_qubit_axis = [(q[0] - m[0], q[1] - m[1])
                            for q, m in zip(qubit_axis, minus_factor)]
        rho_res = np.reshape(rho, [2, 2] * num_qubit)
        qubit_left = num_qubit - len(qubit_axis)
        for i, j in minus_qubit_axis:
            rho_res = np.trace(rho_res, axis1=i, axis2=j)
        if qubit_left > 1:
            rho_res = np.reshape(rho_res, [2 ** qubit_left] * 2)
        return rho_res  

    psi_0 = np.array([1, 0])
    psi_1 = np.array([0, 1])
    g_bt = np.kron(psi_0, psi_0)
    e_bt=np.cos(theta/2)*np.kron(psi_1,psi_0)+np.sin(theta/2)*np.kron(psi_0,psi_1)
    psi_abt = 1/np.sqrt(2)*(np.kron(psi_0, e_bt)+np.kron(psi_1, g_bt))
    rho_abt = np.outer(psi_abt, np.conj(psi_abt))
    rho_b = partial_trace(rho_abt, [1])
    mu_b = circuits(theta, 0)
    s_mub = second_renyi_entropy(mu_b)
    s_rhob = second_renyi_entropy(rho_b)
   
    return s_mub, s_rhob
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    theta = np.array(sys.stdin.read(), dtype=float)

    S2_without_tardigrade, S2_with_tardigrade = compute_entanglement(theta)
    print(*[S2_without_tardigrade, S2_with_tardigrade], sep=",")
