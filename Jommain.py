#!/usr/bin/env python

import random
def main():
    """Jom teka nombor seterusnya."""
    print("Teka nombor 1 1 2 3... !")
    
    nombor = [
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
        ]

    x =random.choice(nombor)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("Apakah nombor seterusnya? "))
        
        if x == guess:
            print(f"Tahniah. Jawapan anda betul!".format(guess))
            break
        else:
            print(f"Maaf. Jawapan anda salah.".format(guess))
            print(f"Anda ada {max_trials} lagi cubaan.")
            max_trials -= 1
        if max_trials == 0:
            print(f"Cubaan anda tamat. Nombor itu ialah {x}.".format(guess))
        
main()