from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# # Disassembly shows:  0001a9f4 6a d4 ff eb     bl         FUN_0000fba4
# # Decompiler shows:   FUN_0000fba4("GET DRONE DATA",&DAT_000d2a04,FUN_00013958,0,0x11,0);
TARGET_ADDR = toAddr(0x0001a9f4)

options = DecompileOptions()
monitor = ConsoleTaskMonitor()
ifc = DecompInterface()
ifc.setOptions(options)
ifc.openProgram(currentProgram())

func = getFunctionContaining(TARGET_ADDR)
res = ifc.decompileFunction(func, 60, monitor)
high_func = res.getHighFunction()
pcodeops = high_func.getPcodeOps(TARGET_ADDR)
op = pcodeops.next()
print([str(i) for i in op.getInputs()]) # TODO make this nicer
