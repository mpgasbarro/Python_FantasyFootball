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

def get_catch_rate(player):
    if type(player) != dict:
       print('You need to pass in a dictionary!')
       return
    else:
       pass

    catches = player['catches']
    targets = player['targets']

    if catches > targets:
       print('You can not have more catches than targets')
       return
    else:
       pass

    catch_rate = catches/targets

    return catch_rate


for player in players:
   name = player["name"]
   catches = player["catches"]
   targets = player["targets"]
   catch_rate = get_catch_rate(player)
   print(name + ' has a catch rate of ' + str(catch_rate))


julio = players[0]
julios_catch_rate = get_catch_rate(julio)

get_catch_rate(players)
print(julios_catch_rate)


class Player:

  def __init__(self, name, pos, catches, targets, rushing_attempts, rushing_yds):
    self.name = name
    self.pos = pos
    self.catches = catches
    self.targets = targets
    self.rushing_attempts = rushing_attempts
    self.rushing_yds = rushing_yds

  def catch_rate(self):
    return self.catches/self.targets
   
  def yards_per_carry(self):
    return self.rushing_yds/self.rushing_attempts
  
  def efficiency(self):
    return {
      'yards_per_carry': self.yards_per_carry(),
      'catch_rate': self.catch_rate()
    }


julio = Player('Julio Jones', 'WR', 99, 157, 2, -3)

print(julio.catches)
print(julio.catch_rate())
print(julio.yards_per_carry())
print(julio.efficiency())