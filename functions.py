def create_cliffordT(num_qubits, num_operations, file = 'input.txt'):
    from qiskit import QuantumCircuit # To generate the QASM file, could be avoided but we used it for simplicity
    from random import random
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
    import re
    pattern = r"\[(\d+)\]"
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


def extract_counts_from_response(response_text):
    # Find the start and end indices of the "meas_outcomes" array
    meas_outcomes_str = response_text.split('meas_outcomes')[1]

    # Count occurrences of '["0"]' and '["1"]' in the substring
    count_0 = meas_outcomes_str.count('0')
    count_1 = meas_outcomes_str.count('1')

    return count_0, count_1

def get_results_from_api(url, api_key, job_id):
    import requests
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    data = {
        'job_id': job_id,
        'inputs': [['a', '1'], ['b', '1']],
    }

    response = requests.post(url, headers=headers, json=data)
    
    count_0, count_1 = extract_counts_from_response(response.text)
    
    return {'0': count_0, '1': count_1}
