from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
from ghidra.program.flatapi import FlatProgramAPI

fpapi = FlatProgramAPI(getState().getCurrentProgram())
fdapi = FlatDecompilerAPI(fpapi)

for x in dir(fdapi): print(x)

main_decomp = fdapi.decompile(fpapi.getFunction('main'))
print(main_decomp)

