# IMPORTS
import json
import logging
# logging.dsiable('DEBUG')
import openai
openai.api_key = OPENAI_API_KEY

# DATA HANDLERS

# read file
def readFile(filename: str):
	with open(filename) as f:
		return json.load(f)

# write file
def writeFile(filename: str, content: str, dict):
	with open(filename, "w") as f:
		return json.dump(content, f)


# MAIN PROGRAM

def main(speech: dict) -> dict:

	exceptions = []

	assetsJson = readFile("assets.json")
	psuedoCode = readFile("psuedoCode.json")
	logging.debug("BEFORE: assetsJson: ", assetsJson)
	logging.debug("BEFORE:psuedoCode: ", psuedoCode)

	validCommand = getValidCommand(speech["speechString"])
	logging.debug("validCommand: ", validCommand)

	actionType = validCommand.keys()[0]

	logging.debug(f"actionType == {actionType[0]}")
	if actionType[0] == "createCommand":
		# update psuedoCode.json
		codeSnippet = validCommand.keys(0)["newCommand"]
		targetObject = validCommand.keys(0)["targetObject"]
		psuedoCode[targetObject] = psuedoCode[targetObject] + codeSnippet

	elif actionType[0] == "deleteAllCommands":
		targetObject = validCommand.keys(0)["targetObject"]
		psuedoCode[targetObject] = ""

	elif actionType[0] == "createVar":
		varName = validCommand.keys(0)["varName"]
		varValue = validCommand.keys(0)["varValue"]
		psuedoCode["VARIABLES"][varName] = varValue 

	elif actionType[0] == "updateVar":
		varName = validCommand.keys(0)["varName"]
		varValue = validCommand.keys(0)["varValue"]
		psuedoCode["VARIABLES"][varName] = varValue 

	elif actionType[0] == "deleteVar":
		varName = validCommand.keys(0)["varName"]
		del psuedoCode["VARIABLES"][varName]

	elif actionType[0] == "createObj":
		newObjJson = {
			validCommand.keys()[0][i] : validCommand[validCommand.keys()[0][i]]
			for i in range(len(validCommand.keys(0).keys())
		}
		assetJson.append(newObjJson)

	elif actionType[0] == "setColor":
		for obj in assetJson.keys():
			if obj["objID"] == validCommand.keys()[0]["objToUpdate"]:
				obj["attributes"]["color"] == validCommand.keys()[0]["newColor"]

	elif validCommand.keys()[0] == "deleteObj":
		for obj in assetJson.keys():
			if obj == validCommand.keys()[0]["objToDelete"]:
				del assetJson[obj]

	logging.debug("AFTER: assetsJson: ", assetsJson)
	logging.debug("AFTER:psuedoCode: ", psuedoCode)

	# generate response command
	if exceptions == []:
		responseCommand = getSummary(validCommand)

	responseDict = {
		responseCommand: responseCommand,
		psuedoCode: psuedoCode,
		assetJson: assetJson
	}

	return responseDict