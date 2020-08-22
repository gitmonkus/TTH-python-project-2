''' This program searches data in a list and displays
the statistical information for a chosen team
'''
# import constants.py file, so we can pull in the data
import constants
# import copy to deepcopy the lists from constants so as to not mutate original lists
import copy

# variables
border_line = "=" * 110
dashed_line = "-" * 110


def clean_data():
    ''' Creates a new player list to be searched later
    Height changed to int and experience changed to True or False
    '''
    storage_list = []
    new_player_list = copy.deepcopy(constants.PLAYERS)
    index_range = range(len(new_player_list))
    for i in index_range:
        storage_list.append(new_player_list[i]['height'][:2])
    storage_list = [int(i) for i in storage_list]
    help = 0
    for i in storage_list:
        new_player_list[help]['height'] = i
        help += 1
    for i in index_range:
        if new_player_list[i]['experience'] == 'YES':
            new_player_list[i]['experience'] = True
        else:
            new_player_list[i]['experience'] = False
    for i in index_range:
        new_player_list[i]['guardians'] = new_player_list[i]['guardians'].split(" and ")
    return new_player_list
 

def balance_teams(team1, team2, team3, player_list):
    ''' # Create a fnal_list with experienced and inexperienced players equally assigned to teams '''
    yes = 0
    yes1 = 0
    yes2 = 0
    no = 0
    no1 = 0
    no2 = 0
   
    for i in range(18):
        player_list[i]['team'] = ''
        if player_list[i]['experience'] == True and yes < 3 and player_list[i]['team'] == '':        
            player_list[i]['team'] = team1
            yes += 1
        elif player_list[i]['experience'] == False and no < 3 and player_list[i]['team'] == '':       
            player_list[i]['team'] = team1
            no += 1
        elif player_list[i]['experience'] == True and yes1 < 3 and player_list[i]['team'] == '':       
            player_list[i]['team'] = team2
            yes1 += 1
        elif player_list[i]['experience'] == False and no1 < 3 and player_list[i]['team'] == '':       
            player_list[i]['team'] = team2
            no1 += 1
        elif player_list[i]['experience'] == True and yes2 < 3 and player_list[i]['team'] == '':       
            player_list[i]['team'] = team3
            no2 += 1
        elif player_list[i]['experience'] == False and no2 < 3 and player_list[i]['team'] == '':       
            player_list[i]['team'] = team3
            no2 += 1
        else:
            player_list[i]['team'] = team3
    return player_list


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
                print("  Have a GREAT day!  Remember to check out the Team Stats Tool often, as we are always adding amazing stats!")
                print(border_line)
                print()
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


def data_find_count_2000(key_search, value_search, key_find, key_value):
    ''' # Searches the final_list for a value related to a team and returns the count ''' 
    how_many = 0
    index_range = range(len(final_list))
    for i in index_range:
        if value_search in final_list[i][key_search] and final_list[i][key_find] == key_value:
            how_many += 1
        elif value_search in final_list[i][key_search] and final_list[i][key_find] == key_value:
            how_many += 1
    return how_many
    

def data_average_2000(key, value, key_return):
    ''' # Pulls data for height, stores in storage_list, and returns the average ''' 
    storage_list = []
    index_range = range(len(final_list))
    for i in index_range:
        if value in final_list[i][key]:
            storage_list.append(final_list[i][key_return])
    return round(sum(storage_list) / len(storage_list))


def data_bank_2000(key, value, key_return):
    ''' # For a given team, return the values associated with a key '''
    storage_list = []
    index_range = range(len(final_list))
    if key_return == 'name':
        for i in index_range:
            if value in final_list[i][key]:
                storage_list.append(final_list[i][key_return])
        return ', '.join(storage_list)
    else:
        for i in index_range:
            if value in final_list[i][key]:
                storage_list.extend(final_list[i][key_return])
        return ', '.join(storage_list)
                
             
def team_statistics(team):
    print()
    print(border_line)
    print("Team {} Stats".format(team))
    print(border_line)
    print()
    print("Total players:       {}".format(data_count_2000('team', team)))
    print("Total experienced:   {}".format(data_find_count_2000('team', team, 'experience', True)))
    print("Total inexperienced: {}".format(data_find_count_2000('team', team, 'experience', False)))
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
    new_list = copy.deepcopy(constants.TEAMS)
    # Call clean_data function and save in player_list to be used next by the balance_teams function
    player_list = clean_data()
    #Call the balance_teams function and pass in the teams
    final_list = balance_teams(new_list[0], new_list[1], new_list[2], player_list)
    print()
    print(border_line)
    print("BASKETBALL TEAM STATS TOOL! -- Your #1 place for up-to-date stats!")
    print(border_line)
    print()
    print(dashed_line)
    print("    MAIN MENU")
    print(dashed_line)
    print()
    first_menu()

    
   
        
    
            