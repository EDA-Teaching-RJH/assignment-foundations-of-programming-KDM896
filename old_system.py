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
        loading += 1 # bug fix 3- added loading += 1 so that it isnt an infinite loop because the value would have never increased to 5 to break the loop.
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #bug fix 1 - changed = to == becasue it was an assignment instead of a comparison. need to be comparison to see if the option is 1 being input by the user
            print("Current Crew List:")
            
            for i in range(len(n)):#bug fix 4- i changed the rage of the loop to be related to the length of the list so that any crew member can be added and included in the printed list instead of it being bound to 4 
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)#bug fix 5- added more appends so that when a new crew member is added all relevant information like rank and division is added to the lists so you can get the full information when you view crew.
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
                if rank == "Captain":#bug fix 10- changed if statement to check captain then commander indavidulally so it would give an accurate count of both ranks.
                    count = count + 1
                elif rank == "Commander":# bug fix 8- added an elif statement to check and count for commander rank as well so that it will count both ranks instead of just captain which was the only one being counted before becasue the if and or statement was stopping after checking for the captain only.
                    count += 1#buf fix 9- added count += 1 to seperatly check and count the commander rank.
                else:
                    count=count#bug fix 7- added count = count to the else statement so that if the rank is not captain or commander it will change the correct count and or rest back to zero after the ranks have been added.
            print(f"High ranking officers: {count}") #bug fix 6- alowing the count to be printed removing the inifinite loop by adding a f string which allows to count and print.
            
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

run_system_monolith() #bug fix 2- added brackets to allow the function to run as it calls it to excute instead of being referanced.
