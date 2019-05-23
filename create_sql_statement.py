import csv

openfile = open('Species_0_To_be_added.csv', 'r')
csvfile = csv.reader(openfile)
header = next(csvfile)
headers = map((lambda x: '[' + x + ']'), header)
insert = 'INSERT INTO [SPECIES_TEST].[dbo].[TblSpecies] (' + ", ".join(headers) + ") VALUES "
for row in csvfile:
    values = map((lambda x: ''+x+''), row)
    print(insert +"("+ ", ".join(values) +") GO;" )