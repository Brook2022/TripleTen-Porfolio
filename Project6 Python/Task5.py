# TASK 5
# I observe that more popular consoles tend to have a longer lifespan before being discontinued, so I calculate the lifespan metric and add it as a new column at the end of the dataset.To do this, I loop over each row in `console_data` and calculate the lifespan in years using the released year and discontinued year columns. I then append the result to each row to create the new column.A separate for loop is included in the precode to print the results, but I ensure that the for loop calculating the lifespan comes before this one.

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

# write your code here
for row in console_data:
    life_span = row[3]-row[2]
    row.append(life_span)
# this code will print your result table
for row in console_data:
    for elem in row:
        print(f'{elem:<20}', end='')
    print()