from nada_dsl import *

def nada_main():
    # Create two parties named "Party1" and "Party2"
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define two secret integer inputs from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Define one secret integer input from Party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Perform the computation: addition of the two secret integers from Party1
    sum_int = my_int1 + my_int2

    # Perform additional computation: adding the result with the secret integer from Party2
    total_sum = sum_int + my_int3

    # Return the results as outputs for both parties
    return [
        Output(sum_int, "sum_output", party1),  # Output for Party1
        Output(total_sum, "total_sum_output", party2)  # Output for Party2
    ]
