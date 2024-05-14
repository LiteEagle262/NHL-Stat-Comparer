import requests

print("Provide the 2 teams you would like to compare below:\n\n") #\n is newline

team1 = input("Team 1 :> ")
team2 = input("Team 2 :> ")
print("\n\n")

def get_team_stats(team_name):
    """Get the following stats from a generic team name like "sharks":

    Data Points:
    -- Face off win percent
    -- Goals against per game
    -- Goals for per game
    -- Penalty kill percent
    -- Point percent
    -- Power play percent
    -- Shots against per game
    -- Shots for per game

    Args:
    team_name: team name.

    Returns:
    A dictionary of the team stats.
    """

    r = requests.get("https://api.nhle.com/stats/rest/en/team/summary?") # send a GET request to the official NHL api endpoint

    data = r.json()['data']
    team_name = team_name.lower() # lowering so that caps/lower dont matter

    for team in data:
        if team_name in team.get('teamFullName', '').lower(): # ↓↓
            '''
            ↑↑ because im to lazy to type city name, it searches for if anything in the name you type, ex: "sharks"
            then it takes the key for where its listed in order to find the other stats
            '''
            stats = {
                'Face off win percent': team.get('faceoffWinPct'),
                'Goals against per game': team.get('goalsAgainstPerGame'),
                'Goals for per game': team.get('goalsForPerGame'),
                'Penalty kill percent': team.get('penaltyKillPct'),
                'Point percent': team.get('pointPct'),
                'Power play percent': team.get('powerPlayPct'),
                'Shots against per game': team.get('shotsAgainstPerGame'),
                'Shots for per game': team.get('shotsForPerGame')
            }
            return stats # returns all the stats in a dictionary cus easier to parse through then having variables for everything
    raise ValueError(f"Team with name '{team_name}' not found.") # raise a error bc it saves like 3 lines instead of writing an if statement

team_stats = get_team_stats("new york rangers")

def print_stats(stats1, team_name1, stats2, team_name2):
    """Very OD print stats

    Data Points:
    -- Face off win percent
    -- Goals against per game
    -- Goals for per game
    -- Penalty kill percent
    -- Point percent
    -- Power play percent
    -- Shots against per game
    -- Shots for per game

    Args:
    team_name: team name.
    stats1: team 1's stats from get_team_stats() function
    team_name1: first team name from team1 variable
    team_name2: second team name from team2 variable
    stats2: team 2's stats from get_team_stats() function

    prints all data points in a fancy looking box so its easier to visualise the stats
    compares stats automaticly to see what team has an edge for eeach stat
    
    sometimes the api returns none for certain stats so returns N/A if a edge cant be found.
    """
    
    print(f"{team_name1} vs {team_name2}")
    print("-" * 80) # print 80 - characters for the top line
    print(f"{'Stat':25} | {team_name1:25} | {team_name2:25} | {'Edge'}")
    print("-" * 80) # print 80 - characters for the bottum part of the top line seperator
    for stat in stats1.keys(): # same as a regular for loop, .keys just iterates through the dictonary keys ex the "team" in "team":"flyers"
        value1 = round(stats1[stat], 2) if isinstance(stats1[stat], float) else stats1[stat]
        value2 = round(stats2[stat], 2) if isinstance(stats2[stat], float) else stats2[stat]
        edge = round(value2 - value1, 2) if isinstance(value1, float) and isinstance(value2, float) else 'N/A'
        print(f"{stat:25} | {str(value1):25} | {str(value2):25} | {str(edge)}") #converts all statistic values to strings andd places them into format
    print("-" * 80) # print 80 - characters for the bottum line
    print(f"{'Edge Explanation':25} | Positive value indicates an edge for {team_name2}.")
    print(f"{'':25} | Negative value indicates an edge for {team_name1}.")
    print("-" * 80) # print 80 - characters for the bottum bottum line
    
    '''
    for clarification of the :25 as well thats just minimum length so it makes the box sizes not mess up
    isinstance checks if a value is a float just making sure its not "None" etc
    round just rounds decimals for readability to the nearest hundredth
    '''

print_stats(get_team_stats(team1), team1, get_team_stats(team2), team2) # call the function using the other functions and variables.