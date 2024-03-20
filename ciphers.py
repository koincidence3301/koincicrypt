import LP_Util
import mathermatix
import re

"""
 koincicrypt - ciphers file for applying ciphers to the runes found in the LP
 author:  koincidence
 
 credits:
 * Emergence - supplying code for Diana cipher
 * Taiiwo - Runic-To-Latin code 
 * Smartacus - Vig Tables and tabular recta (`modified vig table`)
"""

atbash_enc = {'ᚠ': 'ᛠ', 'ᚢ': 'ᛡ', 'ᚦ': 'ᚣ', 'ᚩ': 'ᚫ', 'ᚱ': 'ᚪ', 'ᚳ': 'ᛞ', 'ᚷ': 'ᛟ', 'ᚹ': 'ᛝ', 'ᚻ': 'ᛚ', 'ᚾ': 'ᛗ', 'ᛁ': 'ᛖ', 'ᛄ': 'ᛒ', 'ᛇ': 'ᛏ', 'ᛈ': 'ᛋ', 'ᛉ': 'ᛉ', 'ᛋ': 'ᛈ', 'ᛏ': 'ᛇ', 'ᛒ': 'ᛄ', 'ᛖ': 'ᛁ', 'ᛗ': 'ᚾ', 'ᛚ': 'ᚻ', 'ᛝ': 'ᚹ', 'ᛟ': 'ᚷ', 'ᛞ': 'ᚳ', 'ᚪ': 'ᚱ', 'ᚫ': 'ᚩ', 'ᚣ': 'ᚦ', 'ᛡ': 'ᚢ', 'ᛠ': 'ᚠ'}

disallowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-"

alphabet = "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ"

def check_latin(text):
    result = re.sub("[A-Za-z0-9]", '', text)
    if len(result) == 0:
        return True
    else:
        return False
    
# Diana stuff goes here
F_DIANA = {'ᛠ': 'ᚠ', 'ᛡ': 'ᚢ', 'ᚣ': 'ᚦ', 'ᚫ': 'ᚩ', 'ᚪ': 'ᚱ', 'ᛞ': 'ᚳ', 'ᛟ': 'ᚷ', 'ᛝ': 'ᚹ', 'ᛚ': 'ᚻ', 'ᛗ': 'ᚾ', 'ᛖ': 'ᛁ', 'ᛒ': 'ᛄ', 'ᛏ': 'ᛇ', 'ᛋ': 'ᛈ', 'ᛉ': 'ᛉ', 'ᛈ': 'ᛋ', 'ᛇ': 'ᛏ', 'ᛄ': 'ᛒ', 'ᛁ': 'ᛖ', 'ᚾ': 'ᛗ', 'ᚻ': 'ᛚ', 'ᚹ': 'ᛝ', 'ᚷ': 'ᛟ', 'ᚳ': 'ᛞ', 'ᚱ': 'ᚪ', 'ᚩ': 'ᚫ', 'ᚦ': 'ᚣ', 'ᚢ': 'ᛡ', 'ᚠ': 'ᛠ'}
U_DIANA = {'ᛡ': 'ᚠ', 'ᚣ': 'ᚢ', 'ᚫ': 'ᚦ', 'ᚪ': 'ᚩ', 'ᛞ': 'ᚱ', 'ᛟ': 'ᚳ', 'ᛝ': 'ᚷ', 'ᛚ': 'ᚹ', 'ᛗ': 'ᚻ', 'ᛖ': 'ᚾ', 'ᛒ': 'ᛁ', 'ᛏ': 'ᛄ', 'ᛋ': 'ᛇ', 'ᛉ': 'ᛈ', 'ᛈ': 'ᛉ', 'ᛇ': 'ᛋ', 'ᛄ': 'ᛏ', 'ᛁ': 'ᛒ', 'ᚾ': 'ᛖ', 'ᚻ': 'ᛗ', 'ᚹ': 'ᛚ', 'ᚷ': 'ᛝ', 'ᚳ': 'ᛟ', 'ᚱ': 'ᛞ', 'ᚩ': 'ᚪ', 'ᚦ': 'ᚫ', 'ᚢ': 'ᚣ', 'ᚠ': 'ᛡ', 'ᛠ': 'ᛠ'}
TH_DIANA = {'ᚣ': 'ᚠ', 'ᚫ': 'ᚢ', 'ᚪ': 'ᚦ', 'ᛞ': 'ᚩ', 'ᛟ': 'ᚱ', 'ᛝ': 'ᚳ', 'ᛚ': 'ᚷ', 'ᛗ': 'ᚹ', 'ᛖ': 'ᚻ', 'ᛒ': 'ᚾ', 'ᛏ': 'ᛁ', 'ᛋ': 'ᛄ', 'ᛉ': 'ᛇ', 'ᛈ': 'ᛈ', 'ᛇ': 'ᛉ', 'ᛄ': 'ᛋ', 'ᛁ': 'ᛏ', 'ᚾ': 'ᛒ', 'ᚻ': 'ᛖ', 'ᚹ': 'ᛗ', 'ᚷ': 'ᛚ', 'ᚳ': 'ᛝ', 'ᚱ': 'ᛟ', 'ᚩ': 'ᛞ', 'ᚦ': 'ᚪ', 'ᚢ': 'ᚫ', 'ᚠ': 'ᚣ', 'ᛠ': 'ᛡ', 'ᛡ': 'ᛠ'}
O_DIANA = {'ᚫ': 'ᚠ', 'ᚪ': 'ᚢ', 'ᛞ': 'ᚦ', 'ᛟ': 'ᚩ', 'ᛝ': 'ᚱ', 'ᛚ': 'ᚳ', 'ᛗ': 'ᚷ', 'ᛖ': 'ᚹ', 'ᛒ': 'ᚻ', 'ᛏ': 'ᚾ', 'ᛋ': 'ᛁ', 'ᛉ': 'ᛄ', 'ᛈ': 'ᛇ', 'ᛇ': 'ᛈ', 'ᛄ': 'ᛉ', 'ᛁ': 'ᛋ', 'ᚾ': 'ᛏ', 'ᚻ': 'ᛒ', 'ᚹ': 'ᛖ', 'ᚷ': 'ᛗ', 'ᚳ': 'ᛚ', 'ᚱ': 'ᛝ', 'ᚩ': 'ᛟ', 'ᚦ': 'ᛞ', 'ᚢ': 'ᚪ', 'ᚠ': 'ᚫ', 'ᛠ': 'ᚣ', 'ᛡ': 'ᛡ', 'ᚣ': 'ᛠ'}
R_DIANA = {'ᚪ': 'ᚠ', 'ᛞ': 'ᚢ', 'ᛟ': 'ᚦ', 'ᛝ': 'ᚩ', 'ᛚ': 'ᚱ', 'ᛗ': 'ᚳ', 'ᛖ': 'ᚷ', 'ᛒ': 'ᚹ', 'ᛏ': 'ᚻ', 'ᛋ': 'ᚾ', 'ᛉ': 'ᛁ', 'ᛈ': 'ᛄ', 'ᛇ': 'ᛇ', 'ᛄ': 'ᛈ', 'ᛁ': 'ᛉ', 'ᚾ': 'ᛋ', 'ᚻ': 'ᛏ', 'ᚹ': 'ᛒ', 'ᚷ': 'ᛖ', 'ᚳ': 'ᛗ', 'ᚱ': 'ᛚ', 'ᚩ': 'ᛝ', 'ᚦ': 'ᛟ', 'ᚢ': 'ᛞ', 'ᚠ': 'ᚪ', 'ᛠ': 'ᚫ', 'ᛡ': 'ᚣ', 'ᚣ': 'ᛡ', 'ᚫ': 'ᛠ'}
C_DIANA = {'ᛞ': 'ᚠ', 'ᛟ': 'ᚢ', 'ᛝ': 'ᚦ', 'ᛚ': 'ᚩ', 'ᛗ': 'ᚱ', 'ᛖ': 'ᚳ', 'ᛒ': 'ᚷ', 'ᛏ': 'ᚹ', 'ᛋ': 'ᚻ', 'ᛉ': 'ᚾ', 'ᛈ': 'ᛁ', 'ᛇ': 'ᛄ', 'ᛄ': 'ᛇ', 'ᛁ': 'ᛈ', 'ᚾ': 'ᛉ', 'ᚻ': 'ᛋ', 'ᚹ': 'ᛏ', 'ᚷ': 'ᛒ', 'ᚳ': 'ᛖ', 'ᚱ': 'ᛗ', 'ᚩ': 'ᛚ', 'ᚦ': 'ᛝ', 'ᚢ': 'ᛟ', 'ᚠ': 'ᛞ', 'ᛠ': 'ᚪ', 'ᛡ': 'ᚫ', 'ᚣ': 'ᚣ', 'ᚫ': 'ᛡ', 'ᚪ': 'ᛠ'}
G_DIANA = {'ᛟ': 'ᚠ', 'ᛝ': 'ᚢ', 'ᛚ': 'ᚦ', 'ᛗ': 'ᚩ', 'ᛖ': 'ᚱ', 'ᛒ': 'ᚳ', 'ᛏ': 'ᚷ', 'ᛋ': 'ᚹ', 'ᛉ': 'ᚻ', 'ᛈ': 'ᚾ', 'ᛇ': 'ᛁ', 'ᛄ': 'ᛄ', 'ᛁ': 'ᛇ', 'ᚾ': 'ᛈ', 'ᚻ': 'ᛉ', 'ᚹ': 'ᛋ', 'ᚷ': 'ᛏ', 'ᚳ': 'ᛒ', 'ᚱ': 'ᛖ', 'ᚩ': 'ᛗ', 'ᚦ': 'ᛚ', 'ᚢ': 'ᛝ', 'ᚠ': 'ᛟ', 'ᛠ': 'ᛞ', 'ᛡ': 'ᚪ', 'ᚣ': 'ᚫ', 'ᚫ': 'ᚣ', 'ᚪ': 'ᛡ', 'ᛞ': 'ᛠ'}
W_DIANA = {'ᛝ': 'ᚠ', 'ᛚ': 'ᚢ', 'ᛗ': 'ᚦ', 'ᛖ': 'ᚩ', 'ᛒ': 'ᚱ', 'ᛏ': 'ᚳ', 'ᛋ': 'ᚷ', 'ᛉ': 'ᚹ', 'ᛈ': 'ᚻ', 'ᛇ': 'ᚾ', 'ᛄ': 'ᛁ', 'ᛁ': 'ᛄ', 'ᚾ': 'ᛇ', 'ᚻ': 'ᛈ', 'ᚹ': 'ᛉ', 'ᚷ': 'ᛋ', 'ᚳ': 'ᛏ', 'ᚱ': 'ᛒ', 'ᚩ': 'ᛖ', 'ᚦ': 'ᛗ', 'ᚢ': 'ᛚ', 'ᚠ': 'ᛝ', 'ᛠ': 'ᛟ', 'ᛡ': 'ᛞ', 'ᚣ': 'ᚪ', 'ᚫ': 'ᚫ', 'ᚪ': 'ᚣ', 'ᛞ': 'ᛡ', 'ᛟ': 'ᛠ'}
H_DIANA = {'ᛚ': 'ᚠ', 'ᛗ': 'ᚢ', 'ᛖ': 'ᚦ', 'ᛒ': 'ᚩ', 'ᛏ': 'ᚱ', 'ᛋ': 'ᚳ', 'ᛉ': 'ᚷ', 'ᛈ': 'ᚹ', 'ᛇ': 'ᚻ', 'ᛄ': 'ᚾ', 'ᛁ': 'ᛁ', 'ᚾ': 'ᛄ', 'ᚻ': 'ᛇ', 'ᚹ': 'ᛈ', 'ᚷ': 'ᛉ', 'ᚳ': 'ᛋ', 'ᚱ': 'ᛏ', 'ᚩ': 'ᛒ', 'ᚦ': 'ᛖ', 'ᚢ': 'ᛗ', 'ᚠ': 'ᛚ', 'ᛠ': 'ᛝ', 'ᛡ': 'ᛟ', 'ᚣ': 'ᛞ', 'ᚫ': 'ᚪ', 'ᚪ': 'ᚫ', 'ᛞ': 'ᚣ', 'ᛟ': 'ᛡ', 'ᛝ': 'ᛠ'}
N_DIANA = {'ᛗ': 'ᚠ', 'ᛖ': 'ᚢ', 'ᛒ': 'ᚦ', 'ᛏ': 'ᚩ', 'ᛋ': 'ᚱ', 'ᛉ': 'ᚳ', 'ᛈ': 'ᚷ', 'ᛇ': 'ᚹ', 'ᛄ': 'ᚻ', 'ᛁ': 'ᚾ', 'ᚾ': 'ᛁ', 'ᚻ': 'ᛄ', 'ᚹ': 'ᛇ', 'ᚷ': 'ᛈ', 'ᚳ': 'ᛉ', 'ᚱ': 'ᛋ', 'ᚩ': 'ᛏ', 'ᚦ': 'ᛒ', 'ᚢ': 'ᛖ', 'ᚠ': 'ᛗ', 'ᛠ': 'ᛚ', 'ᛡ': 'ᛝ', 'ᚣ': 'ᛟ', 'ᚫ': 'ᛞ', 'ᚪ': 'ᚪ', 'ᛞ': 'ᚫ', 'ᛟ': 'ᚣ', 'ᛝ': 'ᛡ', 'ᛚ': 'ᛠ'}
I_DIANA = {'ᛖ': 'ᚠ', 'ᛒ': 'ᚢ', 'ᛏ': 'ᚦ', 'ᛋ': 'ᚩ', 'ᛉ': 'ᚱ', 'ᛈ': 'ᚳ', 'ᛇ': 'ᚷ', 'ᛄ': 'ᚹ', 'ᛁ': 'ᚻ', 'ᚾ': 'ᚾ', 'ᚻ': 'ᛁ', 'ᚹ': 'ᛄ', 'ᚷ': 'ᛇ', 'ᚳ': 'ᛈ', 'ᚱ': 'ᛉ', 'ᚩ': 'ᛋ', 'ᚦ': 'ᛏ', 'ᚢ': 'ᛒ', 'ᚠ': 'ᛖ', 'ᛠ': 'ᛗ', 'ᛡ': 'ᛚ', 'ᚣ': 'ᛝ', 'ᚫ': 'ᛟ', 'ᚪ': 'ᛞ', 'ᛞ': 'ᚪ', 'ᛟ': 'ᚫ', 'ᛝ': 'ᚣ', 'ᛚ': 'ᛡ', 'ᛗ': 'ᛠ'}
J_DIANA = {'ᛒ': 'ᚠ', 'ᛏ': 'ᚢ', 'ᛋ': 'ᚦ', 'ᛉ': 'ᚩ', 'ᛈ': 'ᚱ', 'ᛇ': 'ᚳ', 'ᛄ': 'ᚷ', 'ᛁ': 'ᚹ', 'ᚾ': 'ᚻ', 'ᚻ': 'ᚾ', 'ᚹ': 'ᛁ', 'ᚷ': 'ᛄ', 'ᚳ': 'ᛇ', 'ᚱ': 'ᛈ', 'ᚩ': 'ᛉ', 'ᚦ': 'ᛋ', 'ᚢ': 'ᛏ', 'ᚠ': 'ᛒ', 'ᛠ': 'ᛖ', 'ᛡ': 'ᛗ', 'ᚣ': 'ᛚ', 'ᚫ': 'ᛝ', 'ᚪ': 'ᛟ', 'ᛞ': 'ᛞ', 'ᛟ': 'ᚪ', 'ᛝ': 'ᚫ', 'ᛚ': 'ᚣ', 'ᛗ': 'ᛡ', 'ᛖ': 'ᛠ'}
EO_DIANA = {'ᛏ': 'ᚠ', 'ᛋ': 'ᚢ', 'ᛉ': 'ᚦ', 'ᛈ': 'ᚩ', 'ᛇ': 'ᚱ', 'ᛄ': 'ᚳ', 'ᛁ': 'ᚷ', 'ᚾ': 'ᚹ', 'ᚻ': 'ᚻ', 'ᚹ': 'ᚾ', 'ᚷ': 'ᛁ', 'ᚳ': 'ᛄ', 'ᚱ': 'ᛇ', 'ᚩ': 'ᛈ', 'ᚦ': 'ᛉ', 'ᚢ': 'ᛋ', 'ᚠ': 'ᛏ', 'ᛠ': 'ᛒ', 'ᛡ': 'ᛖ', 'ᚣ': 'ᛗ', 'ᚫ': 'ᛚ', 'ᚪ': 'ᛝ', 'ᛞ': 'ᛟ', 'ᛟ': 'ᛞ', 'ᛝ': 'ᚪ', 'ᛚ': 'ᚫ', 'ᛗ': 'ᚣ', 'ᛖ': 'ᛡ', 'ᛒ': 'ᛠ'}
P_DIANA = {'ᛋ': 'ᚠ', 'ᛉ': 'ᚢ', 'ᛈ': 'ᚦ', 'ᛇ': 'ᚩ', 'ᛄ': 'ᚱ', 'ᛁ': 'ᚳ', 'ᚾ': 'ᚷ', 'ᚻ': 'ᚹ', 'ᚹ': 'ᚻ', 'ᚷ': 'ᚾ', 'ᚳ': 'ᛁ', 'ᚱ': 'ᛄ', 'ᚩ': 'ᛇ', 'ᚦ': 'ᛈ', 'ᚢ': 'ᛉ', 'ᚠ': 'ᛋ', 'ᛠ': 'ᛏ', 'ᛡ': 'ᛒ', 'ᚣ': 'ᛖ', 'ᚫ': 'ᛗ', 'ᚪ': 'ᛚ', 'ᛞ': 'ᛝ', 'ᛟ': 'ᛟ', 'ᛝ': 'ᛞ', 'ᛚ': 'ᚪ', 'ᛗ': 'ᚫ', 'ᛖ': 'ᚣ', 'ᛒ': 'ᛡ', 'ᛏ': 'ᛠ'}
X_DIANA = {'ᛉ': 'ᚠ', 'ᛈ': 'ᚢ', 'ᛇ': 'ᚦ', 'ᛄ': 'ᚩ', 'ᛁ': 'ᚱ', 'ᚾ': 'ᚳ', 'ᚻ': 'ᚷ', 'ᚹ': 'ᚹ', 'ᚷ': 'ᚻ', 'ᚳ': 'ᚾ', 'ᚱ': 'ᛁ', 'ᚩ': 'ᛄ', 'ᚦ': 'ᛇ', 'ᚢ': 'ᛈ', 'ᚠ': 'ᛉ', 'ᛠ': 'ᛋ', 'ᛡ': 'ᛏ', 'ᚣ': 'ᛒ', 'ᚫ': 'ᛖ', 'ᚪ': 'ᛗ', 'ᛞ': 'ᛚ', 'ᛟ': 'ᛝ', 'ᛝ': 'ᛟ', 'ᛚ': 'ᛞ', 'ᛗ': 'ᚪ', 'ᛖ': 'ᚫ', 'ᛒ': 'ᚣ', 'ᛏ': 'ᛡ', 'ᛋ': 'ᛠ'}
S_DIANA = {'ᛈ': 'ᚠ', 'ᛇ': 'ᚢ', 'ᛄ': 'ᚦ', 'ᛁ': 'ᚩ', 'ᚾ': 'ᚱ', 'ᚻ': 'ᚳ', 'ᚹ': 'ᚷ', 'ᚷ': 'ᚹ', 'ᚳ': 'ᚻ', 'ᚱ': 'ᚾ', 'ᚩ': 'ᛁ', 'ᚦ': 'ᛄ', 'ᚢ': 'ᛇ', 'ᚠ': 'ᛈ', 'ᛠ': 'ᛉ', 'ᛡ': 'ᛋ', 'ᚣ': 'ᛏ', 'ᚫ': 'ᛒ', 'ᚪ': 'ᛖ', 'ᛞ': 'ᛗ', 'ᛟ': 'ᛚ', 'ᛝ': 'ᛝ', 'ᛚ': 'ᛟ', 'ᛗ': 'ᛞ', 'ᛖ': 'ᚪ', 'ᛒ': 'ᚫ', 'ᛏ': 'ᚣ', 'ᛋ': 'ᛡ', 'ᛉ': 'ᛠ'}
T_DIANA = {'ᛇ': 'ᚠ', 'ᛄ': 'ᚢ', 'ᛁ': 'ᚦ', 'ᚾ': 'ᚩ', 'ᚻ': 'ᚱ', 'ᚹ': 'ᚳ', 'ᚷ': 'ᚷ', 'ᚳ': 'ᚹ', 'ᚱ': 'ᚻ', 'ᚩ': 'ᚾ', 'ᚦ': 'ᛁ', 'ᚢ': 'ᛄ', 'ᚠ': 'ᛇ', 'ᛠ': 'ᛈ', 'ᛡ': 'ᛉ', 'ᚣ': 'ᛋ', 'ᚫ': 'ᛏ', 'ᚪ': 'ᛒ', 'ᛞ': 'ᛖ', 'ᛟ': 'ᛗ', 'ᛝ': 'ᛚ', 'ᛚ': 'ᛝ', 'ᛗ': 'ᛟ', 'ᛖ': 'ᛞ', 'ᛒ': 'ᚪ', 'ᛏ': 'ᚫ', 'ᛋ': 'ᚣ', 'ᛉ': 'ᛡ', 'ᛈ': 'ᛠ'}
B_DIANA = {'ᛄ': 'ᚠ', 'ᛁ': 'ᚢ', 'ᚾ': 'ᚦ', 'ᚻ': 'ᚩ', 'ᚹ': 'ᚱ', 'ᚷ': 'ᚳ', 'ᚳ': 'ᚷ', 'ᚱ': 'ᚹ', 'ᚩ': 'ᚻ', 'ᚦ': 'ᚾ', 'ᚢ': 'ᛁ', 'ᚠ': 'ᛄ', 'ᛠ': 'ᛇ', 'ᛡ': 'ᛈ', 'ᚣ': 'ᛉ', 'ᚫ': 'ᛋ', 'ᚪ': 'ᛏ', 'ᛞ': 'ᛒ', 'ᛟ': 'ᛖ', 'ᛝ': 'ᛗ', 'ᛚ': 'ᛚ', 'ᛗ': 'ᛝ', 'ᛖ': 'ᛟ', 'ᛒ': 'ᛞ', 'ᛏ': 'ᚪ', 'ᛋ': 'ᚫ', 'ᛉ': 'ᚣ', 'ᛈ': 'ᛡ', 'ᛇ': 'ᛠ'}
E_DIANA = {'ᛁ': 'ᚠ', 'ᚾ': 'ᚢ', 'ᚻ': 'ᚦ', 'ᚹ': 'ᚩ', 'ᚷ': 'ᚱ', 'ᚳ': 'ᚳ', 'ᚱ': 'ᚷ', 'ᚩ': 'ᚹ', 'ᚦ': 'ᚻ', 'ᚢ': 'ᚾ', 'ᚠ': 'ᛁ', 'ᛠ': 'ᛄ', 'ᛡ': 'ᛇ', 'ᚣ': 'ᛈ', 'ᚫ': 'ᛉ', 'ᚪ': 'ᛋ', 'ᛞ': 'ᛏ', 'ᛟ': 'ᛒ', 'ᛝ': 'ᛖ', 'ᛚ': 'ᛗ', 'ᛗ': 'ᛚ', 'ᛖ': 'ᛝ', 'ᛒ': 'ᛟ', 'ᛏ': 'ᛞ', 'ᛋ': 'ᚪ', 'ᛉ': 'ᚫ', 'ᛈ': 'ᚣ', 'ᛇ': 'ᛡ', 'ᛄ': 'ᛠ'}
M_DIANA = {'ᚾ': 'ᚠ', 'ᚻ': 'ᚢ', 'ᚹ': 'ᚦ', 'ᚷ': 'ᚩ', 'ᚳ': 'ᚱ', 'ᚱ': 'ᚳ', 'ᚩ': 'ᚷ', 'ᚦ': 'ᚹ', 'ᚢ': 'ᚻ', 'ᚠ': 'ᚾ', 'ᛠ': 'ᛁ', 'ᛡ': 'ᛄ', 'ᚣ': 'ᛇ', 'ᚫ': 'ᛈ', 'ᚪ': 'ᛉ', 'ᛞ': 'ᛋ', 'ᛟ': 'ᛏ', 'ᛝ': 'ᛒ', 'ᛚ': 'ᛖ', 'ᛗ': 'ᛗ', 'ᛖ': 'ᛚ', 'ᛒ': 'ᛝ', 'ᛏ': 'ᛟ', 'ᛋ': 'ᛞ', 'ᛉ': 'ᚪ', 'ᛈ': 'ᚫ', 'ᛇ': 'ᚣ', 'ᛄ': 'ᛡ', 'ᛁ': 'ᛠ'}
L_DIANA = {'ᚻ': 'ᚠ', 'ᚹ': 'ᚢ', 'ᚷ': 'ᚦ', 'ᚳ': 'ᚩ', 'ᚱ': 'ᚱ', 'ᚩ': 'ᚳ', 'ᚦ': 'ᚷ', 'ᚢ': 'ᚹ', 'ᚠ': 'ᚻ', 'ᛠ': 'ᚾ', 'ᛡ': 'ᛁ', 'ᚣ': 'ᛄ', 'ᚫ': 'ᛇ', 'ᚪ': 'ᛈ', 'ᛞ': 'ᛉ', 'ᛟ': 'ᛋ', 'ᛝ': 'ᛏ', 'ᛚ': 'ᛒ', 'ᛗ': 'ᛖ', 'ᛖ': 'ᛗ', 'ᛒ': 'ᛚ', 'ᛏ': 'ᛝ', 'ᛋ': 'ᛟ', 'ᛉ': 'ᛞ', 'ᛈ': 'ᚪ', 'ᛇ': 'ᚫ', 'ᛄ': 'ᚣ', 'ᛁ': 'ᛡ', 'ᚾ': 'ᛠ'}
NG_DIANA = {'ᚹ': 'ᚠ', 'ᚷ': 'ᚢ', 'ᚳ': 'ᚦ', 'ᚱ': 'ᚩ', 'ᚩ': 'ᚱ', 'ᚦ': 'ᚳ', 'ᚢ': 'ᚷ', 'ᚠ': 'ᚹ', 'ᛠ': 'ᚻ', 'ᛡ': 'ᚾ', 'ᚣ': 'ᛁ', 'ᚫ': 'ᛄ', 'ᚪ': 'ᛇ', 'ᛞ': 'ᛈ', 'ᛟ': 'ᛉ', 'ᛝ': 'ᛋ', 'ᛚ': 'ᛏ', 'ᛗ': 'ᛒ', 'ᛖ': 'ᛖ', 'ᛒ': 'ᛗ', 'ᛏ': 'ᛚ', 'ᛋ': 'ᛝ', 'ᛉ': 'ᛟ', 'ᛈ': 'ᛞ', 'ᛇ': 'ᚪ', 'ᛄ': 'ᚫ', 'ᛁ': 'ᚣ', 'ᚾ': 'ᛡ', 'ᚻ': 'ᛠ'}
OE_DIANA = {'ᚷ': 'ᚠ', 'ᚳ': 'ᚢ', 'ᚱ': 'ᚦ', 'ᚩ': 'ᚩ', 'ᚦ': 'ᚱ', 'ᚢ': 'ᚳ', 'ᚠ': 'ᚷ', 'ᛠ': 'ᚹ', 'ᛡ': 'ᚻ', 'ᚣ': 'ᚾ', 'ᚫ': 'ᛁ', 'ᚪ': 'ᛄ', 'ᛞ': 'ᛇ', 'ᛟ': 'ᛈ', 'ᛝ': 'ᛉ', 'ᛚ': 'ᛋ', 'ᛗ': 'ᛏ', 'ᛖ': 'ᛒ', 'ᛒ': 'ᛖ', 'ᛏ': 'ᛗ', 'ᛋ': 'ᛚ', 'ᛉ': 'ᛝ', 'ᛈ': 'ᛟ', 'ᛇ': 'ᛞ', 'ᛄ': 'ᚪ', 'ᛁ': 'ᚫ', 'ᚾ': 'ᚣ', 'ᚻ': 'ᛡ', 'ᚹ': 'ᛠ'}
D_DIANA = {'ᚳ': 'ᚠ', 'ᚱ': 'ᚢ', 'ᚩ': 'ᚦ', 'ᚦ': 'ᚩ', 'ᚢ': 'ᚱ', 'ᚠ': 'ᚳ', 'ᛠ': 'ᚷ', 'ᛡ': 'ᚹ', 'ᚣ': 'ᚻ', 'ᚫ': 'ᚾ', 'ᚪ': 'ᛁ', 'ᛞ': 'ᛄ', 'ᛟ': 'ᛇ', 'ᛝ': 'ᛈ', 'ᛚ': 'ᛉ', 'ᛗ': 'ᛋ', 'ᛖ': 'ᛏ', 'ᛒ': 'ᛒ', 'ᛏ': 'ᛖ', 'ᛋ': 'ᛗ', 'ᛉ': 'ᛚ', 'ᛈ': 'ᛝ', 'ᛇ': 'ᛟ', 'ᛄ': 'ᛞ', 'ᛁ': 'ᚪ', 'ᚾ': 'ᚫ', 'ᚻ': 'ᚣ', 'ᚹ': 'ᛡ', 'ᚷ': 'ᛠ'}
A_DIANA = {'ᚱ': 'ᚠ', 'ᚩ': 'ᚢ', 'ᚦ': 'ᚦ', 'ᚢ': 'ᚩ', 'ᚠ': 'ᚱ', 'ᛠ': 'ᚳ', 'ᛡ': 'ᚷ', 'ᚣ': 'ᚹ', 'ᚫ': 'ᚻ', 'ᚪ': 'ᚾ', 'ᛞ': 'ᛁ', 'ᛟ': 'ᛄ', 'ᛝ': 'ᛇ', 'ᛚ': 'ᛈ', 'ᛗ': 'ᛉ', 'ᛖ': 'ᛋ', 'ᛒ': 'ᛏ', 'ᛏ': 'ᛒ', 'ᛋ': 'ᛖ', 'ᛉ': 'ᛗ', 'ᛈ': 'ᛚ', 'ᛇ': 'ᛝ', 'ᛄ': 'ᛟ', 'ᛁ': 'ᛞ', 'ᚾ': 'ᚪ', 'ᚻ': 'ᚫ', 'ᚹ': 'ᚣ', 'ᚷ': 'ᛡ', 'ᚳ': 'ᛠ'}
AE_DIANA = {'ᚩ': 'ᚠ', 'ᚦ': 'ᚢ', 'ᚢ': 'ᚦ', 'ᚠ': 'ᚩ', 'ᛠ': 'ᚱ', 'ᛡ': 'ᚳ', 'ᚣ': 'ᚷ', 'ᚫ': 'ᚹ', 'ᚪ': 'ᚻ', 'ᛞ': 'ᚾ', 'ᛟ': 'ᛁ', 'ᛝ': 'ᛄ', 'ᛚ': 'ᛇ', 'ᛗ': 'ᛈ', 'ᛖ': 'ᛉ', 'ᛒ': 'ᛋ', 'ᛏ': 'ᛏ', 'ᛋ': 'ᛒ', 'ᛉ': 'ᛖ', 'ᛈ': 'ᛗ', 'ᛇ': 'ᛚ', 'ᛄ': 'ᛝ', 'ᛁ': 'ᛟ', 'ᚾ': 'ᛞ', 'ᚻ': 'ᚪ', 'ᚹ': 'ᚫ', 'ᚷ': 'ᚣ', 'ᚳ': 'ᛡ', 'ᚱ': 'ᛠ'}
Y_DIANA = {'ᚦ': 'ᚠ', 'ᚢ': 'ᚢ', 'ᚠ': 'ᚦ', 'ᛠ': 'ᚩ', 'ᛡ': 'ᚱ', 'ᚣ': 'ᚳ', 'ᚫ': 'ᚷ', 'ᚪ': 'ᚹ', 'ᛞ': 'ᚻ', 'ᛟ': 'ᚾ', 'ᛝ': 'ᛁ', 'ᛚ': 'ᛄ', 'ᛗ': 'ᛇ', 'ᛖ': 'ᛈ', 'ᛒ': 'ᛉ', 'ᛏ': 'ᛋ', 'ᛋ': 'ᛏ', 'ᛉ': 'ᛒ', 'ᛈ': 'ᛖ', 'ᛇ': 'ᛗ', 'ᛄ': 'ᛚ', 'ᛁ': 'ᛝ', 'ᚾ': 'ᛟ', 'ᚻ': 'ᛞ', 'ᚹ': 'ᚪ', 'ᚷ': 'ᚫ', 'ᚳ': 'ᚣ', 'ᚱ': 'ᛡ', 'ᚩ': 'ᛠ'}
IA_DIANA = {'ᚢ': 'ᚠ', 'ᚠ': 'ᚢ', 'ᛠ': 'ᚦ', 'ᛡ': 'ᚩ', 'ᚣ': 'ᚱ', 'ᚫ': 'ᚳ', 'ᚪ': 'ᚷ', 'ᛞ': 'ᚹ', 'ᛟ': 'ᚻ', 'ᛝ': 'ᚾ', 'ᛚ': 'ᛁ', 'ᛗ': 'ᛄ', 'ᛖ': 'ᛇ', 'ᛒ': 'ᛈ', 'ᛏ': 'ᛉ', 'ᛋ': 'ᛋ', 'ᛉ': 'ᛏ', 'ᛈ': 'ᛒ', 'ᛇ': 'ᛖ', 'ᛄ': 'ᛗ', 'ᛁ': 'ᛚ', 'ᚾ': 'ᛝ', 'ᚻ': 'ᛟ', 'ᚹ': 'ᛞ', 'ᚷ': 'ᚪ', 'ᚳ': 'ᚫ', 'ᚱ': 'ᚣ', 'ᚩ': 'ᛡ', 'ᚦ': 'ᛠ'}
EA_DIANA = {'ᚠ': 'ᚠ', 'ᛠ': 'ᚢ', 'ᛡ': 'ᚦ', 'ᚣ': 'ᚩ', 'ᚫ': 'ᚱ', 'ᚪ': 'ᚳ', 'ᛞ': 'ᚷ', 'ᛟ': 'ᚹ', 'ᛝ': 'ᚻ', 'ᛚ': 'ᚾ', 'ᛗ': 'ᛁ', 'ᛖ': 'ᛄ', 'ᛒ': 'ᛇ', 'ᛏ': 'ᛈ', 'ᛋ': 'ᛉ', 'ᛉ': 'ᛋ', 'ᛈ': 'ᛏ', 'ᛇ': 'ᛒ', 'ᛄ': 'ᛖ', 'ᛁ': 'ᛗ', 'ᚾ': 'ᛚ', 'ᚻ': 'ᛝ', 'ᚹ': 'ᛟ', 'ᚷ': 'ᛞ', 'ᚳ': 'ᚪ', 'ᚱ': 'ᚫ', 'ᚩ': 'ᚣ', 'ᚦ': 'ᛡ', 'ᚢ': 'ᛠ'}


def fibgen(limit):
    fibonacci = [0, 1]
    while len(fibonacci[-1]) < limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None
primes = [x for x in range(3307) if isprime(x)]

def ceaser(ciphertext, shift, output_type):
    output = ""
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        elif char in disallowed:
            output += char
        else:
            current_index = LP_Util.RunesToIndex[char]
            if output_type == "R":
                output += LP_Util.IndexToRunes[(current_index-shift)%29]
            else:
                output += LP_Util.IndexToText[(current_index-shift)%29]

    return output
    
def vigenere(ciphertext, key, output_type):
    output = ""
    if check_latin(key) == True:
        key = LP_Util.lat_to_run(key)
    key = (key * (len(ciphertext)//len(key) + 1))[:len(ciphertext)]
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        elif char in disallowed:
            output += char
        else:      
            shift = alphabet.index(key[key_index])
            decrypted_char_index = (alphabet.index(char) - shift) % len(alphabet)
            output += alphabet[decrypted_char_index]
            key_index = (key_index + 1) % key_length

    if output_type == "L":
        output = LP_Util.run_to_lat(output)

    return output

def atbash(ciphertext, output_type):
    output = ""
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        elif char in disallowed:
            output += char
        else:
            if output_type == "R":
                output += atbash_enc[char]
            if output_type == "L":
                output += LP_Util.RuneToText[atbash_enc[char]]

    return output

def totient_stream(ciphertext, output_type):
    output = ''
    shift = 0
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        elif char in disallowed:
            output += char
        else:
            if output_type == "R":
                output += LP_Util.Modified_VigTable_Runes[LP_Util.RunesToIndex[char]][(primes[shift] - 1)%29]
            else:
                output += LP_Util.Modified_VigTable_Letters[(LP_Util.RunesToIndex[char])][(primes[shift] - 1)%29]
            
            shift += 1
    
    return output

def totient_stream_derivitive(ciphertext, output_type):
    return "Not implemented yet, sorry"

def fibonacci_stream(ciphertext, output_type):
    fib = fibgen(len(ciphertext+1))
    output = ""
    shift = 0
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        else:
            if output_type == "R":
                output += LP_Util.Modified_VigTable_Runes[LP_Util.RunesToIndex[char]][(fib[shift] - 1)%29]
            else:
                output += LP_Util.Modified_VigTable_Letters[(LP_Util.RunesToIndex[char])][(fib[shift] - 1)%29]
            
            shift += 1
    
    return output

def fibonacci_stream_derivitive(ciphertext, output_type):
    return "Not implemented yet, sorry"

def beaufort(ciphertext, key, output_type):
    output = ""
    if check_latin(key) == True:
        key = LP_Util.lat_to_run(key)
    key = (key * (len(ciphertext)//len(key) + 1))[:len(ciphertext)]
    key_length = len(key)
    key_index = 0
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        elif char in disallowed:
            output += char
        else:
            shift = alphabet.index(key[key_index])
            decrypted_char_index = (shift - alphabet.index(char)) % len(alphabet)
            output += alphabet[decrypted_char_index]
            key_index = (key_index + 1) % key_length

    if output_type == "L":
        output = LP_Util.run_to_lat(output)

    return output

def inverse_geometry(ciphertext, output_type):
    outstr = ''
    for char in ciphertext:
        if char == " ":
            output +=  " "
        elif char == "\n":
            output += "\n"
        elif char == ".":
            output += "."
        elif char == "&":
            output += "&"
        else:
            var = (729 / LP_Util.RunesToIndex[char])%29
            var2 = var % 1
            #finalvar = (var + 1)%29
            
            if var2 > 0.5:
                finalvar = (var + 1)%29
            elif var2 < 0.5:
                finalvar = (var - 1)%29
            elif var2 == 0.5:
                finalvar - (var)%29
            
            finalvar_dec = finalvar % 1
            if output_type == "R":
                outstr += LP_Util.Modified_VigTable_Runes[int(finalvar-finalvar_dec)%29][0]
            else:
                outstr += LP_Util.Modified_VigTable_Letters[int(finalvar-finalvar_dec)%29][0]

    return outstr

def diana(ciphertext, key, output_type):
    output = ''
    shift = 0

    if check_latin(key) == True:
        key = LP_Util.lat_to_run(key)
    key = (key * (len(ciphertext)//len(key) + 1))[:len(ciphertext)]
    for char in key:
        if char == 'ᚠ':
            output += F_DIANA[ciphertext[shift]] 
        elif char == 'ᚢ':
            output += U_DIANA[ciphertext[shift]]
        elif char == 'ᚦ':
            output += TH_DIANA[ciphertext[shift]] 
        elif char == 'ᚩ':
            output += O_DIANA[ciphertext[shift]] 
        elif char == 'ᚱ':
            output += R_DIANA[ciphertext[shift]] 
        elif char == 'ᚳ':
            output += C_DIANA[ciphertext[shift]] 
        elif char == 'ᚷ':
            output += G_DIANA[ciphertext[shift]] 
        elif char == 'ᚹ':
            output += W_DIANA[ciphertext[shift]] 
        elif char == 'ᚻ':
            output += H_DIANA[ciphertext[shift]] 
        elif char == 'ᚾ':
            output += N_DIANA[ciphertext[shift]] 
        elif char == 'ᛁ':
            output += I_DIANA[ciphertext[shift]] 
        elif char == 'ᛄ':
            output += J_DIANA[ciphertext[shift]] 
        elif char == 'ᛇ':
            output += EO_DIANA[ciphertext[shift]] 
        elif char == 'ᛈ':
            output += P_DIANA[ciphertext[shift]] 
        elif char == 'ᛉ':
            output += X_DIANA[ciphertext[shift]] 
        elif char == 'ᛋ':
            output += S_DIANA[ciphertext[shift]] 
        elif char == 'ᛏ':
            output += T_DIANA[ciphertext[shift]] 
        elif char == 'ᛒ':
            output += B_DIANA[ciphertext[shift]] 
        elif char == 'ᛖ':
            output += E_DIANA[ciphertext[shift]] 
        elif char == 'ᛗ':
            output += M_DIANA[ciphertext[shift]] 
        elif char == 'ᛚ':
            output += L_DIANA[ciphertext[shift]] 
        elif char == 'ᛝ':
            output += NG_DIANA[ciphertext[shift]] 
        elif char == 'ᛟ':
            output += OE_DIANA[ciphertext[shift]] 
        elif char == 'ᛞ':
            output += D_DIANA[ciphertext[shift]] 
        elif char == 'ᚪ':
            output += A_DIANA[ciphertext[shift]] 
        elif char == 'ᚫ':
            output += AE_DIANA[ciphertext[shift]] 
        elif char == 'ᚣ':
            output += Y_DIANA[ciphertext[shift]] 
        elif char == 'ᛡ':
            output += IA_DIANA[ciphertext[shift]] 
        elif char == 'ᛠ':
            output += EA_DIANA[ciphertext[shift]] 
        shift += 1

        if output_type == "L":
            output = LP_Util.run_to_lat(output)           

    return output
