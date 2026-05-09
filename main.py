import time
import curses


def main():
    while True:
        mode = get_mode()

        if mode == "word":
            run_word_mode()
        elif mode == "time":
            run_time_mode()
        elif mode == "exit":
            print("exit...")
            break
            
        else:
            print("Please try again with valid mode selected!")
            
    

def get_mode():
    return input("Choose mode(word/time)").strip().lower()


def run_word_mode():
    sentence = get_sentence()
    print("\ntype this\n" , sentence)

    input("press enter to start")
    start_time = time.time()

    user_input = input("start typing !!")

    end_start = time.time()

    evaluate_word_mode(start_time , end_start , user_input , sentence)

def run_time_mode():
    sentence = get_sentence()
    print("\ntype this\n" , sentence)
    
    input("press enter to start!!")
    start_time = time.time()
    user_input = input("start typing !!")

    end_time = time.time()

    evaluate_time_mode(start_time , end_time , user_input , sentence)


def get_sentence():
    return "hi how are i hope u are doing well !!"

def evaluate_word_mode(start_time , end_time , user_input , sentence):
    sentence_word = sentence.split()
    user_words = user_input.split()
    time_taken = end_time - start_time

    correct = 0

    for i in range(min(len(sentence_word) , len(user_words))):
        if sentence_word[i] == user_words[i]:
            correct += 1
    
    wpm = len(user_words)/time_taken * 60
    
    if (len(user_words) == 0):
        accuracy = 0
    else:
        accuracy = (correct/len(sentence_word)) * 100

    print_result(accuracy , wpm)

def evaluate_time_mode(start_time , end_time , user_input , sentence):
    sentence_word = sentence.split()
    user_words = user_input.split()
    time_taken = end_time - start_time

    correct = 0

    for i in range(min(len(sentence_word) , len(user_words))):
        if sentence_word[i] == user_words:
            correct += 1
    
    wpm = len(user_words)/time_taken * 60
    
    if (len(user_words) == 0):
        accuracy = 0
    else:
        accuracy = (correct/len(user_words)) * 100

    print_result(accuracy , wpm)


def print_result(accuracy , wpm):
    print("accuracy:\t" , accuracy)
    print("wpm\t" , wpm)


def run_live_typing(stdscr):
    curses.curs_set(1)
    stdscr.clear()

    sentence = "once a boy who lived came to die"
    typed = ""

    stdscr.addstr(0,0 , "type this !!")
    stdscr.addstr(1,0,sentence)

    start_time = time.time()
    time_limit = 30 

    while True:
        elapsed_time = time.time() - start_time
        remaining = int(time_limit - elapsed_time)

        if remaining <= 0:
            break 

        stdscr.addstr(3 , 0 , "Time left: {remaining}")
        stdscr.addstr(5 ,  0 , typed)

        stdscr.refresh()
        stdscr.nodelay(True)

        try: # the try and except block if nothing key -1 which mean nothing 
            key = stdscr.getch()
        except:
            key = -1
        
        if key == -1:
            continue
    
        if key == 10:
            break # pressing enter early to quit 

        elif key in (127 , curses.KEY_BACKSPACE):
            typed = typed[:-1]
        
        elif 0 <= key <= 255:
            typed += key
        
    stdscr.clear()

    sentence_word = sentence.split()
    user_word = typed.split()

    correct = 0

    for  i in range(min(len(sentence_word) , len(user_word))):
        if (sentence_word[i] == user_word[i]):
            correct += 1
    
    time_taken = time.time() - start_time
    wpm = len(user_word)/time_taken * 60 if time_taken > 0 else 0
    accuracy = correct/len(user_word) * 100 if len(user_word) > 0 else 0

    

        
        

























































main()