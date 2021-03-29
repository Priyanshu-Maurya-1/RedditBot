from tkinter import *
from tkinter.ttk import *
import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password="",
)
window = Tk()
subredditname = StringVar()
commentpost = StringVar()

try:
    subreddit = reddit.subreddit("19DCS060DEMO")
except:
    print("can't connect to reddit")



def GetPost():
    for comment in subreddit.comments(limit=25):
        print("POSTS SELECTED")
        messageVar.configure(text="Comment="+str(comment.body))


def upvote():
    for comment in subreddit.comments(limit=1):
        comment.upvote()
        print("upvote successfull")
def upvotepost():
    for submission in subreddit.hot(limit=1):
        submission.upvote()
        ur.configure(text="Upvote Ratio="+str(submission.upvote_ratio))
        print("UPVOTE successfull")

def downvote():
    for comment in subreddit.comments(limit=1):
        comment.downvote()
        print("Downvote successfull")

def downvotepost():
    for submission in subreddit.hot(limit=1):
        submission.downvote()
        ur.configure(text="Upvote Ratio=" + str(submission.upvote_ratio))
        print("Downvote successfull")

def comment():
    com=commentpost.get()
    for comment in subreddit.comments(limit=1):
        comment.reply(com)
        print("reply successfull")





window.title("Reddit Bot")

window.geometry('1200x520')
sto = Style()
sto.configure('TButton', font=
('calibri', 10, 'bold', 'underline'),
foreground='Green')
w = Label(window, text ='REDDIT BOT',font=("calibri", 50),style="BW.TLabel")
w.grid(row=0,column=1,padx=5,
               pady=5,
               ipady=3)

window.configure(bg='teal')
lbl1=Label(window, text='Subreddit Name='+str(subreddit.display_name),font=("calibri", 25),style="BW.TLabel").grid(row=1,column=0)
#e1 = Entry(window, textvariable=subredditname,width=40)
#e1.grid(row=1, column=1,padx=5,
#               pady=5,
#               ipady=3)
sto.configure("BW.TLabel", background="teal")
lbl = Label(window, text="Click to Fetch Results",font=("calibri", 25),style="BW.TLabel")

lbl.grid(column=0, row=2)

btn = Button(window, text="Click Me", command=GetPost)
btn.grid(column=1, row=2)

btn = Button(window, text="Click To Upvote", command=upvote)
btn.grid(column=1, row=5)

btn = Button(window, text="Click To Upvote Post", command=upvotepost)
btn.grid(column=2, row=5)
ur = Label(window, text=" ",font=("calibri", 25),style="BW.TLabel")
ur.grid(column=0,row=5)
btn = Button(window, text="Click To Downvote", command=downvote)
btn.grid(column=1, row=6)

btn = Button(window, text="Click To Downvote Posr", command=downvotepost)
btn.grid(column=2, row=6)

messageVar = Label(window, text="Comment=",font=("calibri", 25),style="BW.TLabel")
#messageVar.config(bg='lightgreen')
messageVar.grid(column=0, row=3)

Label(window, text='Enter Your Comment',font=("calibri", 25),style="BW.TLabel").grid(row=7)
e2 = Entry(window,textvariable=commentpost,width=40)
e2.grid(row=1, column=1,padx=5,
               pady=5,
               ipady=3)
e2.grid(row=7, column=1)
btn = Button(window, text="Post Comment", command=comment)
btn.grid(column=3, row=7)

sto.configure('W.TButton', font= ('calibri', 20, 'underline'),
 foreground='Green')

window.mainloop()
