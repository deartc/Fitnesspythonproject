dict1 = {'bolero' : 100,  'hustle' : 110, 'tango' : 80,
         'waltz' : 90, 'samba' : 100, 'merengue' : 60}
dict2 = {'quickstep' : 200, 'rhumba' : 130, 'salsa' : 200, 'samba' : 100, 'east coast swing' : 140, 'jive' : 160,'bolero' : 100,  'hustle' : 110}
result = {}

print ("Slower bpm dances", dict1)
print ("Faster bpm dances", dict2)

# intersect dictionaries
# Create a new dictionary which is the intersection of two dictionaries.  
# Both key & value must match

# dance bpm intersection
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        result[key] = dict1[key]

print ("Dances that are above 100 bpm results", result)