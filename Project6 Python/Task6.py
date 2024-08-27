# TASK 6
# I've successfully calculated my first metric and added it to the dataset as a new column. However, the values are scattered, making it difficult to compare consoles. To make comparisons easier, I need to sort the data.The code to create the lifespan column from the previous task is provided in the precode, along with the code to print the result. I add a line of code to sort `console_data` by the new lifespan column, ordering it from longest to shortest. I save the sorted data in a variable called `sorted_lifespan_data`. The `key()` function, which has been provided, is included in the sorting function like this: `key=key`.

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
    lifespan = row[3] - row[2]
    row.append(lifespan)
    
#Define the key function
def key(row):
    #Sort by life_span, which is at index 6
    return row[-1]
#Sort the console_data by life_span in descending order
sorted_lifespan_data = sorted(console_data, key=key, reverse=True)

# this code will print your result table
for row in sorted_lifespan_data:
    for elem in row:
        print(f'{elem:<20}', end='')
    print()