import json

Q = {
     'q0': {'a': 'q0', 'b': 'q1', 'c': 'q3', 'd': 'q3'},
     'q1': {'a': 'q3', 'b': 'q3', 'c': 'q2', 'd': 'q3'},
     'q2': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q2'},
     'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'},
     }

accept_state = 'q2'

input_string = 'abcd'

my_dict = {'Q':Q, 'accept_state':accept_state, 'input_string':input_string}

with open('task4.json', 'w') as f:
    json.dump(my_dict, f)