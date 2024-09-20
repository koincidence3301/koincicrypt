import main as main_prog
import LP_Util
import solver

def main():
    wordlist = open("wordlist.txt", "r+").read()
    for page in range(0,57):
        ciphertext = LP_Util.return_page(str(page))
        lines = wordlist.split("\n")
        for line in lines:
            mode = f"Autokey with autokey key:  {line}"
            solving_attempt = solver.Attempt(ciphertext, page)
            solving_attempt.cipher_list.append(mode)
            solving_attempt.apply_autokey(line.replace("\n", ""))
            main_prog.gen_log_with_eng(solving_attempt)
            del solving_attempt

    return

if __name__ == "__main__":
    main()