#function to verify if test cases pass
def verify_test(cube_state, expected_state):
    if expected_state==cube_state:
        print("Test passed. Cube displays correctly.")
        return True
    else:
        print("Test failed. Correct cube state should be:")
        print(expected_state)
        print("Current state is:")
        print(cube_state)
        return False
