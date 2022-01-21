# Cover Letter Generator v1.0
# Authored By Mark Minchoff

# import mods and libs
import os, sys

greeting = "You'll Be Asked A Series of Questions To Complete This Form"
print((greeting.upper))

input("Press 'Enter' to Start") # kicks off the program

name = input('What Is Your Name?:')
company = input('What Company Are You Applying To?:') # user selects their potential company
posi = input('What Position Are You Applying To?:') # user selects their potential position
cover = input('What Should We Call This Cover Letter?:') # user selects filename to save as WITH EXTENSION

quit = input('Do You Wish To Continue? Yes/No Only:') # gives user the chance to bail out

# code for system to exit if any of the spellings of 'no' are picked
if quit in ('no', 'NO', 'No', 'nO'):
    sys.exit()

# meat of the code - opens blank file, writes inputs, and saves file
else:
    try:
        with open(f'{cover}', 'w') as f:
            f.write(f"""Dear Hiring Manager,\n

I find myself to be a determined professional seeking the chance to succeed at {company}.  I feel like I could be a good fit for the {posi} position.\n

If you are interested in my previous employment and would like me to elaborate my skill sets I will be more than happy to schedule a meeting with you. I am certain that I can be an asset in any position requiring hard work, enthusiasm and reliability.\n

I look forward to hearing from you. The enclosed resume lists all of my relevant experience and qualifications. Due to their privacy I will only submit references once I am interviewed.\n

Thank you for your time and consideration.\n

Sincerely,\n
{name}""")
