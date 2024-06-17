from ghidra.program.flatapi import FlatProgramAPI

state = getState()
program = state.getCurrentProgram()
fpapi = FlatProgramAPI(program)

for x in dir(fpapi): print(x)
print(fpapi.getCurrentProgram())
print(fpapi.getFirstFunction())
