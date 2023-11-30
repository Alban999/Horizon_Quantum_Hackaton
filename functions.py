# Open the file in read mode
import re
from qiskit import QuantumCircuit
from random import random
pattern = r"\[(\d+)\]"

def create_cliffordT(num_qubits, num_operations, file = 'input.txt'):
    # create a 
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
    with open(file, 'w') as file:
        file.write(circuit.qasm())

def read_qasm(file = 'input.txt'):
    ops = []
    q_is = []
    q_js = []
    with open(file, 'r') as file:
        # Read the file line by line
        for line in file:
            if line[:4] == 'qreg':
                match = re.search(pattern, line)
                numb_qubits = int(match.group(1))
            elif line[0] == 's': 
                ops.append(1)
                match = re.search(pattern, line)
                q_is.append(int(match.group(1)))
                q_js.append(-1)
            elif line[0] == 'h': 
                ops.append(2)
                match = re.search(pattern, line)
                q_is.append(int(match.group(1)))
                q_js.append(-1)
            elif line[0] == 't': 
                ops.append(3)
                match = re.search(pattern, line)
                q_is.append(int(match.group(1)))
                q_js.append(-1)
            elif line[:2] == 'cx': 
                ops.append(4)
                matches = re.findall(pattern, line)
                support = [int(match) for match in matches]
                q_is.append(support[0])
                q_js.append(support[1])
    numb_operations = len(ops)
    # now you have numb_qubits, numb_operations, ops, q_is, q_js
    return {'numb_qubits':numb_qubits, 'numb_operations':numb_operations, 'ops':ops, 'q_is':q_is, 'q_js':q_js}