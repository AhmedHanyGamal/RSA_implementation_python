# e * d = 1 % phi_N
# Solves for d given e and phi_N
def __extended_euclidean_algorithm_inner(phi_n, e, operations_list):
    """
    Solves the equation 'e * d = 1 % phi_N' where e and phi_n are known and d is the desired number using extended euclidean algorithm

    NOTE: there is no defensive programming here, so please enter values that you KNOW have an answer
    """
    new_value = phi_n - (e * (phi_n // e))

    if new_value == 1:
        operations_list[0][0] = phi_n
        operations_list[0][1] = 1
        operations_list[1][0] = e
        operations_list[1][1] = phi_n // e
        return
    
    __extended_euclidean_algorithm_inner(e, new_value, operations_list)

    if operations_list[1][0] == new_value:
        operations_list[0][1] = (operations_list[1][1] * (phi_n // e)) + operations_list[0][1]
        operations_list[1][0] = phi_n
        return 'p'
    else:
        operations_list[1][1] = (operations_list[0][1] * (phi_n // e)) + operations_list[1][1]
        operations_list[0][0] = phi_n
        return 'n'



def extended_euclidean_algorithm(e, phi_n):
    """
    equation: e * d = 1 % phi_N
    Summary - uses extended euclidean algorithm on an equation of form 'e * d = 1 % phi_N' where 'e' and 'phi_N' are known, in order to get the unknown 'd'
    Args - e, phi_n both of type integer/big integer ('e' has to be a coprime to 'd', if 'e' is a prime number then that is guaranteed)
    Returns - d

    NOTE: there is no defensive programming for this function, so if e and d are not co-primes, the function will have an unexpected result (if it doesn't crash that is).
    You can easily avoid this by using a prime number as 'e'
    """
    operations_list = [[0, 0], [0, 0]]

    positive_or_negative_container = __extended_euclidean_algorithm_inner(phi_n, e, operations_list)

    if positive_or_negative_container == 'p':
        return operations_list[0][1]
    else:
        return phi_n - operations_list[1][1]