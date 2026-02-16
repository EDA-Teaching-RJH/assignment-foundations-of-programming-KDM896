n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0

            for rank in r:
                if rank == "Captain":
                    count = count + 1
                elif rank == "Commander":
                    count += 1
                else:
                    count=count
            print(f"High ranking officers: {count}") 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()
def display_roster(Names, Ranks, Divs, Ids):
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