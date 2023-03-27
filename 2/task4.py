from finite_automata import finite_automata

Q = {
     'q0': {'a': 'q0', 'b': 'q1', 'c': 'q3', 'd': 'q3'},
     'q1': {'a': 'q3', 'b': 'q3', 'c': 'q2', 'd': 'q3'},
     'q2': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q2'},
     'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'},
     }

accept_state = 'q2'

input_string = 'abcd'
finite_automata(Q, input_string, accept_state)