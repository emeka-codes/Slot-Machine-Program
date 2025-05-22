import random
fruits= ['🍉', '🍌', '🍎', '🍋', '🥥']

is_running= True
balance= 100000
def random_fruit():
   global balance
   selected_fruits= []

   for currentValue in range(3):
      each_random_fruit= random.choice(fruits)
      selected_fruits.append(each_random_fruit)

   for currentFruits in selected_fruits:
      print(currentFruits, end=' ')
   print()

   if '🍉' in selected_fruits and selected_fruits[0]==selected_fruits[1]==selected_fruits[2]:
      
      winnings_one= user_bet*3
      balance += winnings_one
      print(f'You won N{winnings_one}')

   elif '🍌' in selected_fruits and selected_fruits[0]==selected_fruits[1]==selected_fruits[2]:
      winnings_two= user_bet*2
      balance += winnings_two
      print(f'You won N{winnings_two}')

   elif '🍎' in selected_fruits and selected_fruits[0]==selected_fruits[1]==selected_fruits[2]:
      winnings_three= user_bet*4
      balance += winnings_three
      print(f'You won N{winnings_three}')

   elif '🍋' in selected_fruits and selected_fruits[0]==selected_fruits[1]==selected_fruits[2]:
      winnings_four= user_bet*5
      balance += winnings_four
      print(f'You won N{winnings_four}')

   elif '🥥' in selected_fruits and selected_fruits[0]==selected_fruits[1]==selected_fruits[2]:
      winnings_five= user_bet*6
      balance += winnings_five
      print(f'You won N{winnings_five}')

   else:
      balance -= user_bet
      print('You Lose')
   print(f'Your remaining balance is {balance}')
      
      

while is_running:
   user_bet= int(input('How much do you want to bet?: '))
   random_fruit()
   decision= input('Do you want to continue playing (Y/N)?: ').upper()
   if decision == 'Y':
      continue
   else:
      is_running= False

