repetitive_games=[]
boring_games=[]
good_games=[]
a=input("Boring='b'\ngood='g'\nrepetitive='r':\n")
while a=='b'or a=='g' or a=='r':
    c=input("Enter the name of the game:")
    if c.lower() in repetitive_games or c.lower() in good_games or c.lower() in boring_games:
        print("This value is already in the list")
    else:
        c=c.lower()
        if a=='r':
            repetitive_games.append(c)
        elif a=='b':
            boring_games.append(c)
        else:
            good_games.append(c)
    a=input("Boring='b'\ngood='g'\nrepetitive='r'(if you want to exit, just press Enter):\n")
print(f"Good Games: {good_games}")
print(f"Repetitive Games: {repetitive_games}")
print(f"Boring Games: {boring_games}")
