import sys
sys.path.append("/home/runner/OurXR-Server")
import json
from functions import completions

class speechTokenClass():
  def __init__(self, value):
      self.rawValue = value
      self.tokens = json.loads(value)
      self.speechString = self.castToString()

  def castToString(self):
      if all(self.tokens.values()) == "None":
        return self.tokens.keys().join(" ")
      else:
        speechString = completions.getCompletion("""
Cast the following dictionary to a string:
DICT:
{
	"if": "None",
	"I": "None",
	"touch": "None",
	"this": "box12",
	"blue": "None",                                                 
	"box": "None",
	"then": "None",
	"change": "None",
	"this": "box23",
	"box's": "None",
	"color": "box23",
}
STRING:
If I touch box12 then change the color of box23.

###

Cast the following dictionary to a string:
DICT:
{
	"if": "None",
	"this": "sphere10",
	"sphere": "sphere10",
	"runs": "sphere10",
	"into": "None",
	"that": "cylinder38",
	"cylinder": "cylinder38",
	"then": "None",
	"increase": "None",
	"the": "None",
	"scoreboard": "None",
	"variable": "None",
	"by": "None",
	"one": "None",
}
STRING:
If sphere10 runs into cylinder38 then increase the scoreboard variable by one.

###

Cast the following dictionary to a string:
DICT:
{
	"change": "None",
	"the": "None",
	"color": "None",
	"of": "None",
	"this": "plane25",
	"orange": "plane25",
	"plane": "None",
	"to": "plane25",
	"red": "None",
}
STRING:
Change the color of plane25 to red.

###

Cast the following dictionary to a string:
DICT:
{
	"when": "None",
	"this": "cube42",
	"cube": "None",
	"runs": "None",
	"into": "cube42",
	"that": "None",
	"capsule": "capsule15",
	"then": "None",
	"decrease":"capsule15",
	"the": "None",
	"lives": "None",
	"variable": "None",
	"by": "None",
	"one": "None",
}
STRING:
When cube42 runs into capsule15 then decrease the lives variable by one.

###

Cast the following dictionary to a string:
DICT:
""" + self.rawValue + """
STRING:""")
        return speechString

