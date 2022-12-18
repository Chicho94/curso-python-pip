import random
#opciones que puede elegir la computadora
machines_options = ("piedra", "papel", "tijera")

#resultados del juego
rules = {"piedra": {"papel":"Derrota", "tijera":"Victoria", "piedra": "Empate"}, 
           "papel": {"tijera":"Derrota", "piedra":"Victoria", "papel": "Empate"},
           "tijera":{"piedra":"Derrota", "papel":"Victoria", "tijera": "Empate"}
          }

print('Bienvenido al juego de piedra papel o tijera')
print('Empecemos!!')

round = 0;
machine_wins = 0;
user_wins = 0;
max_wins = 2;

while machine_wins | user_wins < 2:
  #juego de piedra, papel o tijera
  user_option = input("Seleccione piedra papel o tijera: ")
  # cambiando opcion de usuario a minuscula para evitar typos
  user_option.lower()

  if user_option not in machines_options:
    print('debe seleccionar una opcion correcta')
    continue
  
  machine_option = random.choice(machines_options)
  result = rules[user_option][machine_option]
  
  if result == 'Derrota':
    machine_wins += 1
    round += 1
  elif result == 'Victoria':
    user_wins +=1
    round += 1

  print(f"El resultado es: {result}")
  print(f"victorias de la computadora: {machine_wins}")
  print(f"Tus victurias: {user_wins}")
