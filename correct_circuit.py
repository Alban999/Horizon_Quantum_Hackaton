import functions as fn

output_file = 'triple_alpha_code/constants.qh'
numb_qubits = int(input("numb_qubits: "))
numb_operations = input("numb_operations: ")

protocol = input("protocol: ")
noise_model = input("noise_model: ")
backend = input("backend: ")


try: 
    numb_operations = int(numb_operations)
    input_file = 'input_file.txt'
except TypeError:
    input_file = numb_operations

print('input file:', input_file)


fn.create_cliffordT(numb_qubits, numb_operations, input_file)
variables = fn.read_qasm(input_file)

variables['numb_qubits'] = numb_qubits
variables['theta_x'] = 0.3
variables['theta_y'] = 0.0
variables['theta_z'] = 0.0
variables['protocol'] = protocol
variables['noise_model'] = noise_model
variables['backend'] = backend

# Open the file in write mode
with open(output_file, 'w') as file:
    # Iterate through dictionary items and write to the file
    for key, value in variables.items():
        if key == 'backend':
            value = str(value)
            file.write(f"'{value}' -> {key}\n")
        else:
            try:
                value = int(value)
                file.write(f'{value} -> {key}\n')
            except TypeError or ValueError:
                if isinstance(value, list):
                    for el in range(len(value)):
                        file.write(f'{value[el]} -> {key}.[{el}]\n')
                