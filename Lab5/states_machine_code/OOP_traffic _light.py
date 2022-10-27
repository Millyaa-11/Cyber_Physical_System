# https://stackabuse.com/theory-of-computation-finite-state-machines/
class Transition:
    """A change from one state to another"""

    def __init__(self, current_state, state_input, next_state, state_output):
        self.current_state = current_state
        self.state_input = state_input
        self.next_state = next_state
        self.state_output = state_output

    def match(self, current_state, state_input):
        """Determining when the state and the input satisfies this transition relation"""
        return self.current_state == current_state and self.state_input == state_input


class FSM:
    """a baisc model for State Machine"""
    def __init__(self, states=[], inputs=[], outputs=[], accepting_states=[], initial_state=' '):
        self.states = states
        self.inputs = inputs
        self.outputs = outputs
        self.accepting_states = accepting_states
        self.initial_state = initial_state
        self.valid_transitions = False

    def add_transitions(self, transitions=[]):
        """Before using a list of transitions, and verifying they only apply to our states"""
        for transition in transitions:
            if transition.current_state not in self.states:
                print('Invalid transition. {} is not a valid state'.format(transition.current_state))
                return
            if transition.next_state not in self.states:
                print('Invalid transition. {} is not a valid state'.format(transition.next_state))
                return

            if transition.state_output not in self.outputs:
                print('Invalid transition. {} is not a valid output'.format(transition.state_output))
                return

        self.transitions = transitions
        self.valid_transitions = True

    def _accept(self, current_state, state_input):
        """Looks to see when the input for the given state matches a transition rule"""
        # If the input is valid in our alphabet
        if state_input in self.inputs:
            for rule in self.transitions:
                if rule.match(current_state, state_input):
                    return rule.next_state, rule.state_output
            print('No transition for sate and input')
            return None
        return None

    def accepts(self, sequence ):
        """Process an input stream for determining if the FSM will accept it"""
        # Check if we have transitions
        if not self.valid_transitions:
            print('Cannot process sequence without valid transitions')

        print('Starting at {}'.format(self.initial_state))
        # When an empty sequence provided, we simply check if the initial state
        # is an accepted one
        if len(sequence) == 0:
            return self.initial_statein in self.accepting_states

        # Let’s process the initial state
        current_state, state_output = self._accept(self.initial_state, sequence[0])
        #current_state = temp[0]
        if current_state is None:
            return False

        # Continue with the rest of the sequence
        for state_input in sequence[1:]:
            print('Output is {}'.format(state_output))
            print('Current state is {}'.format(current_state))

            current_state, state_output = self._accept(current_state, state_input)



            print(' ')
            if current_state is None:
                return False

        print('Ending state is {}'.format(current_state))
        # Check if the state we have transitioned to is an accepted state
        return current_state in self.accepting_states



# Set up our FSM with the required info:
# Set of states
states = ['red', 'green', 'yellow']


# Set of allowed inputs
inputs = ['tick']

# Set of possible outputs
outputs = ['go', 'stop']

# Set of accepted states
accepting_states = ['red']

# The initial state
initial_state = 'red'
fsm = FSM(states, inputs,outputs, accepting_states, initial_state)

# Create the set of transitions
transition1 = Transition('red', 'tick', 'green', 'go')
transition2 = Transition('green', 'tick', 'yellow', 'stop')
transition3 = Transition('yellow', 'tick', 'red', 'stop')

transitions = [
    transition1,
    transition2,
    transition3]

# Verify and add them to the FSM
fsm.add_transitions(transitions)

# Now that our FSM is correctly set up, we can give it input to process
# Let's transition the FSM to a green light
should_be_accepted = fsm.accepts(['tick', 'tick', 'tick'])
print(should_be_accepted)

# # Let's transition the FSM to a red light
