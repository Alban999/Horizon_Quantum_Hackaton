import functions as fn

print('...................................................................................................................\n....................WELCOME...TO...................................................................................\n...................................................................................................................\n..........................@%@@@@@@@%@..............................................................................\n.......................@@@@@.......................................................................................\n.....................%@@@..........................................................................................\n.............@-.....@@@-...........................................................................................\n..............%@...@@%.....*@%@@@@......-@@@@@-........-@@@-....@@@@@@@@@@@.=@@@@@@@@@@....@@@@@=..................\n...............@%.@@@...@%@@%..+@....:-@@@@@@@@@@.....-@@@@@....@@@@@@@@@@@.=@@@@@@@@@@..@@@@@@@@@@................\n................@@@@:..@@@......@@...=@@@@....@@-....:#@@@@@@......:@@@.....=@@@........*@@@....:@@................\n................*@@@..%@@-......#@%.-@@@@............=@@@:@@@@.....-@@@.....=@@@@@@@@@:..@@@@@@@...................\n................@@@...%@@.......*@@.:@@@@..=@@@@@%..-@@@*--@@@#....-@@@.....=@@@@@@@@@-...:@@@@@@@@................\n................@@@=..#@@%......@@@..#@@@%...-@@@%.-@@@@@@@@@@@:...-@@@.....=@@@.........*+....#@@@................\n...............:@@@....@@@@@@@@@@@....=@@@@@@@@@@%-@@@@.....@@@@...-@@@.....=@@@@@@@@@@.@@@@@@@@@@@................\n................@@%......@@@@@@@.........%@@@@@:..-@@@=......@@@@..:@@@.....-@@@@@@@@@@....@@@@@%..................\n...................................................................................................................\n.............................................Documentation.at:.https://github.com/Alban999/Horizon_Quantum_Hackaton\n...................................................................................................................')

# Example usage
url = input("url: ")
api_key = input("api_key: ")
job_id = input("job_id: ")


result_counts = fn.get_results_from_api(url, api_key, job_id)
print(result_counts)
