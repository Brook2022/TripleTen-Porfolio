# TASK 7
# Finally I calculate a new metric, total revenue, by estimating it as the product of the release price and the total number of units sold (the last two values in each row). I use a for loop to iterate over the rows of `console_data`, calculate the total revenue, and append the result to the end of each row. The precode already includes the code to sort and print the final result, so I leave that unchanged.

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

for row in console_data:
    total_revenue = row[4]*row[5]
    row.append(total_revenue)

# this code will sort your results
sorted_revenue_data = sorted(console_data, key=lambda row: row[-1], reverse=True)

# this code will print your result table
for row in sorted_revenue_data:
    for elem in row:
        print(f'{elem:<20}', end='')
    print()