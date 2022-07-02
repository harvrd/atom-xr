# structural pattern matching: https://stackoverflow.com/questions/67525579/how-use-pattern-matching-for-sql-style-queries-against-json-or-json-lines

import sys
sys.path.append("/home/runner/OurXR-Server")
import json
import jsonschema
import re
from functions import completions

# DEFINE JSON SCHEMAS

createObj = {
  "properties": {
    "objType": {"enum": ["cube", "sphere", "plane", "capsule", "cylinder"]},
    "attributes": {
      "properties": {
      "size": {"enum": ["small", "medium", "large"]},
      "color": {"enum": ["red", "orange", "yellow", "green", "blue", "purple"]}
      },
      "required": ["size", "color"]
    }
  },
  "required": ["objType", "attributes"]
}

setColor = {
  "properties": {
    "objToUpdate": {"type": "string"},
    "newColor": {"enum": ["red", "orange", "yellow", "green", "blue", "purple"]}
  },
  "required": ["objToUpdate", "newColor"]
}
 
deleteObj = {
  "properties": {
    "objToDelete": {"type": "string"}
  },
  "required": ["objToDelete"]
}
 
createVar = {
  "properties": {  
    "varName": {"type": "string"},
    "varValue": {"type": "number"}
  },
  "required": ["varName", "varValue"]
}

updateVar = {
  "properties": {
    "varName": {"type": "string"},
    "newValue": {"type": "number"}
  },
  "required": ["varName", "newValue"]
}

deleteVar = {
  "properties": {
    "varName": {"type": "string"},
  },
  "required": ["varName"]
}

createCommand = {
  "properties": {
    "targetObj": {"type": "string"},
    "newCommand": {"type": "string"},
  },
  "required": ["targetObj", "newCommand"]
}

deleteAllCommands = {
  "properties": {
    "targetObj": {"type": "string"}
  },
  "required": ["targetObj"]
}

jsonData = {
  "objType": "cube",
  "attributes": {
    "size": "smasdf",
    "color": "red"
  }
}


# print(jsonschema.validate(instance=jsonData, schema=updateVar))

def validateJson(jsonData, schema):
  try:
    jsonschema.validate(instance=jsonData, schema=schema)
  except jsonschema.exceptions.ValidationError as err:
    return err.absolute_path[-1]
  return True

print(validateJson(jsonData, createObj))

# for item in publications['items']:
#     match item:
#         case {'kind': 'magazine', 'title': title, 'issues': issues}:
#             print(f'{title} has {issues} issues on hand')

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