class State:
    def __init__(self, name, accepting=False):
        self.name = name
        self.accepting = accepting
        self.transitions = {}

    def add_transition(self, symbol, target_state):
        self.transitions[symbol] = target_state

    def process_input(self, input_str):
        current_state = self
        for symbol in input_str:
            if symbol in current_state.transitions:
                current_state = current_state.transitions[symbol]
            else:
                return False  # Transition non définie, la chaîne n'est pas acceptée

        return current_state.accepting


def check_regex_match(input_str):
    # Définition de la machine à états finis (FA)
    start_state = State('start')
    state_a = State('a', accepting=True)
    state_b = State('b', accepting=True)
    state_ab = State('ab', accepting=True)

    start_state.add_transition('a', state_a)
    start_state.add_transition('b', state_b)
    state_a.add_transition('a', state_a)
    state_a.add_transition('b', state_ab)
    state_b.add_transition('a', state_ab)
    state_b.add_transition('b', state_b)
    state_ab.add_transition('a', state_a)
    state_ab.add_transition('b', state_b)

    return start_state.process_input(input_str)

def check_lines(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if check_regex_match(line.strip()):
                print(f"Ligne {line_number}: {line.strip()}")

check_lines('./router.unix')
