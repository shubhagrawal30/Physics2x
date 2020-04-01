public_shared_prime = 23
public_shared_base = 5

def key(UserXSecret, UserYSecret, bool_print):
    A = (public_shared_base ** UserXSecret) % public_shared_prime
    B = (public_shared_base ** UserYSecret) % public_shared_prime
    if bool_print:
        print "Publicly Shared Prime:", public_shared_prime
        print "Publicly Shared Base:", public_shared_base
        print "Values sent over public chanel:", A, B
    KeyX = (B ** UserXSecret) % public_shared_prime
    KeyY = (A ** UserYSecret) % public_shared_prime
    if bool_print and KeyX == KeyY:
        print "Key for both users are same:", KeyX
    return KeyX
        
def attack():
    for X in range(10, 500):
        for Y in range(10, 500):
            for X1 in range(10, 500):
                for Y1 in range(10, 500):
                    if (X, Y) == (X1, Y1):
                        continue
                    if key(X, Y, False) == key(X1, Y1, False):
                        break
    print "Found!", (X, Y), (X1, Y1)