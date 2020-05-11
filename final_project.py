import time
def print_begin():
    print("""" 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/               
                       """)
    print(6)

def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if not i in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    str=""
    for i in secret_word:
        if i in old_letters_guessed:
            str+=i+" "
        else:
            str+="_ "
    print(str)



def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed in old_letters_guessed or not letter_guessed.isalpha()or len(letter_guessed)>1:
        return False
    else:
        return True
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if  check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        if  letter_guessed in old_letters_guessed:
            printFine(old_letters_guessed)
        return False
def choose_word(file_path, index):
    file = open(file_path, "r")
    notuniq=[]
    uniqo=[]

    for l in file:
        notuniq+=(l.split())

    for w in notuniq:
       if not w in uniqo:
           uniqo.append(w)
    ans = (notuniq[int(index)], len(uniqo))
    file.close()
    return ans

def printFine(old_letters_guessed):
    old_letters_guessed.sort()
    for i in range(0,len(old_letters_guessed)-1):
            print(old_letters_guessed[i],end=" -> ")
    print(old_letters_guessed[len(old_letters_guessed)-1])



def print_situation(HANGMAN_PHOTOS,num_of_tries,word,old_letters_guessed):
    print(HANGMAN_PHOTOS[num_of_tries])
    show_hidden_word(word, old_letters_guessed)


def main():
    print_begin()
    url = input("Enter file path:")
    num = input("Enter index:")
    tpl=choose_word(url,num)
    num_of_tries=0
    MAX_TRIES=6
    old_letters_guessed=[]
    HANGMAN_PHOTOS={0:"""x-------x""",
 1:
"""
x-------x
|
|
|
|
|
"""

 ,
2:
"""
x-------x
|       |
|       0
|
|
|
""",
3:
"""
x-------x
|       |
|       0
|       |
|
|
"""
,4:
"""
x-------x
|       |
|       0
|      /|\\
|
|
"""
        ,5:
"""
x-------x
|       |
|       0
|      /|\\
|      /
|
"""
        ,6:
"""
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
                    }

    print()
    print("Let’s start!")
    print_situation(HANGMAN_PHOTOS, num_of_tries, tpl[0], old_letters_guessed)
    while(num_of_tries<MAX_TRIES):
        ltr=input("Guess a letter:")
        ltr = ltr.lower()
        while not try_update_letter_guessed(ltr,old_letters_guessed):
             ltr = input("Guess a letter:")
             ltr = ltr.lower()

        if not ltr in tpl[0]:
            num_of_tries += 1
            print(":(")
            print_situation(HANGMAN_PHOTOS, num_of_tries, tpl[0], old_letters_guessed)
        else:
            show_hidden_word(tpl[0], old_letters_guessed)

        if check_win(tpl[0],old_letters_guessed):
            print("WIN")
            break
    if not check_win(tpl[0],old_letters_guessed):
        print("LOSE")

    time.sleep(3)


if __name__ == "__main__":
        main()