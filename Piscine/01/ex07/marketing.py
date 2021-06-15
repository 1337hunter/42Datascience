import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def call_center():
    return list((set(clients) | set(participants)) - set(recipients))

def potential_clients():
    return list((set(participants) | set(recipients)) - set(clients))

def loyalty_program():
    return list((set(recipients) | set(clients)) - set(participants))

method = {}
method["call_center"] = call_center
method["potential_clients"] = call_center
method["loyalty_program"] = call_center


def main(argv):
    if len(argv) != 1 or argv[0] not in method.keys():
        raise "Wrong argument"
    my_best_variable = method[argv[0]]()
    print(my_best_variable)
    

if __name__ == '__main__':
    main(sys.argv[1:])