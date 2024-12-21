from tkinter import *
import random
from tkinter import messagebox

# Initialize main window
Mainscreen = Tk()

Mainscreen.attributes('-fullscreen', True)  # Full-screen mode
Mainscreen.title('Typing Test With Paragraph Selection')
Mainscreen.config(bg="#2b2b2b")  # Dark grey background

# Dynamic font scaling based on screen resolution
screen_width = Mainscreen.winfo_screenwidth()
screen_height = Mainscreen.winfo_screenheight()
font_scale = screen_width / 1920  # Assuming 1920x1080 as the baseline resolution

score = 0
missed = 0
errors = 0
accuracy = 100
time = 0  # Timer starts at 0
count1 = 0
movingwords = ''
timer_running = True  # Flag to control the timer

# Extended predefined paragraphs for the typing test
paragraphs = [
    "The quick brown fox jumps over the lazy dog. This phrase has been used for decades as a typing practice exercise because it includes all the letters of the English alphabet. It is a great way to improve typing speed and accuracy while mastering the use of the keyboard. Typing this repeatedly helps you learn the placement of letters on the keyboard.",
    "Artificial Intelligence and machine learning are revolutionizing technology and society. These cutting-edge fields enable machines to perform tasks that typically require human intelligence, such as decision-making, speech recognition, and language translation. AI is being applied in healthcare, transportation, and entertainment, making it a cornerstone of modern innovation.",
    "Python is a versatile and powerful programming language that is easy to learn and use. It is widely employed in various fields, including web development, data analysis, artificial intelligence, and automation. Python's simplicity and flexibility make it a popular choice among developers. Its libraries, such as NumPy, Pandas, and TensorFlow, further enhance its capabilities."
]

selected_paragraph = StringVar(value=paragraphs[0])  # Default paragraph

# Function to start the game with the selected paragraph
def start_game():
    global current_text, time, score, missed, errors, timer_running
    current_text = selected_paragraph.get()
    labelforward.configure(text=current_text)
    score = 0
    missed = 0
    errors = 0
    time = 0
    timer_running = True  # Restart the timer
    scorelabelcount.configure(text=score)
    missedlabelcount.configure(text=missed)
    errorlabelcount.configure(text=errors)
    timercount.configure(text=time)
    accuracy_label.configure(text="Accuracy: 100%")
    wordentry.delete(0, END)
    wordentry.focus_set()
    giventime()  # Start the timer

# Function to display moving text
def movingtext():
    global count1, movingwords
    floatingtext = 'Typing Test By Abhi Patil'
    if count1 >= len(floatingtext):
        count1 = 0
        movingwords = ''
    movingwords += floatingtext[count1]
    count1 += 1
    fontlabel.configure(text=movingwords)
    fontlabel.after(150, movingtext)

# Function to handle the timer increment
def giventime():
    global time, timer_running
    if timer_running:
        time += 1
        timercount.configure(text=time)
        timercount.after(1000, giventime)

# Function to handle real-time error detection
def detect_errors(event=None):
    global current_text, errors, accuracy
    typed_text = wordentry.get()
    errors = 0

    for i, char in enumerate(typed_text):
        if i < len(current_text) and char != current_text[i]:
            errors += 1

    if errors > 0:
        wordentry.config(fg="red")
    else:
        wordentry.config(fg="black")

    accuracy = max(0, 100 - int(errors / len(typed_text) * 100)) if typed_text else 100
    accuracy_label.configure(text=f"Accuracy: {accuracy}%")
    errorlabelcount.configure(text=errors)

# Function to handle the game logic when the player presses Enter
def game(event):
    global score, missed, timer_running
    typed_text = wordentry.get()
    if typed_text == current_text:
        score += 1
        scorelabelcount.configure(text=score)
        wordentry.delete(0, END)
        timer_running = False  # Stop the timer when the paragraph is completed
        messagebox.showinfo("Congratulations!", f"You completed the paragraph!\nScore: {score}\nTime: {time} seconds\nAccuracy: {accuracy}%")
    else:
        missed += 1
        missedlabelcount.configure(text=missed)

    wordentry.delete(0, END)
    detect_errors()

# Create labels and entry widgets
fontlabel = Label(Mainscreen, text='', font=('arial', int(25 * font_scale), 'italic bold'), fg='#FF6F61', bg='#2b2b2b', width=40)
fontlabel.pack(pady=20)
movingtext()

startlabel = Label(Mainscreen, text='Select a Paragraph to Start', font=('arial', int(20 * font_scale), 'italic bold'), bg='#2b2b2b', fg='white')
startlabel.pack(pady=10)

# Paragraph selection dropdown
paragraph_selector = OptionMenu(Mainscreen, selected_paragraph, *paragraphs)
paragraph_selector.config(font=('arial', int(14 * font_scale), 'italic bold'), bg='#fdfd96', fg='black', width=60)
paragraph_selector.pack(pady=10)

# Start button
start_button = Button(Mainscreen, text="Start Game", font=('arial', int(14 * font_scale), 'bold'), bg='#77dd77', fg='black', command=start_game)
start_button.pack(pady=10)

# Larger paragraph display
labelforward = Label(Mainscreen, text='', font=('arial', int(16 * font_scale), 'italic bold'), fg='#77dd77', bg='#2b2b2b', wraplength=screen_width - 200, justify=LEFT)
labelforward.pack(pady=20)

# Input box
wordentry = Entry(Mainscreen, font=('arial', int(20 * font_scale), 'italic bold'), bd=10, bg='#fdfd96', fg='black', relief=FLAT, justify='left', width=50)
wordentry.pack(pady=10)
wordentry.bind('<KeyRelease>', detect_errors)

# Accuracy, Time, and Score Box (Below the Input Box)
score_frame = Frame(Mainscreen, bg="#2b2b2b")
score_frame.pack(pady=10)

Label(score_frame, text='Score:', font=('arial', int(16 * font_scale), 'italic bold'), fg='orange', bg='#2b2b2b').grid(row=0, column=0, padx=10)
scorelabelcount = Label(score_frame, text=score, font=('arial', int(16 * font_scale), 'italic bold'), fg='white', bg='#2b2b2b')
scorelabelcount.grid(row=0, column=1, padx=10)

Label(score_frame, text='Missed:', font=('arial', int(16 * font_scale), 'italic bold'), fg='orange', bg='#2b2b2b').grid(row=0, column=2, padx=10)
missedlabelcount = Label(score_frame, text=missed, font=('arial', int(16 * font_scale), 'italic bold'), fg='white', bg='#2b2b2b')
missedlabelcount.grid(row=0, column=3, padx=10)

Label(score_frame, text='Errors:', font=('arial', int(16 * font_scale), 'italic bold'), fg='orange', bg='#2b2b2b').grid(row=0, column=4, padx=10)
errorlabelcount = Label(score_frame, text=errors, font=('arial', int(16 * font_scale), 'italic bold'), fg='white', bg='#2b2b2b')
errorlabelcount.grid(row=0, column=5, padx=10)

Label(score_frame, text='Time:', font=('arial', int(16 * font_scale), 'italic bold'), fg='orange', bg='#2b2b2b').grid(row=0, column=6, padx=10)
timercount = Label(score_frame, text=time, font=('arial', int(16 * font_scale), 'italic bold'), fg='white', bg='#2b2b2b')
timercount.grid(row=0, column=7, padx=10)

accuracy_label = Label(score_frame, text="Accuracy: 100%", font=('arial', int(16 * font_scale), 'italic bold'), fg='#fdfd96', bg='#2b2b2b')
accuracy_label.grid(row=0, column=8, padx=10)

# Game instruction
gameinstruction = Label(Mainscreen, text='Hit enter button after typing the paragraph', font=('arial', int(18 * font_scale), 'italic bold'), fg='lightgrey', bg='#2b2b2b', wraplength=screen_width - 200)
gameinstruction.pack(pady=20)

# Bind the Enter key to the game function
Mainscreen.bind('<Return>', game)

# Start the main loop
mainloop()
