import curses
import time

# =========================
# MAIN ENTRY
# =========================


def main():
    curses.wrapper(run_typing_test)


# =========================
# TYPING TEST
# =========================


def run_typing_test(stdscr):

    # ---------- CURSES SETUP ----------
    curses.curs_set(1)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.nodelay(True)

    # ---------- TEST DATA ----------
    sentence = "the quick brown fox jumps over the lazy dog"

    typed = ""

    start_time = None
    time_limit = 30

    # =========================
    # MAIN LOOP
    # =========================

    while True:

        # ---------- TIMER ----------
        if start_time is None:
            remaining = time_limit
        else:
            elapsed = time.time() - start_time
            remaining = int(time_limit - elapsed)

        # stop when timer ends
        if remaining <= 0:
            break

        # ---------- SCREEN CLEAR ----------
        # stdscr.clear()

        # ---------- HEADER ----------
        stdscr.addstr(0, 0, "CLI Monkeytype")
        stdscr.addstr(1, 0, f"Time Left: {remaining}s")

        # ---------- TARGET SENTENCE ----------
        stdscr.addstr(3, 0, "Type this:")

        # character-by-character rendering
        for i, char in enumerate(sentence):

            if i < len(typed):

                # CORRECT CHAR
                if typed[i] == char:
                    stdscr.addstr(5, i, char, curses.color_pair(1))

                # WRONG CHAR
                else:
                    stdscr.addstr(5, i, char, curses.color_pair(2))

            else:
                stdscr.addstr(5, i, char)

        # ---------- USER INPUT LINE ----------
        stdscr.addstr(7, 0, typed)

        # ---------- CURSOR ----------
        stdscr.move(7, len(typed))

        # ---------- REFRESH ----------
        stdscr.refresh()

        # ---------- INPUT ----------
        key = stdscr.getch()

        # no key pressed
        if key == -1:
            continue

        # start timer on first keypress
        if start_time is None:
            start_time = time.time()

        # ENTER KEY
        if key == 10:
            break

        # BACKSPACE
        elif key in (127, curses.KEY_BACKSPACE):
            typed = typed[:-1]

        # NORMAL CHARACTERS
        elif 0 <= key <= 255:
            typed += chr(key)

    

    show_results(stdscr, typed, sentence, start_time)





def calculate_results(typed, sentence, start_time):

    typed_words = typed.split()
    sentence_words = sentence.split()

    correct = 0

    for i in range(min(len(typed_words), len(sentence_words))):

        if typed_words[i] == sentence_words[i]:
            correct += 1

    time_taken = max(time.time() - start_time, 1)

    wpm = (len(typed_words) / time_taken) * 60

    if len(typed_words) == 0:
        accuracy = 0
    else:
        accuracy = (correct / len(typed_words)) * 100

    return round(wpm, 2), round(accuracy, 2)





def show_results(stdscr, typed, sentence, start_time):

    wpm, accuracy = calculate_results(typed, sentence, start_time)

    stdscr.clear()

    stdscr.addstr(2, 0, "TEST COMPLETE")
    stdscr.addstr(4, 0, f"WPM: {wpm}")
    stdscr.addstr(5, 0, f"Accuracy: {accuracy}%")

    stdscr.addstr(7, 0, "Press any key to exit")

    stdscr.refresh()

    stdscr.getch()




if __name__ == "__main__":
    main()
