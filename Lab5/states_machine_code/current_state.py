import sys


def main():
    user_input = ""

    print('Enter character by character.')
    print('Allowed characters are: a, b, c.')
    print('Use EOF (Ctrl+D) to end input.')

    # defining our states - just giving them names for readability
    s1 = '1'
    s2 = '2'
    s3 = '3'
    error = 'error'

    state = s1  # current state
    finish = s3  # proper finish state,
    # this can be a list

    # a hash map outlining possible transitions
    transitions = {
        (s1, 'a'): s1,
        (s1, 'b'): s2,
        (s2, 'c'): s3,
        (s2, 'a'): s1
        # we could add error states here,
        # but we handle that differently later
    }

    while True:

        # reading input
        try:
            c = input()
            user_input += c
            if c != 'a' and c != 'b' and c != 'c':
                raise ValueError("String doesn't fit the requirements. Letter not in the alphabet.")
        except EOFError:
            break
        except ValueError as e:
            print(e)
            sys.exit()

        # performing transition
        try:
            state = transitions[(state, c)]
            print("Current state: " + state)
            # if this were a Meley machine, this is where we'd add output
            # the print itself is technically a transition output, but
            # that's here just so we could see what's going on while learning
        except KeyError:
            # if we get any invalid key combo (because we've read c which
            # does not lead to a valid state) we'll end up in an error state
            # - here
            state = error
            print("Current state: " + state)
            break

    print("User input: ", user_input)

    # check if we've ended in the proper finish state or  not
    if state == finish:
        print("String fits the requirements.")
    else:
        print("String doesn't fit the requirements. Terminated in the wrong state.")


main()
