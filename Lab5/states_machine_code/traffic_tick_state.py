import sys


def main():
    user_input = ""

    print('Enter character by character.')
    print('Allowed characters is : t')
    print('Use EOF (Ctrl+D) to end input.')

    # defining our states - just giving them names for readability
    s1 = '1'
    s2 = '2'
    s3 = '3'
    error = 'error'

    one = 'go'
    two = 'stop'
    state = s1  # current state
    finish = s3  # proper finish state,
    # this can be a list

    # a hash map outlining possible transitions
    transitions = {
        (s1, 't'): s2,
        (s2, 't'): s3,
        (s3, 't'): s1,
        # we could add error states here,
        # but we handle that differently later
    }

    outputs = {
        s1: "Red",
        s2: "Green",
        s3: "Yellow",
        error: "error"
    }

    while True:

        # reading input
        try:
            c = input()
            user_input += c
            if c != 't':
                raise ValueError("String doesn't fit the requirements. Letter not in the alphabet.")
        except EOFError:
            break
        except ValueError as e:
            print(e)
            sys.exit()

        # performing transition
        try:
            state = transitions[(state, c)]
            color = outputs[state]
            print("Current Color: " + color)
        except KeyError:
            state = error
            print("Current state: " + state)
            break

    print("User input: ", user_input)

    if state == finish:
        print("String fits the requirements.")
    else:
        print("String doesn't fit the requirements. Terminated in the wrong state.")


main()
