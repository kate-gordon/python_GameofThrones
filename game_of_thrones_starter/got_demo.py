from pprint import pprint
from characters import characters
from houses import houses 

# ## Characters with names starting with "A "
# namesA = 0
# for character in characters:
#     if character['name'][0] == 'A':
#         namesA += 1
# print(namesA)

# ## Characters with names starting with "Z" 
# namesZ = 0
# for character in characters: 
#     if character['name'].startswith('Z') == True: 
#         namesZ += 1
# print(namesZ)

# ## Number of characters who died
# index = 0
# for character in characters: 
#     if character['died'] != '': 
#         index +=1
# print(index)

# ## Character with the most titles 
# amtofTitles = 0
# charName = ''
# for character in characters: 
#     if len(character['titles']) > amtofTitles:
#         amtofTitles = len(character['titles'])
#         charName = character['name']
# print(amtofTitles)
# print(charName)

# ## Number of Valyrian characters
# numVal = 0
# for character in characters: 
#     if character['culture'] == 'Valyrian':
#         numVal += 1
# print(numVal)

# ## Name of actor who plays Hot Pie    
# for character in characters: 
#     if character['aliases'] == 'Hot Pie' or character['name'] == 'Hot Pie': 
#         print(character['playedBy'])
    
# ## Number of characters from the books who are in the series
# inSeries = 0
# for character in characters: 
#     if character['tvSeries'][0] != '': 
#         inSeries += 1
# print(inSeries)

# ## List of Targaryens 
# for character in characters: 
#     if 'Targaryen' in character['name']: 
#         print(character['name'])



## Houses & Number of Allegiances to each 

members_by_house = {}
for character in characters:
    for url in character['allegiances']: 
        houseName = houses[url]
        if houseName in members_by_house: 
            members_by_house[houseName] += 1
        else: 
            members_by_house[houseName] = 1 
    
pprint(members_by_house)       
    