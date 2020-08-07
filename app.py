import constants


border_line = "=" * 50
dashed_line = "-" * 50
new_player_list = {}
final_list = []

new_list = [{'team': i} for i in constants.TEAMS]
storage_list = constants.PLAYERS

player_count = range(len(storage_list) // len(new_list))

for i in player_count:
    for i in new_list:
        new_player_list = storage_list.pop()
        new_player_list.update(i) 
        final_list.append(new_player_list)

# for i, item in enumerate(final_list):
#     print(f'{i}. {item}')

def datacount_2000(key, value):
    how_many = 0
    index_range = range(17)
    for i in index_range:
        if value in final_list[i][key]:
            how_many += 1
    return(how_many)

def datafindcount_2000(key_search, value_search, key_find, value_find):
    how_many = 0
    index_range = range(17)
    for i in index_range:
        if value_search in final_list[i][key_search] and value_find in final_list[i][key_find]:
            how_many += 1
    return(how_many)

def databank_2000(key, value, key_return):
    storage_list = []
    index_range = range(17)
    for i in index_range:
        if value in final_list[i][key]:
            storage_list.append(final_list[i][key_return])
    return '\n'.join(storage_list)


def dataaverage_2000(key, value, key_return):
    storage_list = []
    num_list = []
    index_range = range(17)
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
    





# key = 'name'
# if key in final_list[0]:
#     print('YES')
# else:
#     print('NO')

# for i, item in enumerate(final_list):
#     print(f'{i}. {item}')

# print(final_list[0]['name'])

# print(final_list[0]['team'])



if __name__ == "__main__":
    print(border_line)
    print("BASKETBALL TEAM STATS TOOL")
    print(border_line)
    print()
    print("**** MENU ****")
    print()
    print("Here are your choices")
    print()
    print("  1. Display Team Stats")
    print("  2. Quit")
    print()
    first_menu_answer = int(input("Enter an option: "))
    if first_menu_answer == 1:
        print()
        print("  1. Panthers")
        print("  2. Bandits")
        print("  3. Warriors")
        print()
        team_menu_answer = int(input("Enter an option:"))
        if team_menu_answer == 1:
            print()
            print(border_line)
            print("Team Panthers Stats")
            print(border_line)
            print()
            print("Total players: {}".format(datacount_2000('team', 'Panthers')))
            print("Total experienced: {}".format(datafindcount_2000('team', 'Panthers', 'experience', 'YES')))
            print("Total inexperienced: {}".format(datafindcount_2000('team', 'Panthers', 'experience', 'NO')))
            print("Average height: {} inches".format(dataaverage_2000('team', 'Panthers', 'height')))
            print()
            print(dashed_line)
            print("Players on Team")
            print(dashed_line)
            print()
            print("{}".format(databank_2000('team', 'Panthers', 'name')))
            print()
            print(dashed_line)
            print("Guardians")
            print(dashed_line)
            print()
            print("{}".format(databank_2000('team', 'Panthers', 'guardians')))
            print()
            print("Press ENTER to continue")

        if team_menu_answer == 2:
            print("Team Bandits stats")
        if team_menu_answer == 3:
            print("Team Warriors stats")
    
    if first_menu_answer == 2:
        print("Check out the roster often, as we're always adding stats.")