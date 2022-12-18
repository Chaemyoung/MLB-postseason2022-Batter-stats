import pandas as pd

import os


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


df = pd.read_csv('batter_stats.csv')

finished = False

while not finished:
  print("Welcome to MLB POSTSEASON2022 PLAYER HITTING STATS")
  userChooseOption = input(
    "Are you looking for 'player stats?' or 'ranking chart?': ")
  if userChooseOption == 'player stats':
    userName = str(input("Name?: "))
    try:
      value1 = df.index[df['Name'] == userName].tolist()
      value2 = df.loc[value1[0], 'Name']
      if userName == value2:
        extractByName = df.loc[df['Name'].str.contains(userName).idxmax()]
        print("\nThe player's stats: \n", extractByName.to_string())
    except:
      print('\nThere is no player with that name!')
    # value2 = df.loc[value1[0], 'Name']
    # print(userName)

    # elif userName != value2:
    #   print("Check your spelling again")

  elif userChooseOption == 'ranking chart':
    keywords = [
      "AB", "Run", "Hit", "Double", "Triple", "Homerun", "RBI", "BB", "SO",
      "SB", "CS", "AVG", "OBP", "SLG", "OPS"
    ]
    print(', '.join(keywords))
    try:
      userStatTitle = str(
        input("Which stats? Choose one of those: ")).strip(' ')
      stat = df[['Name', userStatTitle]]
      df_sorted_by_values = stat.sort_values(by=userStatTitle, ascending=False)
      print("\n Here is the ranking: ")
      print(df_sorted_by_values.to_string(index=False))
    except:
      print('\numm maybe spelling wrong?')

    #finish_or_not = str(input("\nDo you want to try again?('Yes' or 'No'): "))

  else:
    print("Check your spelling again")

  finish_or_not = str(input("\nDo you want to try again?('Yes' or 'No'): "))
  if finish_or_not == 'no':
    finished = True
    print('bye-bye')
  elif finish_or_not == 'yes':
    finish_or_not = False
    cls()
