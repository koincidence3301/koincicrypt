import base64

import mathermatix
import LP_Util
import pathlib

def ExportKeypair(public_key, private_key):
    '''
    VERY SIMPLE way of storing keys, please never do this in other circumstances.  I am too lazy to do this differently
    '''
    private_key_start = "-----BEGIN RSA PRIVATE KEY-----"
    private_key_end = "-----END RSA PRIVATE KEY-----"
    private_key_b64 = base64.b64encode(bytes(str(private_key), "utf-8"))
    private_key_file = ""
    private_key_file += private_key_start + "\n\n"
    count = 0
    for char in private_key_b64.decode():
        private_key_file += char
        count += 1
        if count == 64:
            private_key_file += "\n"
            count = 0
            
    private_key_file += "\n" + private_key_end

    public_key_start = "-----BEGIN RSA PUBLIC KEY-----"
    public_key_end = "-----END RSA PUBLIC KEY-----"
    public_key_b64 = base64.b64encode(bytes(str(public_key), "utf-8"))
    public_key_file = ""
    public_key_file += public_key_start + "\n\n"
    count = 0
    for char in public_key_b64.decode():
        public_key_file += char
        count += 1
        if count == 64:
            public_key_file += "\n"
            count = 0
    public_key_file += "\n" + public_key_end

    with open("psprivate.pem", "w+") as f:
        f.write(private_key_file)
    f.close()

    with open("pspublic.pem", "w+") as f:
        f.write(public_key_file)
    f.close()

    print("Generation and exporting to pem-like key done")
    exit()

def ImportKeys():
    with open("pspublic.pem", "r") as f:
        lines = f.readlines()
        lines2 = lines[2:-1]
        
        base64str = ""
        for l in lines2:
            base64str += l.replace("\n", "")
        
        public_key = base64.b64decode(bytes(base64str, "utf-8"))    
    f.close()
    
    with open("psprivate.pem", "r") as f:
        lines = f.readlines()
        lines2 = lines[2:-1]
        
        base64str = ""
        for l in lines2:
            base64str += l.replace("\n", "")
        
        private_key = base64.b64decode(bytes(base64str, "utf-8"))
    f.close()

    return public_key, private_key

def generateps():
    '''
    Simple RSA keypair generation based on the PS message
    '''
    p = 99554414790940424414351515490472769096534141749790794321708050837
    q = 104593961812606247801193807142122161186583731774511103180935025763

    n = p*q

    phi = (p-1)*(q-1)

    e = 65537

    g = mathermatix.gcd(e, phi)

    if g == 1:
        print("Coprime!")
    else:
        print("Not coprime")
        exit()

    d = pow(e, -1, phi)

    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"

    print("Public key:  " + str(public_key))
    print("Private key:  " + str(private_key))

    ExportKeypair(public_key, private_key)

    return "Done!"

def encryptps():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    choice = input("(L)atin or (r)unic:\n> ")
    if choice.upper() != "L" and choice.upper() != "R":
        print("Invalid choice..")
        exit()
    ct = input("Please input cipher text:\n> ")
    if choice.upper() == "L":
        runic = LP_Util.lat_to_run(ct)
        base = []
        base2 = []
        for rune in runic.replace(" ", ""):
            base.append(LP_Util.RunesToGP[rune])
            base2.append(LP_Util.RunesToIndex[rune])
            
    elif choice.upper() == "R":
        base = []
        base2 = []
        for rune in ct.replace(" ", ""):
            base.append(LP_Util.RunesToGP[rune])
            base2.append(LP_Util.RunesToIndex[rune])

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : cyphertext = message^e mod n
    """
    nbase1 = []
    nbase2 = []

    for i in base:
        nbase1.append((pow(i,int(pub[0]),int(pub[1]))))
        
    for i in base2:
        nbase2.append((pow(i,int(pub[0]),int(pub[1]))))

    print("Sum Before runic translation:  " + str(nbase1))
    print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    for res in nbase1:
        nbase1str += LP_Util.IndexToRunes[res%29]

    nbase2str = ""
    for res2 in nbase2:
        nbase2str += LP_Util.IndexToRunes[res2%29]

    #this is done because i am lazy, very lazy
    nbase1str2 = ""
    for char in nbase1str:
        nbase1str2 += LP_Util.RuneToText[char] + " "

    nbase2str2 = ""
    for char2 in nbase2str:
        nbase2str2 += LP_Util.RuneToText[char2] + " "

    print("GP to Index RSA encrypt:  " + nbase1str2)
    print("Index to Index RSA encrypt:  " + nbase2str2)

    return "Done!"
        
def decryptps():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    choice = input("(L)atin or (r)unic:\n> ")
    if choice.upper() != "L" and choice.upper() != "R":
        print("Invalid choice..")
        exit()
    ct = input("Please input cipher text:\n> ")
    if choice.upper() == "L":
        runic = LP_Util.lat_to_run(ct)
        base = []
        base2 = []
        for rune in runic.replace(" ", ""):
            base.append(LP_Util.RunesToGP[rune])
            base2.append(LP_Util.RunesToIndex[rune])
            
    elif choice.upper() == "R":
        base = []
        base2 = []
        for rune in ct.replace(" ", ""):
            base.append(LP_Util.RunesToGP[rune])
            base2.append(LP_Util.RunesToIndex[rune])

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : plaintext = cyphertext^d mod n
    """
    nbase1 = []
    nbase2 = []

    for i in base:
        nbase1.append((pow(i,int(priv[0]),int(priv[1])))%29)
        
    for i in base2:
        nbase2.append((pow(i,int(priv[0]),int(priv[1])))%29)

    print("Sum Before runic translation:  " + str(nbase1))
    print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    for res in nbase1:
        nbase1str += LP_Util.IndexToRunes[res]

    nbase2str = ""
    for res2 in nbase2:
        nbase2str += LP_Util.IndexToRunes[res2]

    #this is done because i am lazy, very lazy
        
    nbase1str2 = ""
    for char in nbase1str:
        nbase1str2 += LP_Util.RuneToText[char] + " "

    nbase2str2 = ""
    for char2 in nbase2str:
        nbase2str2 += LP_Util.RuneToText[char2] + " "

    print("GP to Index RSA decrypt:  " + nbase1str2)
    print("Index to Index RSA decrypt:  " + nbase2str2)

    return "Done!"
        
def decryptall():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : plaintext = cyphertext^d mod n
    """
    nbase1 = ""
    nbase12 = []
    nbase2 = ""
    nbase22 = []

    npages = LP_Util.pages.replace("&", "\n").replace("%", "\n").replace("$", "\n").replace("/", "")

    disallowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in npages:
        if i == " ":
            nbase1 += " "
            nbase12.append(" ")
        elif i == "\n":
            nbase1 += "\n"
            nbase12.append("\n")
        elif i == ".":
            nbase1 += "."
            nbase12.append(".")
        elif i in disallowed:
            nbase1 += "!"
            nbase12.append("!")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase1 += "!"
            nbase12.append("!")
        else:
            curr = LP_Util.RunesToGP[i]
            nbase1+=str(((pow(curr,int(priv[0]),int(priv[1])))%29))
            nbase12.append(((pow(curr,int(priv[0]),int(priv[1])))%29))
        
    for i in npages:
        if i == " ":
            nbase2 += " "
            nbase22.append(" ")
        elif i == "\n":
            nbase2 += "\n"
            nbase22.append("\n")
        elif i == ".":
            nbase2 += "."
            nbase22.append(".")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase2 += "!"
            nbase22.append("!")
        elif i in disallowed:
            nbase2 += "!"
            nbase22.append("!")
        else:
            curr = LP_Util.RunesToIndex[i]
            nbase2+=str(((pow(curr,int(priv[0]),int(priv[1])))%29))
            nbase22.append(str(((pow(curr,int(priv[0]),int(priv[1])))%29)))
                

    #print("Sum Before runic translation:  " + str(nbase1))
    #print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    nbase11str = ""
    for i in nbase12:
        if i == " ":
            nbase1str += " "
            nbase11str += " "
        elif i == "\n":
            nbase1str += "\n"
            nbase11str += "\n"
        elif i == ".":
            nbase1str += "."
            nbase11str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase1str += nrune
            nbase11str += LP_Util.RuneToText[nrune]

    nbase2str = ""
    nbase22str = ""
    for i in nbase22:
        if i == " ":
            nbase2str += " "
            nbase22str += " "
        elif i == "\n":
            nbase2str += "\n"
            nbase22str += "\n"
        elif i == ".":
            nbase2str += "."
            nbase22str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase2str += nrune
            nbase22str += LP_Util.RuneToText[nrune]

    #this is done because i am lazy, very lazy
                
        
                
    with open("resultsdecrypt.txt", "w+", encoding="utf-8") as f:
        f.write("LP FULL RSA DECRYPT USING GP SUM - Latin output\n")
        f.write("-----------------------------------------------")
        f.write(nbase11str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA DECRYPT USING GP SUM - Runic output\n")
        f.write("-----------------------------------------------")
        f.write(nbase1str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA DECRYPT USING INDEX - Latin output\n")
        f.write("-----------------------------------------------")
        f.write(nbase22str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA DECRYPT USING INDEX - Runic output\n")
        f.write("----------------------------------------------")
        f.write(nbase2str)
        f.write("\n\n\n\n\n")
    f.close()

    print("Due to the output being nearly 5k lines, we have written the results to resultsdecrypt.txt")
    return "Done!"

def decryptpage():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : plaintext = cyphertext^d mod n
    """
    nbase1 = ""
    nbase12 = []
    nbase2 = ""
    nbase22 = []

    npages = LP_Util.pages.replace("&", "\n").replace("/", "").replace("$", "\n")

    disallowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    whichpage = input("Which page would you like to decrypt with RSA?\n> ")

    npages2 = npages.split("%")

    for i in npages2[int(whichpage)]:
        if i == " ":
            nbase1 += " "
            nbase12.append(" ")
        elif i == "\n":
            nbase1 += "\n"
            nbase12.append("\n")
        elif i == ".":
            nbase1 += "."
            nbase12.append(".")
        elif i in disallowed:
            nbase1 += "!"
            nbase12.append("!")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase1 += "!"
            nbase12.append("!")
        else:
            curr = LP_Util.RunesToGP[i]
            nbase1+=str(((pow(curr,int(priv[0]),int(priv[1])))%29))
            nbase12.append(((pow(curr,int(priv[0]),int(priv[1])))%29))
        
    for i in npages2[int(whichpage)]:
        if i == " ":
            nbase2 += " "
            nbase22.append(" ")
        elif i == "\n":
            nbase2 += "\n"
            nbase22.append("\n")
        elif i == ".":
            nbase2 += "."
            nbase22.append(".")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase2 += "!"
            nbase22.append("!")
        elif i in disallowed:
            nbase2 += "!"
            nbase22.append("!")
        else:
            curr = LP_Util.RunesToIndex[i]
            nbase2+=str(((pow(curr,int(priv[0]),int(priv[1])))%29))
            nbase22.append(str(((pow(curr,int(priv[0]),int(priv[1])))%29)))
                

    #print("Sum Before runic translation:  " + str(nbase1))
    #print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    nbase11str = ""
    for i in nbase12:
        if i == " ":
            nbase1str += " "
            nbase11str += " "
        elif i == "\n":
            nbase1str += "\n"
            nbase11str += "\n"
        elif i == ".":
            nbase1str += "."
            nbase11str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase1str += nrune
            nbase11str += LP_Util.RuneToText[nrune]

    nbase2str = ""
    nbase22str = ""
    for i in nbase22:
        if i == " ":
            nbase2str += " "
            nbase22str += " "
        elif i == "\n":
            nbase2str += "\n"
            nbase22str += "\n"
        elif i == ".":
            nbase2str += "."
            nbase22str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase2str += nrune
            nbase22str += LP_Util.RuneToText[nrune]

    print("GP Sum base:")
    print("Runic:\n" + nbase1str)
    print("Latin:\n" + nbase11str)
    print("\nIndex base:")
    print("Runic:\n" + nbase2str)
    print("Latin:\n" + nbase22str)
    return "Done!"

def encryptall():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : cyphertext = message^e mod n
    """
    nbase1 = ""
    nbase12 = []
    nbase2 = ""
    nbase22 = []

    npages = LP_Util.pages.replace("&", "\n").replace("%", "\n").replace("$", "\n").replace("/", "")

    disallowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in npages:
        if i == " ":
            nbase1 += " "
            nbase12.append(" ")
        elif i == "\n":
            nbase1 += "\n"
            nbase12.append("\n")
        elif i == ".":
            nbase1 += "."
            nbase12.append(".")
        elif i in disallowed:
            nbase1 += "!"
            nbase12.append("!")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase1 += "!"
            nbase12.append("!")
        else:
            curr = LP_Util.RunesToGP[i]
            nbase1+=str(((pow(curr,int(pub[0]),int(pub[1])))%29))
            nbase12.append(((pow(curr,int(pub[0]),int(pub[1])))%29))
        
    for i in npages:
        if i == " ":
            nbase2 += " "
            nbase22.append(" ")
        elif i == "\n":
            nbase2 += "\n"
            nbase22.append("\n")
        elif i == ".":
            nbase2 += "."
            nbase22.append(".")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase2 += "!"
            nbase22.append("!")
        elif i in disallowed:
            nbase2 += "!"
            nbase22.append("!")
        else:
            curr = LP_Util.RunesToIndex[i]
            nbase2+=str(((pow(curr,int(pub[0]),int(pub[1])))%29))
            nbase22.append(str(((pow(curr,int(pub[0]),int(pub[1])))%29)))
                

    #print("Sum Before runic translation:  " + str(nbase1))
    #print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    nbase11str = ""
    for i in nbase12:
        if i == " ":
            nbase1str += " "
            nbase11str += " "
        elif i == "\n":
            nbase1str += "\n"
            nbase11str += "\n"
        elif i == ".":
            nbase1str += "."
            nbase11str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase1str += nrune
            nbase11str += LP_Util.RuneToText[nrune]

    nbase2str = ""
    nbase22str = ""
    for i in nbase22:
        if i == " ":
            nbase2str += " "
            nbase22str += " "
        elif i == "\n":
            nbase2str += "\n"
            nbase22str += "\n"
        elif i == ".":
            nbase2str += "."
            nbase22str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase2str += nrune
            nbase22str += LP_Util.RuneToText[nrune]

        #this is done because i am lazy, very lazy
                
        
                
    with open("resultsencrypt.txt", "w+", encoding="utf-8") as f:
        f.write("LP FULL RSA ENCRYPT USING GP SUM - Latin output\n")
        f.write("-----------------------------------------------")
        f.write(nbase11str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA ENCRYPT USING GP SUM - Runic output\n")
        f.write("-----------------------------------------------")
        f.write(nbase1str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA ENCRYPT USING INDEX - Latin output\n")
        f.write("-----------------------------------------------")
        f.write(nbase22str)
        f.write("\n\n\n\n\n")
        f.write("LP FULL RSA ENCRYPT USING INDEX - Runic output\n")
        f.write("----------------------------------------------")
        f.write(nbase2str)
        f.write("\n\n\n\n\n")
    f.close()

    print("Due to the output being nearly 5k lines, we have written the results to resultsencrypt.txt")
    return "Done!"

def encryptpage():
    pubfile = pathlib.Path("./assets/pspublic.pem")
    privfile = pathlib.Path("./psprivate.pem")

    if not pubfile.is_file():
        print("Keys not found, generate them")
        exit()

    if not privfile.is_file():
        print("Keys not found, generate them")
        exit()

    public, private = ImportKeys()
    epublic = public.decode()
    eprivate = private.decode()
        
    pub = epublic.split(":")
    priv = eprivate.split(":")
    """
    public_key = f"{e}:{n}"
    private_key = f"{d}:{n}"
    formula : plaintext = cyphertext^d mod n
    """
    nbase1 = ""
    nbase12 = []
    nbase2 = ""
    nbase22 = []

    npages = LP_Util.pages.replace("&", "\n").replace("/", "").replace("$", "\n")

    disallowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    whichpage = input("Which page would you like to decrypt with RSA?\n> ")

    npages2 = npages.split("%")

    for i in npages2[int(whichpage)]:
        if i == " ":
            nbase1 += " "
            nbase12.append(" ")
        elif i == "\n":
            nbase1 += "\n"
            nbase12.append("\n")
        elif i == ".":
            nbase1 += "."
            nbase12.append(".")
        elif i in disallowed:
            nbase1 += "!"
            nbase12.append("!")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase1 += "!"
            nbase12.append("!")
        else:
            curr = LP_Util.RunesToGP[i]
            nbase1+=str(((pow(curr,int(pub[0]),int(pub[1])))%29))
            nbase12.append(((pow(curr,int(pub[0]),int(pub[1])))%29))
        
    for i in npages2[int(whichpage)]:
        if i == " ":
            nbase2 += " "
            nbase22.append(" ")
        elif i == "\n":
            nbase2 += "\n"
            nbase22.append("\n")
        elif i == ".":
            nbase2 += "."
            nbase22.append(".")
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            nbase2 += "!"
            nbase22.append("!")
        elif i in disallowed:
            nbase2 += "!"
            nbase22.append("!")
        else:
            curr = LP_Util.RunesToIndex[i]
            nbase2+=str(((pow(curr,int(pub[0]),int(pub[1])))%29))
            nbase22.append(str(((pow(curr,int(pub[0]),int(pub[1])))%29)))
                

    #print("Sum Before runic translation:  " + str(nbase1))
    #print("Index Before runic translation:  " + str(nbase2))

    nbase1str = ""
    nbase11str = ""
    for i in nbase12:
        if i == " ":
            nbase1str += " "
            nbase11str += " "
        elif i == "\n":
            nbase1str += "\n"
            nbase11str += "\n"
        elif i == ".":
            nbase1str += "."
            nbase11str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase1str += nrune
            nbase11str += LP_Util.RuneToText[nrune]

    nbase2str = ""
    nbase22str = ""
    for i in nbase22:
        if i == " ":
            nbase2str += " "
            nbase22str += " "
        elif i == "\n":
            nbase2str += "\n"
            nbase22str += "\n"
        elif i == ".":
            nbase2str += "."
            nbase22str += "."
        elif i == "!":
            pass
        else:
            nrune = LP_Util.IndexToRunes[int(i)]
            nbase2str += nrune
            nbase22str += LP_Util.RuneToText[nrune]

    print("GP Sum base:")
    print("Runic:\n" + nbase1str)
    print("Latin:\n" + nbase11str)
    print("\nIndex base:")
    print("Runic:\n" + nbase2str)
    print("Latin:\n" + nbase22str)

    return "Done!"