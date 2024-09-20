import argparse, datetime
import LP_Util, solver, formatter

"""
 credits:
 Emergence - Diana
 Taiiwo - LP Util (runes to latin etc)
 Smartacus - Vigenere tables
 JBO - Autokey code
"""

def gen_log(attempt):
    current = attempt.current
    cipher_list = attempt.cipher_list

    comp = "Ciphers applied:\n"
    for cipher in cipher_list:
        comp += cipher + f" on page {attempt.page_number}\n"

    comp2 = ""
    for char in current:
        comp2 += char

    comp3 = ""
    for char in comp2:
        comp3 += LP_Util.RuneToText[char]

    print(comp)
    print("\nRuneglish:  "+comp2)
    print("\nEnglish:  "+comp3)


    with open("log.txt", "a+") as f:
        f.write(f"Log written {datetime.datetime.now()}")
        f.write("\n"+comp)
        f.write("\nRuneglish:  "+comp2)
        f.write("\nEnglish:  "+comp3+"\n\n")

def gen_log_with_eng(attempt):
    current = attempt.current
    cipher_list = attempt.cipher_list

    comp = "Ciphers applied:\n"
    for cipher in cipher_list:
        comp += cipher + f" on page {attempt.page_number}\n" 

    comp2 = ""
    for char in current:
        comp2 += char

    comp3 = ""
    for char in comp2:
        comp3 += LP_Util.RuneToText[char]

    if attempt.check_english == True:
        print(comp)
        print("\nRuneglish:  "+comp2)
        print("\nEnglish:  "+comp3)

    with open("log.txt", "a+") as f:
        f.write(f"Log written {datetime.datetime.now()}")
        f.write("\n"+comp)
        f.write("\nRuneglish:  "+comp2)
        f.write("\nEnglish:  "+comp3+"\n\n")

class Handler:
    def __init__(self):
        self.version = "0.1.0"

    def handle(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "action",
            choices=["solve"],
            help="koincicrypt"
        )

        parser.add_argument("other", nargs="*")
        args = parser.parse_args()

        action = getattr(self, args.action)
        action()

    def solve(self):
        print("""
        koincicrypt:
        1)  Apply a single cipher
        2)  Chain ciphers
        3)  Attempt bruteforce
        4)  Exit 
        """)
        choice = input("> ")

        if choice == "1":
            print("""
        cipher selection:
        1)  Ceaser
        2)  Vigenere
        3)  Atbash
        4)  Totient Stream
        5)  Totient Stream derivitives
        6)  Fibonacci Stream
        7)  Fibonacci Stream derivitives
        8)  Beaufort
        9)  Inverse Geometry (as cipher)
        10) Diana
        11) Autokey
        """)
            i = input("> ")

            pagec = input("\nPlease choose a page number to apply cipher to:\n> ")
            if int(pagec) > 57 or int(pagec) < 0:
                print(f"Value: {pagec} out of 0-56 range")
                exit()
            
            ciphertext = LP_Util.return_page(pagec)

            solve_attempt = solver.Attempt(ciphertext, pagec)

            if i == "1":
                shift = input("\nPlease input a shift value:\n> ")
                solve_attempt.cipher_list.append(f"Caesar with a shift of {shift}")
                solve_attempt.apply_ceaser(shift)
            elif i == "2":
                key = input("\nPlease input a vigenere key to use:\n> ")
                solve_attempt.cipher_list.append(f"Vigenere with the key:  {key}")
                solve_attempt.apply_vigenere(key)
            elif i == "3":
                solve_attempt.cipher_list.append("Atbash")
                solve_attempt.apply_atbash()
            elif i == "4":
                solve_attempt.cipher_list.append("Totient stream")
                solve_attempt.apply_totient_stream()
            elif i == "5":
                #ciphertext = ciphers.totient_stream_derivitive(ciphertext, output_type="R")
                print("Totient Stream Derivitives not implemented yet, skipping..")
                pass
            elif i == "6":
                solve_attempt.cipher_list.append("Fibonacci stream")
                solve_attempt.apply_fib_stream()
            elif i == "7":
                #solve_attempt.cipher_list.append("Fibonacci stream derivitive")
                #ciphertext = ciphers.fibonacci_stream_derivitive(ciphertext, output_type="R")
                print("Fibonacci stream derivitives not implemented yet, skipping..")
            elif i == "8":
                key = input("\nPlease input a beaufort key to use:\n> ")
                solve_attempt.cipher_list.append(f"Beaufort with the key of {key}")
                solve_attempt.apply_beaufort(key)
            elif i == "9":
                solve_attempt.cipher_list.append("Inverse Geometry")
                solve_attempt.apply_inverse_geometry()
            elif i == "10":
                key = input("\nPlease input a diana key to use:\n> ")
                solve_attempt.cipher_list.append(f"Diana with the key {key}")
                solve_attempt.apply_diana(key)
            elif i == "11":
                key = input("\nPlease input a autokey key to use:\n> ")
                solve_attempt.cipher_list.append(f"Autokey with the key of {key}")
                solve_attempt.apply_autokey(key)
            else:
                print(f"Invalid cipher choice: {i}")
                exit()
            
            gen_log(solve_attempt)

        elif choice == "2":
            print("""
        cipher selection:
        1)  Ceaser
        2)  Vigenere
        3)  Atbash
        4)  Totient Stream
        5)  Totient Stream derivitives
        6)  Fibonacci Stream
        7)  Fibonacci Stream derivitives
        8)  Beaufort
        9)  Inverse Geometry (as cipher)
        10) Diana Cipher
        11) Autokey
                  
        Please input multiple ciphers like this example:  '1,2,1,4,4,4,6,9,1'.  If you enter an invalid cipher it will exit and not reurn anything.
        """)
            choice = input("> ")

            allowed = "1234567890,"
            for char in choice:
                if char not in allowed:
                    exit()
            
            pagec = input("\nPlease choose a page number to apply cipher to:\n> ")
            if int(pagec) > 57 or int(pagec) < 0:
                print(f"Value: {pagec} out of 0-56 range")
                exit()
            ciphertext = LP_Util.return_page(pagec)

            solve_attempt = solver.Attempt(ciphertext, pagec)
            print(f"Solving attempt started on page {pagec}:\n\n{solve_attempt.orig}")

            cipher_list = choice.split(",")
            for i in cipher_list:
                if i == "1":
                    shift = input("\nPlease input a shift value:\n> ")
                    solve_attempt.cipher_list.append(f"Caesar with a shift of {shift}")
                    solve_attempt.apply_ceaser(shift)
                elif i == "2":
                    key = input("\nPlease input a vigenere key to use:\n> ")
                    solve_attempt.cipher_list.append(f"Vigenere with the key:  {key}")
                    solve_attempt.apply_vigenere(key)
                elif i == "3":
                    solve_attempt.cipher_list.append("Atbash")
                    solve_attempt.apply_atbash()
                elif i == "4":
                    solve_attempt.cipher_list.append("Totient stream")
                    solve_attempt.apply_totient_stream()
                elif i == "5":
                    #ciphertext = ciphers.totient_stream_derivitive(ciphertext, output_type="R")
                    print("Totient Stream Derivitives not implemented yet, skipping..")
                    pass
                elif i == "6":
                    solve_attempt.cipher_list.append("Fibonacci stream")
                    solve_attempt.apply_fib_stream()
                elif i == "7":
                    #solve_attempt.cipher_list.append("Fibonacci stream derivitive")
                    #ciphertext = ciphers.fibonacci_stream_derivitive(ciphertext, output_type="R")
                    print("Fibonacci stream derivitives not implemented yet, skipping..")
                elif i == "8":
                    key = input("\nPlease input a beaufort key to use:\n> ")
                    solve_attempt.cipher_list.append(f"Beaufort with the key of {key}")
                    solve_attempt.apply_beaufort(key)
                elif i == "9":
                    solve_attempt.cipher_list.append("Inverse Geometry")
                    solve_attempt.apply_inverse_geometry()
                elif i == "10":
                    key = input("\nPlease input a diana key to use:\n> ")
                    solve_attempt.cipher_list.append("Diana")
                    solve_attempt.apply_diana(key)
                elif i == "11":
                    key = input("\nPlease input a autokey key to use:\n> ")
                    solve_attempt.cipher_list.append("Autokey")
                    solve_attempt.apply_autokey(key)
                else:
                    print(f"Invalid cipher choice: {i}")
                    exit()
                
            gen_log(solve_attempt)
            self.solve()

if __name__ == "__main__":
    handler = Handler()
    handler.handle()