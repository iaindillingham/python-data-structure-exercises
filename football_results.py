import collections
import functools
import itertools

# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.

results = [
    {"Austria": 0, "Hungary": 2},
    {"Portugal": 1, "Iceland": 1},
    {"Iceland": 1, "Hungary": 1},
    {"Portugal": 0, "Austria": 0},
    {"Iceland": 2, "Austria": 1},
    {"Hungary": 3, "Portugal": 3},
]

print("There were {} matches in the group".format(len(results)))

sorter = functools.partial(sorted, key=lambda x: x[1], reverse=True)

# TODO: Write code to answer the following questions:

match_goals = sorter([(r.keys(), sum(r.values())) for r in results])
print("The match with the most goals was", "?")
print("The match with the fewest goals was", "?")

team_goals = collections.defaultdict(list)
for team, match_goals in itertools.chain(*(r.items() for r in results)):
    team_goals[team].append(match_goals)

team_total_goals = {team: sum(goals) for team, goals in team_goals.items()}
team_total_goals = sorter(team_total_goals.items())
print("The team with the most total goals was", "?")
print("The team with the fewest total goals was", "?")


def get_result_as_points(result_as_goals):
    teams, goals = zip(*result_as_goals.items())
    delta = goals[0] - goals[1]
    points = (1, 1) if delta == 0 else (3, 0) if delta > 0 else (0, 3)
    result_as_points = dict(zip(teams, points))
    return result_as_points


results_as_points = [get_result_as_points(r) for r in results]

team_points = collections.defaultdict(list)
for team, match_points in itertools.chain(*(r.items() for r in results_as_points)):
    team_points[team].append(match_points)

team_total_points = {team: sum(points) for team, points in team_points.items()}
team_total_points = sorter(team_total_points.items())
print("The team with the most points was", "?")
print("The team with the fewest points was", "?")

# TODO (extra): Write code to compute and display a league table
