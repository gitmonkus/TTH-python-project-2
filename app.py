''' This program searches data in a list and displays
the statistical information for a chosen team
'''
# import constants.py file, so we can pull in the data
import constants


# create a key: value pair list for the teams
new_list = [{'team': i} for i in constants.TEAMS]

# add players to new list, so that we can assign players to the teams
storage_list = constants.PLAYERS

# variables
border_line = "=" * 100
dashed_line = "-" * 100
new_player_list = {}
final_list = []
player_count = range(len(storage_list) // len(new_list))

# Create a fnal_list with players assigned to teams
for i in player_count:
    for i in new_list:
        new_player_list = storage_list.pop()
        new_player_list.update(i) 
        final_list.append(new_player_list)


def first_menu():
    while True:
        print("Here are your choices")
        print()
        print("  1. Display Team Stats")
        print("  2. Quit")
        print()
        try:
            first_menu_answer = int(input("Enter an option: "))
        except ValueError:
            print()
            print("-- Doesn't look like a 1 or 2 -- try again.")
            print()
        else:
            if first_menu_answer < 1 or first_menu_answer > 2:
                print()
                print("-- Doesn't look like a 1 or 2 -- try again.")
                print()
            elif first_menu_answer == 1:
                second_menu()
                break
            elif first_menu_answer == 2:
                print()
                print(border_line)
                print("Check out the Team Stats Tool often.  We are always adding amazing stats.")
                print(border_line)
                break


def second_menu():
    while True:
        print()
        print(dashed_line)
        print("    Pick a team to display their stats")
        print(dashed_line)
        print()
        print("  1. Panthers")
        print("  2. Bandits")
        print("  3. Warriors")
        print()
        try:
            team_menu_answer = int(input("Enter an option: "))
        except ValueError:
            print()
            print("-- Doesn't look like a 1, 2, or 3 -- try again.")
        else:
            if team_menu_answer < 1 or team_menu_answer > 3:
                print()
                print("-- Doesn't look like a 1, 2, or 3 -- try again.")
            elif team_menu_answer == 1:
                team_statistics('Panthers')
                break
            elif team_menu_answer == 2:
                team_statistics('Bandits')
                break
            elif team_menu_answer == 3:
                team_statistics('Warriors')
                break



def data_count_2000(key, value):
    ''' # Searches the final_list and returns the player count in a team '''
    how_many = 0
    index_range = range(len(final_list))
    for i in index_range:
        if value in final_list[i][key]:
            how_many += 1
    return(how_many)


def data_find_count_2000(key_search, value_search, key_find, value_find):
    ''' # Searches the final_list for a value related to a team and returns the count ''' 
    how_many = 0
    index_range = range(len(final_list))
    for i in index_range:
        if value_search in final_list[i][key_search] and value_find in final_list[i][key_find]:
            how_many += 1
    return(how_many)


def data_average_2000(key, value, key_return):
    ''' # Pulls data for height, strips extra text, turns string into int, places in num_list and returns the average ''' 
    storage_list = []
    num_list = []
    index_range = range(len(final_list))
    for i in index_range:
        if value in final_list[i][key]:
            storage_list.append(final_list[i][key_return])
    for i in range(len(storage_list)):
        for i in storage_list:
            new_list = storage_list.pop()
            new_list = new_list[:2]
            num_list.append(new_list)
    num_list = [int(i) for i in num_list]
    return round(sum(num_list) / len(num_list))


def data_bank_2000(key, value, key_return):
    ''' # For a given team, return the values associated with a key '''
    storage_list = []
    index_range = range(len(final_list))
    for i in index_range:
        if value in final_list[i][key]:
            storage_list.append(final_list[i][key_return])
    return '\n'.join(storage_list)
                
             
def team_statistics(team):
    print()
    print(border_line)
    print("Team {} Stats".format(team))
    print(border_line)
    print()
    print("Total players:       {}".format(data_count_2000('team', team)))
    print("Total experienced:   {}".format(data_find_count_2000('team', team, 'experience', 'YES')))
    print("Total inexperienced: {}".format(data_find_count_2000('team', team, 'experience', 'NO')))
    print("Average height:      {} inches".format(data_average_2000('team', team, 'height')))
    print()
    print(dashed_line)
    print("Players on Team")
    print(dashed_line)
    print()
    print("{}".format(data_bank_2000('team', team, 'name')))
    print()
    print(dashed_line)
    print("Guardians")
    print(dashed_line)
    print()
    print("{}".format(data_bank_2000('team', team, 'guardians')))
    print()
    input("Press ENTER to continue")
    first_menu()
    

if __name__ == "__main__":
    print()
    print(border_line)
    print("BASKETBALL TEAM STATS TOOL")
    print(border_line)
    print()
    print(dashed_line)
    print("    MAIN MENU")
    print(dashed_line)
    print()
    first_menu()
    
   
        
    
            