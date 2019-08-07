from  Day2.Game import Character, Barbarian

player = Character(20)
enemy = Character()


# enemy.attack(player)

for i in range(1):
    enemy.attack(player)


print(f'After attack player has armor {player.armor} and health {player.health}')

barbarian = Barbarian()

barbarian.attack(player)