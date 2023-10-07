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


# print(extended_euclidean_algorithm(22_801_763_488_001_518_597_448_300_800_000_000_000_000, 845_100_400_152_152_934_331_135_470_251))
# print(22_801_763_488_001_518_597_448_300_800_000_000_000_000 - pair_list[0][1])
# print(f"list[0][0] = {negative_value}\nlist[0][1] = {negative_value_multiple}\nlist[1][0] = {positive_value}\npair[1][1] = {positive_value_multiple}")


# secret_number = int(input("the number that you want to send in secret: "))

# primeNumber1 = 117058850968226927947102241264110341106500019518946520685691897927746968742423827226268711882892579200524737832004365229496510797170251252881125131245460355027923690392243281479382293401367616300190850059080995202169752352803129989319972609698366806249596235449373649908548290883657499941735084033489098194499
# primeNumber2 = 178124924431670774151400417304643300998514973083714721968871324503137058577693106439249050968138529779569005955674140482164012514771005090661996120655756298660302883070053111740921100651978919639595968070283088108603228679457574774879335388685822096547192157138082684341256439279525816978923189613961138435571
# N = primeNumber1 * primeNumber2

# phi_N = (primeNumber1 - 1) * (primeNumber2 - 1)

# private_key = 15333117085851440652883649256578147043580067020938499762946070388740405821280673245807998792937815940051800878867728027768251719659541125653385438545466688042892670760674508833949850466454673795048250722673878449501233494907968771374001
# public_key = 17882211086058128329020250460871624290438370903546731110719504664879823967569598941814655444701225942449488173724898597839616882469589210381923119579725131282552933270033367006650506217781879886067953464922156033340946210779810071017103004852162341028470330685365826770224630728465360483180637856266252712294796879439982984300210206820020010739182991443417400328435420915021095552045548253115357023366284457450660352513855487777604669393122024452613471785917580218848511385506907975561463049952269275321679798345486523474515941461025180555129353611872484606635080551422292443181919462347749593121395051587709646835461


# print(f"the public key = {public_key}")

# encrypted_num = fast_power(secret_number, private_key, N)
# print(f"encrypted number = {encrypted_num}")

# decrypted_num = fast_power(encrypted_num, public_key, N)
# print(f"original number = {decrypted_num}")


# primeNum1 = 1000000000000066600000000000001
# primeNum2 = 22801763489

# phi_N = (primeNum1 - 1) * (primeNum2 - 1)

# e = 845_100_400_152_152_934_331_135_470_251


# print(extended_euclidean_algorithm(public_key, phi_N))

# extended_euclidean_algorithm(phi_N, e)
# print(f"list[0][0] = {negative_value}\nlist[0][1] = {negative_value_multiple}\nlist[1][0] = {positive_value}\npair[1][1] = {positive_value_multiple}")