# structural pattern matching: https://stackoverflow.com/questions/67525579/how-use-pattern-matching-for-sql-style-queries-against-json-or-json-lines

import sys
sys.path.append("/home/runner/OurXR-Server")
import json
import jsonschema
import re
from functions import completions

matches = {
"createObj": """{
"createObj": {
  "objType": "(?:cube|sphere|plane|capsule|cylinder)",
  "attributes": {
    "size": "(?:small|medium|large)",
    "color": "(?:red|orange|yellow|green|blue|purple)"
  }
}
}""",  
"setColor": """{
"setColor": {
  "objToUpdate": "[a-zA-Z0-9]+",
  "newColor": "(?:red|orange|yellow|green|blue|purple)"
}
}""",  
"deleteObj":"""{
"deleteObj": {
  "objToDelete": "[a-zA-Z0-9]+"
}
}""",  
"createVar": """{
"createVar": {
  "varName": "[a-z]+",
  "varValue": [0-9]+
}
}""",
"updateVar": """{
"updateVar": {
  "varName": "[a-z]+",
  "varValue": [0-9]+
}
}""",
"deleteVar": """{
"deleteVar": {
  "varName": "[a-z]+",
}
}""",
"createCommand": """{
"createCommand": {
  "targetObject": "[a-zA-Z0-9]+",
  "newCommand": "[a-z]+"
}
}""",
"deleteAllCommands": """{
"deleteAllCommands": {
  "targetObject": "[a-zA-Z0-9]+"
}
}"""
}

for item in publications['items']:
    match item:
        case {'kind': 'magazine', 'title': title, 'issues': issues}:
            print(f'{title} has {issues} issues on hand')

# class validCommand():
#   def __init__(self, value):
#     self.rawValue = value
#     try:
#       self.json = json.loads(value)
#       self.error = None
#     except ValueError:
#       self.error = "***ERROR(Invalid json)"
      
#     self.commandType = self.getCommandType()
#     self.valid = self.verify()
#     self.response = self.getResponse()

#   def verify(self):
#     if self.error == None:
#       # print(matches[self.commandType])
#       return True if re.match(matches[self.commandType], self.rawValue) else False
#     else: return self.error
    
#   def getCommandType(self):
#     if self.error == None:
#       return list(self.json.keys())[0]
#     else: return self.error
    
#   def getResponse(self):
#     if self.error == None:
#       response = ""
#       return response
#     else: return self.error

# test = validCommand("""{
# "setColor": {
#   "objToUpdate": "no",
#   "newColor": "est"
# }
# }""")

# print(test.valid)