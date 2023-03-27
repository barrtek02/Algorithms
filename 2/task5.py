import json

# file = 'my_simulation.json'
file = 'task4.json'
# file = 'task.json'


with open(file, 'r') as f:
    config = json.load(f)
    accept_state = config['accept_state']
    input_string = config['input_string']
    Q = config['Q']

def finite_automata(states, string, accept_state):
    current_state = 'q0'
    alphabet = list(states[current_state].keys())

    for symbol in string:
        if symbol not in alphabet:
            return "String doesn't match alphabet {alphabet}!"

    text = []
    for symbol in string:
        next_state = states[current_state][symbol]
        text.append(f'{current_state} ------- {symbol} ------> {next_state}')
        current_state = next_state
    text.append(f'Final state: {next_state}')
    if current_state in accept_state:
        text.append(f'Input string accepted')
    else:
        text.append(f'Input string not accepted')

    return text

simulation = finite_automata(Q, input_string, accept_state)
config['simulation']=simulation

with open(file, 'w') as f:
    json.dump(config, f)
