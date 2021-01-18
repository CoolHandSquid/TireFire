def set(var):
    if var == "Web_Portlist":
        portlist    = set_webportlist()
        return portlist
    else:
        val = input("What would you like to set the {} to?\n> ".format(var))
        return val

def set_webportlist():
    portlist = []
    port    = input("What is the a known web port?\n> ")
    while True:
        try:
            port = int(port)
            portlist.append(port)
            break
        except:
            print("That looks like bad input. Lets try again.")
            continue
    while True: 
        q1  = input("Add another port? (q if your list is complete)\n> ")
        if q1.lower() == "q":
            break
        else:
            try:
                port = int(q1)
                portlist.append(port)
                continue
            except:
                print("That looks like bad input. Lets try again.")
                continue
    return portlist
