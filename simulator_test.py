"""THIS FILE WILL BEGIN TO RUN THE SIMULATOR DUE TO THE IMPORT STATEMENT!!!
TO TEST PROPERLY, TYPE 'EXIT' WHERE THE CONSOLE ASKS FOR INPUT."""
from simulate import is_valid, process_input
from test import verify_test
from display import print_cube

solved_cube = """      y y y
      y y y
      y y y
o o o b b b r r r g g g
o o o b b b r r r g g g
o o o b b b r r r g g g
      w w w
      w w w
      w w w"""

#list of valid inputs that return cube to original state at the end of the sequence
valid_input_list = ("r u r' u' r u r' u' r u r' u' r u r' u' r u r' u' r u r' u'",
              "r r r r",
              "u' u' u' u'",
              "f2 f2",
              "l l2 l",
              "b' b2 b'",
              "r2 d2 r2 d2 r2 d2 r2 d2 r2 d2 r2 d2")
#list of inputs containing invalid commands
invalid_input_list = ("red",
                      "tr x yz",
                      "r u r2 uf",
                      "m2 e2 s2 rw2",
                      "d e f fed r e dy e s",
                      "r2 u2 r'2 u2 r2 u2 r2 u2")
#invalid commands that should be identified
invalid_commands = ("red",
                    "tr",
                    "uf",
                    "rw2",
                    "fed",
                    "r'2")

#run valid inputs, should all return cube to solved state
for input in valid_input_list:
    if is_valid(input.split()) is None:
        process_input(input.split())
        display_state = print_cube()
        if not verify_test(display_state, solved_cube):
            break
    else:
        print(f"Test failed: valid input '{input}' identified as invalid.")
        break

#run invalid inputs, console will identify the first invalid command found
for i in range(len(invalid_input_list)):
    invalid_command = is_valid(invalid_input_list[i].split())
    if invalid_command is not None:
        print("First invalid command identified: ")
        print(invalid_command)
        if invalid_command==invalid_commands[i]:
            print("Correct command identified as invalid.")
        else:
            print("Test failed: incorrect command identified as invalid.")
            print("Invalid command should have been identified as:")
            print(invalid_commands[i])
            break
    else:
        process_input(invalid_input_list[i].split())
        print_cube()
        print("Test failed: processed input that contained invalid command.")
        print("Invalid command should have been identified as:")
        print(invalid_commands[i])
        break
