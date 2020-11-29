print('''
*******************************************************************************
  (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You have arrived at the island. As you get on the shore, the pathnway divides into two.")
path1 = input("Left or right. Which way would you like to go?").lower()

if path1 == 'left':
    print('As you start walking left, you see the trail split again.')
    print('One trail runs from a forest. the other through a clean apparently scenic route')
    path2= input('Forest or clear?').lower()
    if path2 == "forest":
      print('You walk through the forest but you get attacked by snacks. Game over')
    elif path2 == 'clear':
      print('This path was full of quicksand. Game over')
    else:
      print("Incorrect selection. Game over")
elif path1 == 'right':
  print("As you start walking right, a stream of water appears.")
  print("The only options available are to swim through the water or use a tree to swing across.")
  path2 = input("Swim or swing?").lower()
  if path2 == 'swim':
    print('The water was infested with crocodiles. You have been eaten.')
  elif path2 == 'swing':
      
    print('You have made it across the water.')
    print('As you start walking, you arrive at a strange shed with two doors.')
    print('One of the doors is blue. The other is gold.')
    path3 = input('Which one would you like to pick? blue or gold ').lower()
      
    if path3 == "blue":
      print ('You found the treasure. The chest is full of stocks of blockbuster')
    elif path3 == "gold":
      print('All that glitters is not gold. The door was rigged to blow. Game over')
    else:
      print('Incorrect selection')

  else:
    print('Incorrect input, the game will end')
else:
  print('Incorrect input, the game will end')


