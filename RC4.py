from S_Chart import chart as s

i = int(input("What is the value of i?: "))
j = int(input("What is the value of j?: "))

def encryption(): # Uses the 5 steps of the RC4 algorithm

     global i
     global j
     
     i = (i+1) % 256

     j = (j + s[i]) % 256

     s_of_j = s[i]
     s_of_i = s[j]

     t = (s_of_i + s_of_j) % 256

     return s[t]

while True:
     encryption_output = ""
     plaintext = str(input("What is the given plaintext?: "))

     if len(plaintext) > 22:
          pass

     else:
          for p in range(len(plaintext)): # Runs a loop for every character in plaintext
               hexed = encryption() ^ ord(str(plaintext[p])) # XORs the curent character with the encryption function
               if hexed < 16:
                    encryption_output += "0" + str(hexed) # Makes sure that the hexadecimal being added is two digits/letters, rather than just one 
               else:
                    encryption_output += hex(hexed)[2:] # Only adds the last two characters of the hex 

          print("Hex cipher stream: " + encryption_output + "\n\n")

## DECRYPTION ##

     i = int(input("What is the value of i?: "))
     j = int(input("What is the value of j?: "))
     ciphertext = str(input("What is the ciphertext?: "))

     while True:
          plaintext_output = ""

          if len(ciphertext) > 44:
               print("Invalid string. Please make it shorter than 44 characters\n")
               continue
          else:
               for c in range(0, len(ciphertext), 2):
                    hexed = encryption() ^ int(ciphertext[c:c+2], 16) # XORs the ciphertext with the encryption function, which would cancel the encryption function
                    plaintext_output += str(chr(hexed))

               print(f"Plaintext stream: {plaintext_output}\n")
