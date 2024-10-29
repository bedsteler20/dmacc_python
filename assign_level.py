def novice():
    return 50

def beginner():
    return 150

def experienced():
    return 300

def advanced():
    return 500

switch = {
    "N": novice,
    "B": beginner,
    "E": experienced,
    "A": advanced
}
value = "N"

print(switch[value]()) 
