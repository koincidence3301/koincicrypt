"""
 koincicrypt - an open source, all rounder LP solver.  does it solve the lp yet?  no...  will it ever?  probably not...
 author:  koincidence

 credits:
 * Emergence - supplying code for Diana cipher
 * Taiiwo - Runic-To-Latin code from the Cicada Solvers discord bot
 * Smartacus - Vig Tables and tabular recta (`modified vig table`)
"""

import LP_Util
import mathermatix
import RSA_Util
import ciphers

import argparse

class Handler:
    def handle(self):
        """Interpret the first command line argument, and redirect."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "action",
            choices=["generateps", "encryptps", "decryptps", "decryptall", "decryptpage", "encryptall", "encryptpage", "menu", "cipher"],
            help="koincicrypt",
        ) # MORE UTIL SUCH AS PGP WILL BE ADDED LATER
        parser.add_argument("other", nargs="*")
        args = parser.parse_args()

        action = getattr(self, args.action)
        action()
    
    def generateps(self):
        response = RSA_Util.generateps()
        print(response)
        exit()
    
    def encryptps(self):
        response = RSA_Util.encryptps()
        print(response)
        exit()

    def decryptps(self):
        response = RSA_Util.decryptps()
        print(response)
        exit()

    def encryptps(self):
        response = RSA_Util.encryptps()
        print(response)
        exit()

    def decryptall(self):
        response = RSA_Util.decryptall()
        print(response)
        exit()

    def decryptpage(self):
        response = RSA_Util.decryptpage()
        print(response)
        exit()
    
    def encryptall(self):
        response = RSA_Util.encryptall()
        print(response)
        exit()

    def encryptpage(self):
        response = RSA_Util.encryptpage()
        print(response)
        exit()

    def menu(self):
        print("don't do this again.  i'm warning you.  it will delete system 32 or /")
        exit()

    def cipher(self):
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
        """)
            choice = input("> ")

            pagec = input("\nPlease choose a page number to apply cipher to:\n> ")
            if int(pagec) > 57 or int(pagec) < 0:
                print(f"Value: {pagec} out of 0-56 range")
                exit()
            page_array = LP_Util.pages.split("%")
            ciphertext = page_array[int(pagec)]

            #while output_type != "R" or output_type != "L":
            output_type = input("\nPlease select an output type, (R)unes or (L)atin\n> ")

            if choice == "1":
                shift = input("\nPlease input a shift\n> ")
                response = ciphers.ceaser(ciphertext, int(shift), output_type)
                print(response)
                self.cipher()
            elif choice == "2":
                key = input("\nPlease input a key to use:\n> ")
                response = ciphers.vigenere(ciphertext, key, output_type)
                print(response)
                self.cipher()
            elif choice == "3":
                response = ciphers.atbash(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "4":
                response = ciphers.totient_stream(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "5":
                response = ciphers.totient_stream_derivitive(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "6":
                response = ciphers.fibonacci_stream(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "7":
                response = ciphers.fibonacci_stream_derivitive(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "8":
                key = input("Please input a key:\n> ")
                response = ciphers.beaufort(ciphertext, key, output_type)
                print(response)
                self.cipher()
            elif choice == "9":
                response = ciphers.inverse_geometry(ciphertext, output_type)
                print(response)
                self.cipher()
            elif choice == "10":
                key = input("Please input a key:\n> ")
                response = ciphers.diana(ciphertext, key, output_type)

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
            page_array = LP_Util.pages.split("%")
            ciphertext = page_array[int(pagec)]

            output_type = input("\nPlease select an output type, (R)unes or (L)atin\n> ")

            cipher_list = choice.split(",")
            for i in cipher_list:
                if i == "1":
                    shift = input("\nPlease input a shift value:\n> ")
                    ciphertext = ciphers.ceaser(ciphertext, int(shift), output_type="R")
                elif i == "2":
                    key = input("\nPlease input a key to use:\n> ")
                    ciphertext = ciphers.vigenere(ciphertext, key, output_type="R")
                elif i == "3":
                    ciphertext = ciphers.atbash(ciphertext, output_type="R")
                elif i == "4":
                    ciphertext = ciphers.totient_stream(ciphertext, output_type="R")
                elif i == "5":
                    #ciphertext = ciphers.totient_stream_derivitive(ciphertext, output_type="R")
                    print("Totient Stream Derivitives not implemented yet, skipping..")
                    pass
                elif i == "6":
                    ciphertext = ciphers.fibonacci_stream(ciphertext, output_type="R")
                elif i == "7":
                    ciphertext = ciphers.fibonacci_stream_derivitive(ciphertext, output_type="R")
                elif i == "8":
                    key = input("\nPlease input a key to use:\n> ")
                    ciphertext = ciphers.beaufort(ciphertext, key, output_type="R")
                elif i == "9":
                    ciphertext = ciphers.inverse_geometry(ciphertext, output_type="")
                else:
                    print(f"Invalid cipher choice: {i}")
                    exit()
                
            if output_type == "L":
                print(LP_Util.run_to_lat())
            else:
                print(ciphertext)

        exit()

if __name__ == "__main__":
    handler = Handler()
    handler.handle()
