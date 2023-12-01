# YOGATES: Mitigating Noisy Gates at High Level
[![YOGATES](yogates.png)](yogates.gif)

In the inaugural Horizon Quantum Hackathon, we harnessed Triple Alpha's capabilities to develop an API that executes a Quantum Error Correction (QEC) protocol on arbitrary circuits involving Clifford+T gates. This innovative solution is implemented using the Helium language.

## User Guide to Run the Code:

1. Run `correct_circuit.py` from the terminal, providing 5 parameters to describe the experiment.
2. Copy files from the `triple_alpha_code` folder to the Helium directory, excluding `standard_gate_set.qis`, which has to replace the instructions set in the 'Other' folder.
3. Run `results_display.py` from the terminal, providing 3 parameters to return the final dictionary obtained from Horizon Quantum.

The Python script `correct_circuit.py` will execute the API on Horizon Quantum and yield the final register obtained from the backend.

## Code Overview:

1. **`correct_circuit.py`:** This Python file serves as the user interface, taking 5 input variables:
   1. `numb_qubits`: the number of logical qubits.
   2. `operations`: if an integer, it represents the number of operations (`num_operations`); if a file.txt, a Python routine (`circuit2lists.py`) converts the OPENQASM circuit to our formalism.
   3. `protocol`: an integer selecting the QEC scheme (1->bitflip_protocol, 2->phaseflip_protocol, 3->five_qubits_protocol).
   4. `noise_model`: an integer selecting the noise model (1->flips around X, 2->flips around Z, 3->random rotation, [4 -> dephasing error]).
   5. `backend`: a text description of the backend to be used [not yet available from the IDE side to insert the backend as a parameter]
   The output is the `constants.qh` saved in the `triple_alpha_code` folder. In this file we save all the variables necessary to run Helium.

2. **`functions.py`:** Contains two functions:
   1. **`create_cliffordT`:** Generates a random Clifford+T circuit with `num_operations` operations and prints the OPENQASM circuit to `input.txt`.
   2. **`read_qasm`:** Converts the OPENQASM circuit to three lists: `ops`, `q_is`, and `q_js`.
  
3. **`results_display.py`:** This Python file serves as the user interface, taking 3 input variables `url`, `api_key`, and `job_id` to run an API which returns results converted into a dictionary file

4. **`Triple_Alpha_Code`:** Folder containing files stored on the Horizon Quantum IDE:
   1. `main.qhe`: Applies operations on the initial state, incorporating the selected QEC protocol and introducing random noise.
   2. `magic_states.qhe`: Runs another circuit in parallel to create a reservoir of |T> states for teleportation onto the `in` register when a T gate is needed.
   3. `protocols.qhe`: Library of subroutines for the three implemented QEC protocols.
   4. `constants.qh`: Contains fixed variables defined on the IDE [created by the `correct_circuit.py` file]
   5. `maybe_noise.py`: Single-qubit operation applying noise on the 'in' qubits.
   6. `standard_gate_set.qis`: Set of operations, containing the new noisy gates called from `maybe_noise.py`.

YOGATES, your solution to mitigating noisy gates in quantum circuits at high level! 🎉
