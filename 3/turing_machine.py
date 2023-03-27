class TuringMachine:
    def __init__(self, Q, start_state='q0'):
        self.Q = Q #dict of transitions
        self.start_state = start_state
        self.alphabet = [key[1] for key in Q.keys() if key[0]==start_state]
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

    def run(self, input_str):
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
            if (current_state, current_char) not in self.Q:
                print("No transition defined for state {} and input {}".format(current_state, current_char))
                return

            next_state, write_char, move_dir = self.Q[(current_state, current_char)]
            if write_char != '':
                tape[head_pos] = write_char

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
