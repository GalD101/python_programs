import time
from secret_pass import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    preceding = ""
    trailing = "000"
    counter = 0
    real_pass = []
    for j in range(4): # pylint: disable = unused-variable
        for i in range(10):
            password_attempt = preceding + str(i) + trailing
            start = time.time()
            check_password(password_attempt)
            end = time.time()
            if (end - start) >= 0.2 + counter:
                counter += 0.1
                preceding += str(i)
                trailing = trailing[:-1]
                real_pass.append(i)
                break

    real_pass.append(0)
    while(not check_password(real_pass)):
        real_pass.append((real_pass.pop() + 1))

    

    converted_array_pass = [str(number) for number in real_pass]
    final_pass = "".join(converted_array_pass)

    return final_pass

print(crack_password())