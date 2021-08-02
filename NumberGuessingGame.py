import random
num = random.randint(1,11)
print("********** Program Started **********")
print("[*] You Have 5 Lives To Guess")
for i in range(5):
    a = int(input("[+] Guess The Number: "))
    if a == num:
        print("[*] You Guessed It Correctly, ", num)
        break
    else:
        print("[^] You Guessed It Wrong!")
print("********** Program Finished **********")  
