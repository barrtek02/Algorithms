from finite_automata import finite_automata

Q = {
     'q0': {'a': 'q1', '0': 'q3', '1': 'q3'},
     'q1': {'a': 'q2', '0': 'q1', '1': 'q1'},
     'q2': {'a': 'q3', '0': 'q2', '1': 'q2'},
     'q3': {'a': 'q3', '0': 'q3', '1': 'q3'},
     }


input_string = 'aa00'
accept_state = 'q2'

finite_automata(Q, input_string, accept_state)
