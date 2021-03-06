"""
TO IMPLEMENT:
-which command?
-sequential persistence
-undos
"""

from flask import Flask, send_file, request
from classes import speechTokenModule, validCommandModule

app = Flask(__name__)

@app.route('/getResponse', methods=["POST"])
def getResponse():
    
  print("\nEndpoint hit.")

  ### INITIALIZATION ###
  print("Initializing...")
  # Get text input
  rf = request.form
  rawInput = rf.get("rawInput")
  if not rawInput: raise ValueError('Missing rawInput.')
  print("\nrawInput: ", rawInput)

  responseJson = {
    "validCommands": [],
    "responseCommands": []
  }

  ### NLP ###
  def getValidCommands(speechString):
  	fewShotPrompt = """
Speech: Give me a blue cube.
CODE: 
{
"createObj": {
	"objType": "cube",
	"attributes": {
		"color": "blue"
	}
}
}

###

Speech: Create a red capsule.
CODE: 
{
"createObj": {
	"objType": "capsule",
	"attributes": {
		"color": "red"
	}
}
}

###

Speech: Make sphere21 blue.
CODE: 
{
"setColor": {
	"objToUpdate": "sphere21",
	"newColor": "blue"
}
}

###

Speech: Delete cylinder53.
CODE: 
{
"deleteObj": {
	"objToDelete": "cylinder53"
}
}

###

Speech: Create a scoreboard variable with value 1.
CODE: 
{
"createVar": {
	"varName": "scoreboard",
	"varValue": 1
}
}

###

Speech: Set counter variable to 10.
CODE: 
{
"updateVar": {
	"varToUpdate": "counter",
	"newValue": 10
}
}

###

Speech: Reset lives variable to 0.
CODE: 
{
"updateVar": {
	"varToUpdate": "lives",
	"newValue": 0
}
}

###

Speech: Delete the points variable.
CODE:
{
"deleteVar": {
	"varToDelete": "points",
}
}

###

Speech: Change scoreboard variable to twelve.
CODE:
{
"updateVar": {
	"varToUpdate": "scoreboard",
	"newValue": 12
}
}

###

Speech: When you touch collectible18 then remove the collectible and increase the scoreboard variable by one.
CODE: 
{
"createCommand": {
	"targetObj": "player",
	"newCommand": "if(isTouching(collectible18)){changeVariable(scoreboard, 1);}"
}
}
|||
{
"createCommand": {
	"targetObj": "collectible18",
	"newCommand": "if(isTouching(player)){setActive(false)}"
}
}

###

Speech: If I touch cube7 then it turns red.
CODE:
{
"createCommand": {
	"targetObj": "cube7",
	"newCommand": "if(isTouching(player)){changeVariable(scoreboard, 1);}"
}
}

###

Speech: If you run into sphere11 then decrease the lives variable by one.
CODE:
{
"createCommand": {
	"targetObj": "player",
	"newCommand": "if(isTouching(sphere11)){changeVariable(lives, -1);}"
}
}

###

Speech: When cylinder13 runs into sphere20 cylinder 13 turns blue and sphere20 turns red.
CODE:
{
"createCommand": {
	"targetObj": "cylinder13",
	"newCommand": "if(isTouching(sphere20)){changeColor(blue);}"
}
}
|||
{
"createCommand": {
	"targetObj": "sphere20",
	"newCommand": "if(isTouching(cylinder13)){changeColor(red);}"
}
}

###

Speech: After three seconds, change the color of plane1 to orange and the color of plane2 to green.
CODE:
{
"createCommand": {
	"targetObj": "plane1",
	"newCommand": "wait(3);changeColor(orange);"
}
}
|||
{
"createCommand": {
	"targetObj": "plane2",
	"newCommand": "wait(3);changeColor(green);"
}
}

Speech: """ + speechString + """
CODE:"""
  	completion = completions.getCompletion(fewShotPrompt)
  	return completion
    # return validCommands
      
  speechString = speechTokenModule.speechTokenClass(rawInput).castToString()
  validCommandsString = getValidCommands(speechString)
  print("validCommandsString: ", validCommandsString)
  validCommandsList = validCommandsString.split("|||")
  for validCommandString in validCommandsList:
    print("validCommandString: ", validCommandString)
    # validCommandJson = json.loads(validCommandString)
    # print("validCommandJson: ", validCommandJson)
    validCommand = validCommandModule.validCommandClass(validCommandString)
    if validCommand.verify() == True:
      responseJson["validCommands"].append(eval(validCommandString))
    responseCommand = validCommand.getResponse()
    responseJson["responseCommands"].append(responseCommand)

  print("responseJson: ", responseJson)
  print("Done.")
  return responseJson

### SERVER  ###    
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    print("Enter OurXR ????")
    app.run(host='0.0.0.0', threaded=True)