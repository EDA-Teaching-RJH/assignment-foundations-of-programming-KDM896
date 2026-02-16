def init_database(): 
    global Names,Ranks,Divs,Ids
    Names = ["Kirk", "Troi", "Mccoy", "Sulu", "Harry"]
    Ranks = ["Ensign","Lieutenant","Lieutenant Commander","Commander","Captain"]
    Divs = ["Command", "Councillor", "Medical", "Command", "Operations"]
    Ids = ["0","1","2","3","4"] #Making all the lists of the characters, ranks, divs and Ids
    return Names, Ranks, Divs, Ids

def display_menu():
    name = input("What is your full name? ") # Get users full name to define whos logged in (repeats)
    print("----------------------------------------------")
    print("Add crew Members : 1")
    print("Remove crew Members : 2")
    print("Update crew Rank : 3")
    print("Display crew Roster : 4")
    print("Search Crew : 5")
    print("Filter By Division : 6")
    print("Calculate Payroll : 7")
    print("Count Officers : 8")
    print("----------------------------------------------")
    print(f"{name} is the current user logged in")
    print("----------------------------------------------")
    choice = input("What option do you want to select? ")
    return choice

def add_member():
    name = input("What is their name? ")
    Rank_list = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    while True:
        rank = input("What is their rank? ")
        if rank in Rank_list:
            break
        else:
            print("Invalid rank try again")
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
                elif rank not in Ranks:
                    print("Invalid rank try again")
                    continue
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

def remove_member():# removing a member from the list by using stored IDs then deleting all information related.
    id = input("What is the ID of the member you want to remove? ")
    if id in Ids:
        index = Ids.index(id)
        del Ids[index]
        del Ranks[index]
        del Names[index]
        del Divs[index]
    else:
        print("invalid ID try again")         

def update_rank():
    valid_ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    Id = input("what is the ID of the member you want to update? ")
    if Id in Ids:
        index = Ids.index(Id)
        new_rank = input("what is the rank you want to change to: Captain, Commander, Lieutenant Commander, Lieutenant and Ensign?")
    if new_rank in valid_ranks: 
        Ranks[index] = new_rank
    else:        
        print("invalid rank try again")

def display_roster():
    print("Crew Roster:")
    for i in range(len(Names)):
        print(f"Name: {Names[i]}, Rank: {Ranks[i]}, Division: {Divs[i]}, ID: {Ids[i]}")
        
def search_crew():
    search_crew = input("What is the name of the crew member you want to search for? ")
    if search_crew in Names:
        index = Names.index(search_crew)
        print(f"Name: {Names[index]}, Rank: {Ranks[index]}, Division: {Divs[index]}, ID: {Ids[index]}")
    else:        print("Crew member does not exist.")

def filter_division():
    filter_division = input("What division do you want to filter by? ")
    for i in range(len(Divs)):
        if Divs[i] == filter_division:
            print(f"Name: {Names[i]}, Rank: {Ranks[i]}, Division: {Divs[i]}, ID: {Ids[i]}")

def calculate_payroll():
    total_payroll = 0
    for rank in Ranks:
        if rank == "Captain":
            total_payroll += 100000
        elif rank == "Commander":
            total_payroll += 75000
        elif rank == "Lieutenant Commander":
            total_payroll += 50000
        elif rank == "Lieutenant":
            total_payroll += 30000
        elif rank == "Ensign":
            total_payroll += 20000
    print(f"Total Payroll: ${total_payroll}")

def count_officers():
    count_officers = 0
    for name in Names:
        if name in Names:
            count_officers += 1
    print(f"Total Officers: {count_officers}")

def main():
    init_database()
    opt = display_menu()
    valid_ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    while True:
        if opt == "1":
            add_member()
        elif opt == "2":
            remove_member()
        elif opt == "3":
            update_rank()
        elif opt == "4":
            display_roster()
        elif opt == "5":
                search_crew()
        elif opt == "6":
                filter_division()
        elif opt == "7":                
            calculate_payroll()
        elif opt == "8":
            count_officers()
        opt = display_menu()
    
        
main()

