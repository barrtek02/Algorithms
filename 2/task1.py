Q = {
     'q0': {'0': 'q1', '1': 'q0'},
     'q1': {'0': 'q3', '1': 'q2'},
     'q2': {'0': 'q2', '1': 'q0'},
     'q3': {'0': 'q2', '1': 'q2'}
    }

accept_state = 'q3'

def finite_automata(states, string, accept_state):
    current_state = 'q0'
    alphabet = list(states[current_state].keys())
    string_correct = True

    for symbol in string:
        if symbol not in alphabet:
            string_correct = False
            print(f"String doesn't match alphabet {alphabet}!")
            break

    if string_correct is True:
        for symbol in string:
            next_state = states[current_state][symbol]
            print(f'{current_state} ------- {symbol} ------> {next_state}')
            current_state = next_state
        print(f'Final state: {next_state}')
        if current_state == accept_state:
            print(f'Input string accepted')
        else:
            print(f'Input string not accepted')


input_string = '1100'
finite_automata(Q, input_string, accept_state)

