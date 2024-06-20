from ghidra.program.model.block import BasicBlockModel
from ghidra.util.task import ConsoleTaskMonitor

funcName = 'main'
blockModel = BasicBlockModel(currentProgram())
monitor = ConsoleTaskMonitor()
func = getGlobalFunctions(funcName)[0]

print(f"Basic block details for function '{funcName}':")
blocks = blockModel.getCodeBlocksContaining(func.getBody(), monitor)

# print first block
print(f"\t[*] {func.getEntryPoint()} ")

# print any remaining blocks
while(blocks.hasNext()):
    bb = blocks.next()
    dest = bb.getDestinations(monitor)
    while(dest.hasNext()):
        dbb = dest.next()
        # For some odd reason `getCodeBlocksContaining()` and `.next()`
        # return the root basic block after CALL instructions (x86). To filter
        # these out, we use `getFunctionAt()` which returns `None` if the address
        # is not the entry point of a function. See:
        # https://github.com/NationalSecurityAgency/ghidra/issues/855
        if not getFunctionAt(dbb.getDestinationAddress()):
            print(f"\t[*] {dbb} ")
