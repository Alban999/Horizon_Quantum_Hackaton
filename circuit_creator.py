from qiskit import QuantumCircuit
from random import random

num_qubits = 4
num_operations = 10

circuit = QuantumCircuit(num_qubits)
for num_op in range(num_operations):
    op = int(random()*4+1)
    q_i = int(random()*num_qubits)
    if op==1: # S
        circuit.s(q_i)
    if op==2: # H
        circuit.h(q_i)
    if op==3: # T
        circuit.t(q_i)
    if op==4: # CX
        while True:
            q_j = int(random()*num_qubits)
            if q_j!=q_i: break
        circuit.cx(q_i, q_j)

with open("input.txt", 'w') as file:
    file.write(circuit.qasm())


