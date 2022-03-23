[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/QuCAI-Lab/QHack2022/blob/dev/solutions_notebook.ipynb)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](#)
[![License](https://img.shields.io/github/license/QuCAI-Lab/QHack2022.svg?logo=CreativeCommons&style=flat-square)](https://github.com/QuCAI-Lab/QHack2022/blob/dev/LICENSE.md)
[![Contributions](https://img.shields.io/badge/contributions-welcome-orange?style=flat-square)](#)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/QuCAI-Lab/QHack2022/graphs/commit-activity)
[![Release](https://img.shields.io/github/release/QuCAI-Lab/QHack2022.svg)](https://github.com/QuCAI-Lab/QHack2022/releases)
<!-- [![version](https://img.shields.io/badge/version-0.0.1-blue)](#) -->

<div align="center">
  <a href="https://qucai-lab.github.io/"><img src="https://github.com/QuCAI-Lab/qucai-lab.github.io/blob/main/assets/QuCAI-Lab.png" height="500" width="500" /></a>
</div>

<div align="center">
  <h1> <a href="https://qhack.ai/"> QHack2022 </a> -  <a href="https://qhack.ai/events/#coding-challenges">Coding Challenge Solutions</a> </h1>
  <h2> Hackeinberg Team Repository</h2>
  
</div>
<br>

<!--  -->

# Dependencies

<code>
<a href="https://www.python.org/"><img height="27" src="https://www.python.org/static/img/python-logo.png">
<a href="https://numpy.org/"><img height="27" src="https://numpy.org/images/logo.svg">
<a href="https://matplotlib.org"><img height="27" src="https://matplotlib.org/_static/images/logo2.svg"> 
<a href="https://pennylane.ai/"><img height="27" src="https://pennylane.ai/img/xanadu_x.png"></a>
</code>
<br>
<br>

For specific versions, see the [requirements.txt](requirements.txt) file.

# First steps

Clone this repository:
```bash
git clone https://github.com/QuCAI-Lab/QHack2022.git && cd QHack2022
```
Create a conda environment with the required dependencies:
```bash
conda env create -n qhack2022 environment.yml && conda activate qhack2022
```
Alternatively, one can install the required dependencies via the `requirements.txt` file:
```bash
conda create -yn qhack2022 && conda activate qhack2022 && conda install -yc conda-forge pip==22.0.3
```
```bash
python3 -m pip install --user --upgrade pip && python3 -m pip install -r requirements.txt
```

# Table of Contents

- **[solutions_notebook](solutions_notebook.ipynb)**
- **[PennyLane101](pennylane101)**
  - **[pennylane101_100_OrderMatters_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/pennylane101/pennylane101_100_OrderMatters_solution.py)**
  - **[pennylane101_200_KnowYourDevices_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/pennylane101/pennylane101_200_KnowYourDevices_solution.py)**
  - **[pennylane101_300_superdense_coding_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/pennylane101/pennylane101_300_superdense_coding_solution.py)**
  - **[pennylane101_400_FiniteDifferenceGradient_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/pennylane101/pennylane101_400_FiniteDifferenceGradient_solution.py)**
  - **[pennylane101_500_BitflipErrorCode_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/pennylane101/pennylane101_500_BitflipErrorCode_solution.py)**
- **[Algorithms](quantum_algorithms)**
  - **[algorithms_100_DeutschJozsa_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_algorithms/algorithms_100_DeutschJozsa_solution.py)**
  - **[algorithms_200_AdaptingTopology_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_algorithms/algorithms_200_AdaptingTopology_solution.py)**
  - **[algorithms_300_AdderQFT_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_algorithms/algorithms_300_AdderQFT_solution.py)**
  - **Algorithms-400-Quantum-Counting**
  - **Algorithms-500-Deutsch-Jozsa-Strikes-Again**
- **[QuantumMachineLearning](quantum_machine_learning)**
  - **[qml_100_GeneratingFourierState_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_machine_learning/qml_100_GeneratingFourierState_solution.py)** 
  - **[qml_200_WhoLikesTheBeatles_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_machine_learning/qml_200_WhoLikesTheBeatles_solution.py)**
  - **Quantum Machine-Learning-300-Ising-on-the-Cake**
  - **[qml_400_BuildingQRAM_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_machine_learning/qml_400_BuildingQRAM_solution.py)**
  - **Quantum Machine-Learning-500-UDMIS**
- **[QuantumChemistry](quantum_chemistry)**
  - **[qchem_100_IsParticlePreserving_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_chemistry/qchem_100_IsParticlePreserving_solution.py)** 
  - **[qchem_200_OptimizingMeasurements_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_chemistry/qchem_200_OptimizingMeasurements_solution.py)**
  - **Quantum Chemistry-300-Givens-Universality**
  - **Quantum Chemistry-400-Triple-Givens**
  - **Quantum Chemistry-500-Mind-the-Gap**
- **[Games](quantum_games)**
  - **[games_100_TardigradeMasquerade_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_games/games_100_TardigradeMasquerade_solution.py)**  
  - **[games_200_CHSH_solution.py](https://github.com/QuCAI-Lab/QHack2022/tree/dev/quantum_games/games_200_CHSH_solution.py)** 
  - **Games-300-Bomb-Tester** 
  - **Games-400-Find-the-Car** 
  - **Games-500-Switches** 

# Group distribution
  
- [Lucas Camponogara Viera](https://github.com/camponogaraviera) (theory and implementation).
- [José Paulo Marchezi](https://github.com/zemarchezi) (implementation).
- [Douglas Franco Pinto](https://www.linkedin.com/in/douglas-pinto-89466b7a/) (theory).
  
None of the members had prior knowledge of PennyLane. The learning experience was on-the-go. The week was busy for all members, so we were able to complete only 15/25 challenges.
  
# References &nbsp; <a href="#"><img valign="middle" height="45px" src="https://img.icons8.com/book" width="45" hspace="0px" vspace="0px"></a> 

\[1] [QHack2022 problemset templates](https://github.com/XanaduAI/QHack/tree/master/Coding_Challenges).

[2] [PennyLane Documentation](https://pennylane.readthedocs.io/en/stable/).

[3] Nielsen MA, Chuang IL. 2010. Quantum Computation and Quantum Information. New York: [Cambridge Univ. Press.](https://doi.org/10.1017/CBO9780511976667) 10th Anniv. Ed.

# License

This work is licensed under a [Creative Commons Zero v1.0 Universal](LICENSE.md) license.

<hr>

Created and maintained by [@camponogaraviera][1].

[1]: https://github.com/camponogaraviera
