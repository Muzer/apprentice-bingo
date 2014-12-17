#!/usr/bin/env python3
import sys
import random
import subprocess

# Plz pass numbe and names for names or anything else for things
# Outputs to bingo.tex/bingo.pdf

names=["Bianca",
       "Chiles",
       "Daniel",
       "Ella",
       "Felipe",
       "James",
       "Jemma",
       "Katie",
       "Lauren",
       "Lindsay",
       "Mark",
       "Nurun",
       "Pamela",
       "Robert",
       "Roisin",
       "Sanjay",
       "Sarah",
       "Scott",
       "Solomon",
       "Steven"]

interviews=["``I'm the best me I can be.''",
            "``I've come from nothing.''",
            "``I didn't need no education.''",
            "``I'm in this to win.''",
            "``Are you a one trick pony?''",
            "``You're not listening to me!''",
            "``The bottom line is [...]''",
            "``I'm a born leader!''",
            "``This was a disastrous interview.''",
            "``X is full of bullshit!''",
            "``It's so unfair!''",
            "``It says here on your CV [...]''",
            "``Please let me finish.''",
            "``You're interrupting me!''",
            "``I'm not a passenger.''",
            "``The gloves are coming off.''",
            "``You've got to man-up!''",
            "``I mean business.''",
            "``The sky's the limit.''",
            "``I'm exactly what it says on the tin''",
            "``CAN I JUST SAY...''",
            "``LOOK, [...]''",
            "``I don't want to hear from you any more/I'm fed up with hearing you.''",
            "``Shambles!''",
            "``110\%''",
            "``At the end of the day''",
            "Karen calls upon someones bullshit",
            "Running to phone in PJs",
            "A reference to a tough upbringing",
            "Lord Sugar makes a terrible terrible joke",
            "Fog happens to coincide with early morning minivans-driving-away-from-house shot",
            "Blatant discrepancy between fired candidate's clothing with departing taxi shots",
            "Candidate uses the third person",
            "Someone forgets to call Alan Sugar a lord",
            "Lord Sugar gets angry because someone forgets to call him a Lord",
            "Lord Sugar arrives unannounced into the house",
            "Lord Sugar talking from really far away in a building",
            "Lord Sugar talking from so far away, they've had to put him on a monitor",
            "Candidate has a breakdown and admits they aren't Superman",
            "Candidate compares self to Lord Sugar",
            "Candidate cries",
            "Candidate states that the day is the worst of their life",
            "``Rather you than me''",
            "Candidate makes impossible promise that interviewer calls on",
            "Interviewer insults candidate's background"]



things=["``I'm the best me I can be.''",
        "``I've come from nothing.''",
        "``I didn't need no education.''",
        "``Let me take charge.''",
        "``I could have done a better job, but didn't volunteer myself.''",
        "``I do this in my day job.''",
        "``I deserve to be project manager.''",
        "``I'm in this to win.''",
        "``This is the last time I want to see you here in the [elimination round].''",
        "``Are you a one trick pony?''",
        "``You're not listening to me!''",
        "``Failure is not an option.''",
        "``I knew we should've gone with my gut instead.''",
        "``The bottom line is [...]''",
        "``I'm a born leader!''",
        "``This was a disastrous task.''",
        "``X is full of bullshit!''",
        "Lord Sugar questioning his need for salesmen",
        "``It's so unfair!''",
        "``It says here on your CV [...]''",
        "``WHAT WENT WRONG!?!?!?!''",
        "``Please let me finish.''",
        "``I've got a girlfriend/boyfriend.''",
        "``You're interrupting me!''",
        "``I'm not a passenger.''",
        "``Nick tells me [...]''",
        "``The gloves are coming off.''",
        "``You've got to man-up!''",
        "``You lost us this task.''",
        "``A load of toot.''",
        "``I mean business.''",
        "``Lean mean selling machine.''",
        "``The sky's the limit.''",
        "``I'm exactly what it says on the tin''",
        "``You lost us the task''",
        "``Just give me one more chance''",
        "``CAN I JUST SAY...''",
        "``LOOK, [...]''",
        "``I'm an expert at this, trust me, it's my background''",
        "``They can't make a decision''",
        "``I can't lose in this task''",
        "``X feels threatened by me.''",
        "``I don't want to hear from you any more/I'm fed up with hearing you.''",
        "``I take responsibility''",
        "``I'm going to give you the benefit of the doubt.''",
        "``Shambles!''",
        "``110\%''",
        "``At the end of the day''",
        "Karen raises eyebrow",
        "Karen rolls eyes",
        "Karen calls upon someones bullshit",
        "Task-based pun",
        "Running to phone in PJs",
        "Nick sneers (gives the weird nose wrinkling thingy)",
        "Flirty sales patter fails",
        "Candidates become romantically involved",
        "A reference to a tough upbringing",
        "Lord Sugar gets annoyed about people losing him money",
        "The prize for winning a task involves going in a helicopter",
        "People have to run because they have a stupid deadline",
        "Lord Sugar makes a terrible terrible joke",
        "DOUBLE FIRING",
        "Fog happens to coincide with early morning minivans-driving-away-from-house shot",
        "Obvious product placement despite the BBC",
        "Blatant discrepancy between fired candidate's clothing with departing taxi shots",
        "Candidate uses the third person",
        "Someone forgets to call Alan Sugar a lord",
        "Lord Sugar gets angry because someone forgets to call him a Lord",
        "A candidate chases someone down the street to sell them something",
        "Lord Sugar arrives unannounced into the house",
        "Someone cancels a telephone call in the middle of a conversation",
        "Lord Sugar talking from really far away in a building",
        "Lord Sugar talking from so far away, they've had to put him on a monitor",
        "Project Manager drank the Kool-Aid and now fanatically believes in \#TEAM :'D",
        "Project Manager has a breakdown and admits they aren't Superman",
        "Awkward moment when candidates at the house slag off the person who just returned",
        "Candidate compares self to Lord Sugar"]

dim = int(sys.argv[1])
thing = sys.argv[2]

with open('bingo.tex', 'w') as f:
    f.write(r"""\documentclass[a4paper,12pt]{article}
\usepackage{tabularx}
\title{Apprehended Swalies bingo}
\author{Murray Colpman, Tom Leese, Piers Morgans-Wicks}
\setlength{\tabcolsep}{18pt}
\renewcommand{\arraystretch}{2}
\begin{document}
\maketitle
\section{Bingo!}
\begin{center}
\begin{tabularx}{\linewidth}{|""")

    for i in range(dim):
        f.write(r"X|")
    f.write(r"""}
\hline
""")

    for i in range(dim):
        for j in range(dim):
            item = random.choice(names if thing == "names" else
                    interviews if thing == "interviews" else things)
            (names if thing == "names" else interviews if thing == "interviews"
                    else things).remove(item)
            f.write(item)
            if j + 1 != dim:
                f.write(" & ")
        f.write(r""" \\ \hline
""")
    f.write(r"""\end{tabularx}
\end{center}
\end{document}
""")

subprocess.call(["pdflatex", "bingo.tex"])
