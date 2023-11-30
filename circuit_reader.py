# Open the file in read mode
import re
pattern = r"\[(\d+)\]"

ops = []
q_is = []
q_js = []
with open('input.txt', 'r') as file:
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