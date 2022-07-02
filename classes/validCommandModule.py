# todo: implement more specific responses (type error)

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
    "color": {"enum": ["red", "orange", "yellow", "green", "blue", "purple"]}
    # "attributes": {
    #   "properties": {
    #   # "size": {"enum": ["small", "medium", "large"]},
    #   "color": {"enum": ["red", "orange", "yellow", "green", "blue", "purple"]}
    #   },
    #   # "required": ["size", "color"]
    #   "required": ["color"]
    # }
  },
  "required": ["objType", "color"]
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
    "varToUpdate": {"type": "string"},
    "newValue": {"type": "number"}
  },
  "required": ["varToUpdate", "newValue"]
}

deleteVar = {
  "properties": {
    "varToDelete": {"type": "string"},
  },
  "required": ["varToDelete"]
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
    "targetDeleteObj": {"type": "string"}
  },
  "required": ["targetObj"]
}

# RESPONSE DICT

responseDict = {
  "color": "What color would you like to make your object?",
  "objType": "What type of object would you like to make?",
  "objToUpdate": "Which object would you like to change the color of?",
  "newColor": "What color would you like to change your object to?",
  "objToDelete": "Which object would you like to delete?",
  "varName": "What would you like to name your new variable?",
  "varValue": "What value would you like to set your variable to?",
  "varToUpdate": "Which variable would you like to update?",
  "newValue": "What would you like to set the value of your variable to?",
  "varToDelete": "Which variable would you liek to delete?",
  "targetObj": "Which object would you like to be affected by the game logic?",
  "targetDeleteObj": "Which object would you like to delete game logic from?"
}

def validateJson(jsonData, schema):
  try:
    jsonschema.validate(instance=jsonData, schema=schema)
  except jsonschema.exceptions.ValidationError as err:
    # print("ERROR: ", err.absolute_path[-1])
    try:
      return err.absolute_path[-1]
    except:
      return str(err).split("'")[1]
  return True


class validCommandClass():
  def __init__(self, value):
    self.rawValue = value
    try:
      self.json = json.loads(value)
      self.jsonError = None
    except ValueError:
      self.jsonError = "***ERROR(Invalid json)"

    self.propertyError = None
    self.commandType = None
    # self.valid = self.verify()
    self.response = None

  def verify(self):
    if self.jsonError == None:
      # print("sent to validator: ", self.json[self.commandType], eval(self.commandType))
      validatorResponse = validateJson(self.json[self.getCommandType()], eval(self.getCommandType()))
      if validatorResponse == True:
        return True 
      else:
        self.propertyError = validatorResponse
        print(self.propertyError)
        return False
      # return True if re.match(matches[self.commandType], self.rawValue) else False
    else: return self.jsonError
    
  def getCommandType(self):
    if self.jsonError == None:
      return list(self.json.keys())[0]
    else: return self.jsonError
    
  def getResponse(self):
    if self.jsonError == None:
      if self.verify() == True:
        response = "Ok."
      else:
        response = responseDict[self.propertyError]
      return response
    else: return self.jsonError


# test = validCommandClass("""{
# "updateVar": {
#   "varToUpdate": "test"
# }
# }""")

# print(test.verify())
