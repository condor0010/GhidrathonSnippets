from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

TARGET_FUNC = "FUN_0000fba4"

# Step 1. Get functions that call the target function ('callers')
target_addr = 0
callers = []
funcs = getGlobalFunctions(TARGET_FUNC)
for func in funcs:
    if func.getName() == TARGET_FUNC:
        print("\nFound {} @ 0x{}".format(TARGET_FUNC, func.getEntryPoint()))
        target_addr = func.getEntryPoint()
        references = getReferencesTo(target_addr)
        for xref in references:
            call_addr = xref.getFromAddress()
            caller = getFunctionContaining(call_addr)
            callers.append(caller)
        break

# deduplicate callers
callers = list(set(callers))

# Step 2. Decompile all callers and find PCODE CALL operations leading to `target_add`
options = DecompileOptions()
monitor = ConsoleTaskMonitor()
ifc = DecompInterface()
ifc.setOptions(options)
ifc.openProgram(currentProgram())

for caller in callers:
    res = ifc.decompileFunction(caller, 60, monitor)
    high_func = res.getHighFunction()
    lsm = high_func.getLocalSymbolMap()
    symbols = lsm.getSymbols()
    if high_func:
        opiter = high_func.getPcodeOps()
        while opiter.hasNext():
            op = opiter.next()
            mnemonic = str(op.getMnemonic())
            if mnemonic == "CALL":
                inputs = op.getInputs()
                addr = inputs[0].getAddress()
                args = inputs[1:] # List of VarnodeAST types
                if addr == target_addr:
                    print(f"Call to {addr} at {op.getSeqnum().getTarget()} has {len(args)} arguments: {[str(arg) for arg in args]}")
                    for arg in args:
                        # Do stuff with each `arg` here...
                        # Not sure what to do? Check out this great article by Lars A. Wallenborn for some ideas:
                        # https://blag.nullteilerfrei.de/2020/02/02/defeating-sodinokibi-revil-string-obfuscation-in-ghidra/
                        # Specifically, search for the function implementation of "traceVarnodeValue"
                        pass
