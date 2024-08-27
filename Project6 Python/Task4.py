# TASK 4
# Here, I am asked to retrieve specific data from the table. The last column contains the number of consoles sold over their lifetimes. I calculate the total units sold by using a for loop to sum all the values in this column and store the result in a variable called `total_sold`. Finally, I print `total_sold` to the screen.

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

#Initialize total_sold to 0
total_sold= 0
#Loop over each row in console_data
for row in console_data:
    #Add the number of units sold to total_sold using the correct index(5th element in the row)
    total_sold += row[5]
    
#print(f'Total units sold across all consoles:{total_sold:,}')
print(total_sold)  