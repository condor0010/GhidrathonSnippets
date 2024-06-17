# Method 1:
func = getFirstFunction()
while func is not None:
    print(f"Function: {func.getName()} @ 0x{func.getEntryPoint()}")
    func = getFunctionAfter(func)

# Method 2:
fm = currentProgram().getFunctionManager()
funcs = fm.getFunctions(True) # True means 'forward'
for func in funcs: 
    print(f"Function: {func.getName()} @ 0x{func.getEntryPoint()}")
