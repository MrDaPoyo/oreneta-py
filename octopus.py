import time

# spawn(Octopus.friend(1))
# spawn(Octopus.friend(2))
# hide(Octopus.friend(2))

print("Octopus: I'm an octopus! =;O;=")
time.sleep(1)
print("...")
time.sleep(2)
x = input("Octopus: Are you an octopus? =;v;= (Yes I am!/No sorry)\nYou: ")
if "y" in x or "Y" in x:
    print("\nOctopus: Oh, really? Me too! \;u;/")
    time.sleep(2)
    print("Octopus: I'm kinda alone tho. I once had a friend, but she left =;o;=")
    time.sleep(2)
    print("I wish you could help me to find her...")
else:
    print("Sad octopus: Aww =;n;=")