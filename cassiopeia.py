import cassiopeia

cassiopeia.set_riot_api_key("RGAPI-3a22ebe5-32f7-454f-8c4b-3675c25872fa")
gamemode = cassiopeia.Queue.ranked_solo_fives

region = "NA"
leaderboard = cassiopeia.get_challenger_league(queue=gamemode, region=region)

for player in leaderboard:
  print(player.summoner.name)