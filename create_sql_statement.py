import csv

openfile = open('Species_0_To_be_added.csv', 'r')
csvfile = csv.reader(openfile)

#with open('Species_0_To_be_added.csv') as csvfile:
#    csvReader = csv.reader(csvfile, delimiter=';')
header = next(csvfile)
headers = map((lambda x: '[' + x + ']'), header)
#for row in csvReader:
    #    print(row)
insert = 'INSERT INTO [SPECIES_TEST].[dbo].[TblSpecies] (' + ", ".join(headers) + ") VALUES "
#insert = "INSERT INTO [SPECIES_TEST].[dbo].[TblSpecies]([fTaxonomyID],[fLSID],[fWoRMID],[fSpeciesName]," \
#     "[fCommonName],[fFeatures]," \
#     "[fColour],[fSize],[fDistribution],[fSimilar],[fReferences],[fNotes],[fFAFFCode],[fHabitat]," \
#     "[fFishBoard],[fBoxColor],[fGenus]," \
#     "[fPhylum],[fClass],[fOrder],[fFamily],[fSpecies]) VALUES "
for row in csvfile:
    values = map((lambda x: ''+x+''), row)
    print(insert +"("+ ", ".join(values) +") GO;" )