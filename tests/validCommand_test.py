# better organization? https://www.testcult.com/handle-test-data-the-right-way-in-pytest/

import sys
sys.path.append('/home/runner/OurXR-Server/')
import pytest

from classes import validCommand

# CREATE OBJ

def test_createObj():
  for command in json["createObj"]["valid"]:
  command = validCommand("""...""")
  assert command.commandType == "createObj"
  assert command.verify == true
  assert command.response == ""

def test_createObj_invalidObjType():
  for command in json["createObj"]["invalid"]["invalidObjType"]:
    invalidObjType_command = validCommand(command)
    assert invalidObjType_command.commandType == "createObj"
    assert invalidObjType_command.verify == true
    assert invalidObjType_command.response == ""

def test_createObj_invalidColor_createObj():
  for command in json["createObj"]["invalid"]["invalidObjType"]:
    invalidObjType_command = validCommand(command)
    assert invalidColor_command.commandType == "createObj"
    assert invalidColor_command.verify == true
    assert invalidColor_command.response == ""


# SET COLOR

def test_setColor():
  command = validCommand("""...""")
  assert command.commandType == "setColor"
  assert command.verify == true
  assert command.response == ""

#     self.json = json.loads(value)
#     self.commandType = self.getCommandType()
#     self.response = self.getResponse()