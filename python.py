#Official player stats for 2019

players = [{
   'name': 'Julio Jones',
   'catches': 99,
   'targets': 157
   },
   {
   'name': 'Davante Adams',
   'catches': 83,
   'targets': 127
   },
   {
   'name': 'Michael Thomas',
   'catches': 149,
   'targets': 185
   },
]


for player in players:
   name = player["name"]
   catches = player["catches"]
   targets = player["targets"]
   catch_rate = catches/targets
   print(name + ' has a catch rate of ' + str(catch_rate))