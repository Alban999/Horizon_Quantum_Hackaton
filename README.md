# YOGATES
## Mitigating your noisy gates on a high level manner

As part of the first Horizon Quantum Hackathon we took advantage of Triple Alpha to create an API that can be ran through Python to apply a QEC protocol on an arbitrary circuit composed by Clifford+T gates. We do this by exploiting the Helium language. 

User's guide to run the code:
- copy the files contained in the 'triple_alpha_code' folder on the Helium folder, except for the 'standard_gate_set.qis' which have to replace the original ones.
- correct the address for the API in 'correct_circuit.py'.
- run 'correct_circuit.py' from the terminal with 5 parameters describing the kind of experiment to be ran.

This last Python file will then run the API on Horizon Quantum and output the final register obtained from the backend. 

Here we provide a brief overview of our code:
1. correct_circuit.py: The user interface is offered through Python and the correct_circuit.py file will take as input from the user 5 variables:
  1.1. numb_qubits: the number of logical qubits;
  1.2. operations: if integer -> number of operations (num_operations), if file.txt -> a python routine (circuit2lists.py) will be called to convert the OPENQASM circuit to our formalism made by strings:
   - ops: lists of gates encoded as integer numbers between 1 and 4, i.e. ops[i] = {1: S gate, 2: T gate, 3: H gate, 4: CX gate};
   - q_is, q_js: lists of qubits on which the ops are applied. If the operation is a single qubit gate then the q_js[i] associated with that operation will be set in '-1';
  1.3. protocol: integer number that selects the QEC scheme: 1->bitflip_protocol, 2->phaseflip_protocol, 3->five_qubits_protocol;
  1.4. noise_model: integer number that selects the noise model: 1->flips around X, 2->flips around Z, 3->random rotation, [4 -> dephasing error];
  1  5. backend: text description of the backend to be used;
2. circuit_creator.py: creates a random Clifford+T circuit of num_operations operations and prints in a 'input.txt' file the OPENQASM circuit;
3. circuit_reader.py: converts the OPENQASM circuit to the three lists ops, q_is, q_js;
4. triple_alpha_code: folder containing the files stored on the Horizon Quantum IDE:
  4.1. main.qhe: by the means of subroutines, applies the operations on the initial state (the 'in' register) by applying the selected QEC protocol and randomly applies the noise
  4.2. magic_states.qhe: by running in parallel another circuit it creates a reservouir of |T> to the teleported on the 'in' register in case a T gate is needed
  4.3. protocols.qhe: library of subroutines of the three QEC protocols implemented
  4.4. constants.qh: file containing all the fixed variables, either defined on the IDE or passed through the API from the python call
  4.5. maybe_noise.py: single qubit operation that applies a noise on the 'in' qubits
  4.6. standard_gate_set.qis: -> to be used as set of operations, contains the new noisy gates that it will call from maybe_noise.py





