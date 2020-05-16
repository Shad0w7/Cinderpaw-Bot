# ships.py

def ship(n1, n2):
    name1 = n1.lower()
    name2 = n2.lower()
    shipIt = (name1, name2)
    z = -1
    # Predefined Ships

    if shipIt == ("tallstar", "jake"):
        return "100.00"
    if shipIt == ("hollyleaf", "fallenleaves"):
        return "100.00"
    if shipIt == ("holly", "fallen"):
        return "100.00"
    if shipIt == ("crowfeather", "nightcloud"):
        return "0.00"    
    if shipIt == ("leafpool", "crowfeather"):
        return "100.00"               
    if shipIt == ("tall", "jake"):
        return "100.00"
    
    # In the event that shipIt is just random:
    if z == -1:
        n1ascii = 0
        for a in name1:
            n1ascii += ord(a)
        
        n2ascii = 0
        for b in name2:
            n2ascii += ord(b)

        currentVal = n1ascii/float(n2ascii)
        x = str(currentVal)
        y = x.split('.')[1]
        if len(y) < 4:
            z = y[:len(y)]
            while len(z) < 4:
                z += '0'
        else:
            z = y[:4]
        returningVariable = "{0}{1}.{2}{3}".format(z[0], z[1], z[2], z[3])
        return returningVariable
