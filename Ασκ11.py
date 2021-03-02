import json

file = open("dict.txt","r")
k = file.read()

diction = json.loads(k)
file.close()

a_dict = {}
def GetKeys(diction):
for keys, value in diction.items():
    if type(value) is dict:
        GetKeys(value)
        if (keys in a_dict):
            a_dict[keys] += 1
            else:
         a_dict[keys] = 1
         elif (keys in a_dict):
        a_dict[keys] += 1
            else:
          a_dict[keys] = 1
          if type(value)is list:
              for i in range(len(value)):
                  if type(value[i]) is dict:
                      GetKeys(value[i])

 GetKeys(diction)     

 KeyVals = max(a_dict.items, key=lamda x: x[1])
 KeyList = list()    
 for key, value in a_dict.items():
     if value == KeyVals[i]:
         KeyList.append(key)
         print("All keys with the max value: ", KeyList)           