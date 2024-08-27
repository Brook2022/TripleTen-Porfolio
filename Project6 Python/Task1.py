# TASK 1
# I was tasked to work with the dataset stored in the `console_data` variable, which is presented as a nested list. I start by printing this data in a clean, table-like format on the screen. To achieve this, I print each row on a separate line and ensure that each element is spaced consistently. I use a nested for loop and an f-string in the `print()` function to accomplish this. Each element is left-aligned with a fixed string length of 20 characters.

console_data = [['NES', 'Nintendo', 1985, 1995, 179.0, 61910000],
 ['Game Boy', 'Nintendo', 1989, 2003, 89.99, 118690000],
 ['SNES', 'Nintendo', 1990, 2003, 199.0, 49100000],
 ['Virtual Boy', 'Nintendo', 1995, 1996, 179.95, 770000],
 ['Game Boy Advance', 'Nintendo', 2001, 2010, 99.99, 81510000],
 ['Atari 2600', 'Atari', 1977, 1992, 199.0, 30000000],
 ['Sega Genesis', 'Sega', 1988, 1997, 189.0, 30750000],
 ['Game Gear', 'Sega', 1990, 1997, 149.99, 10620000],
 ['Sega CD', 'Sega', 1991, 1996, 299.0, 2240000],
 ['3DO', 'The 3DO Company', 1993, 1996, 699.99, 2000000],
 ['PlayStation', 'Sony Electronics', 1994, 2006, 299.0, 102490000],
 ['PlayStation 2', 'Sony Electronics', 2000, 2013, 299.0, 155000000]]

for row in console_data: #Iterate over each row in the console_data
    for elem in row: #Iterate over each element in the current row
        print(f'{elem:<20}', end='')
        #print each element with a width of 20 chars, left-aligned
    print()#print a new line after each row is printed