# in this riddle we will find a thief

# SCENARIO:
# the was a robbery last night in the factory
# and the thief was almost cought by the watchman
# but he was so lucky to evade.
# The watchman has seen the theif in a dark area, couln't identify who is he.
# But he got some signs about the thief.

from pickle import TRUE


clue1 = "Head is bald"
clue2 = "He has a golden watch"

# Number of workers in the factory
no_of_workers = 10

# the watchman informs the management
# and the management calls all the workers to the hall

# list of workers present in the hall
workers = [
    #worker 1
    {
        "name" : "W1",
        "clue1" : False,
        "clue2" : True
    },
      {
        "name" : "W2",
        "clue1" : False,
        "clue2" : True
    },
        {
        "name" : "W3",
        "clue1" : False,
        "clue2" : False
    },
          {
        "name" : "W4",
        "clue1" : False,
        "clue2" : True
    },
            {
        "name" : "W5",
        "clue1" : False,
        "clue2" : True
    },
              {
        "name" : "W6",
        "clue1" : False,
        "clue2" : True
    },
                {
        "name" : "W7",
        "clue1" : False,
        "clue2" : True
    },
                  {
        "name" : "W8",
        "clue1" : True,
        "clue2" : True
    },
                  
                     {
        "name" : "W9",
        "clue1" : False,
        "clue2" : True
    },
                     
                        {
        "name" : "W10",
        "clue1" : True,
        "clue2" : True
    },
    
]


checked=0

# here we are looping on number of workers to check clue1 and clue2
while checked < no_of_workers:
    
    worker = workers[checked]
    
    if worker['clue1'] == True:
        if worker['clue2']  == True:
            print("Thief might be: ", worker['name']) 
    
    
    checked = checked + 1
    
    # print("Checked", checked)

