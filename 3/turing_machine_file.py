import json

class TuringMachine:
    def __init__(self):
        self.Q = None
        self.start_state = None
        self.alphabet = None
        self.accept_state = 'qa'
        self.reject_state = 'qr'

    def print_tape(self, tape, current_index, cur_state):
        left_length = sum(len(word) + 2 for word in tape[:current_index]) + current_index
        num_spaces = (len(tape[current_index])+2) // 2
        cur_state+=' '
        tape_string =cur_state + ' '.join('|' + char + '|' for char in tape)
        marker_string = len(cur_state)*' ' + ' ' * (left_length + num_spaces) + '^'
        print(tape_string)
        print(marker_string)

    def run(self, file, input=None):

        with open(file, 'r') as f:
            config = json.load(f)
            self.start_state = config['start_state']
            if input is None:
                input_str = config['input_string']
            else:
                input_str = input
            self.Q = config['Q']
            self.alphabet = self.Q['q0'].keys()

        tape = list(input_str)
        for character in tape:
            if character not in self.alphabet:
                print(f'Character {character} is not acceptable!')
                return
        tape.append(' ')
        head_pos = 0
        current_state = self.start_state
        self.print_tape(tape, head_pos, current_state)


        while current_state != self.accept_state and current_state != self.reject_state:
            current_char = tape[head_pos]
            if not self.Q[current_state][current_char]:
                print(f"No transition defined for state {current_state} and input {current_char}")
                return

            next_state, write_char, move_dir = self.Q[current_state][current_char]
            if write_char != '':
                tape[head_pos] = write_char

            if next_state not in ['qa', 'qr']:
                if move_dir == 'L':
                    head_pos -= 1 if head_pos > 0 else 0
                elif move_dir == 'R':
                    head_pos += 1
                    if head_pos == len(tape):
                        tape.append(' ')

            current_state = next_state
            self.print_tape(tape, head_pos, current_state)
        if current_state == self.accept_state:
            print("Input accepted")
        else:
            print("Input rejected")

