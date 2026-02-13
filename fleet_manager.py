def init_database(): 
    global Names,Ranks,Divs,Ids
    Names = ["Kirk", "Troi", "Mccoy", "Sulu", "Harry"]
    Ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    Divs = ["Command", "Councillor", "Medical", "Command", "Operations"]
    Ids = ["0","1","2","3"] #Making all the lists of the characters, ranks, divs and Ids
    return Names, Ranks, Divs, Ids

def display_menu():
    name = input("What is your full name? ") # Get users full name
    print("=================================")
    print("Add Members : 1")
    print("Remove Members : 2")
    print("Update Rank : 3")
    print("Display Roster : 4")
    print("Search Crew : 5")
    print("Filter By Division : 6")
    print("Calculate Payroll : 7")
    print("Count Officers : 8")
    print("===========================================")
    print(f"{name} is currently logged in")
    print("===========================================")
    choice = input("What option do you want to select? ")
    return choice

def add_member():
    name = input("What is their name? ")
    rank = input("What is their rank? ")
    div = input("What is their division? ")
    while True:
        try:
            id = int(input("What is their ID? "))
            if id > 0:
                if id > int(Ids[-1]):
                    Ids.append(str(id))
                    Ranks.append(rank)
                    Names.append(name)
                    Divs.append(div)
                    break
                elif int(Ids[-2]) < id < int(Ids[-1]):
                    Ids.append(str(id))
                    Ranks.append(rank)
                    Names.append(name)
                    Divs.append(div)
                    break
                else:
                    print("Invalid ID")
                    continue
        except:
            print("Invalid")
            continue

             

def main():
    init_database()
    opt = display_menu()
    if opt == "1":
        add_member()

    print(Names)
    print(Ranks)
    print(Divs)
    print(Ids)
main()