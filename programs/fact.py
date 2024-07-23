from nada_dsl import *

def nada_main():
    # Define the parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define secret integer inputs from each party
    secret_int1 = SecretInteger(Input(name="secret_int1", party=party1))
    secret_int2 = SecretInteger(Input(name="secret_int2", party=party2))

    # Check if both secret integers are equal
    are_equal = (secret_int1 == secret_int2)

    # Return the result of the verification
    return [Output(are_equal, "verification_result", party1)]