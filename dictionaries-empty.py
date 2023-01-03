my_dictionary = {}

my_dictionary['name'] = 'Sam'
my_dictionary['family'] = 'Solomon'
my_dictionary['age'] = '50'
my_dictionary['job'] = 'engineer'
my_dictionary['city'] = 'Hamburg'


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(alien_0['x_position'])

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The alien_0['x_position'] is {alien_0['x_position']}")
