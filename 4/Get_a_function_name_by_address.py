# helper function to get a Ghidra Address type
def getAddress(offset):
    return currentProgram().getAddressFactory().getDefaultAddressSpace().getAddress(offset)

# get a FunctionManager reference for the current program
functionManager = currentProgram().getFunctionManager()

# getFunctionAt() only works with function entryPoint addresses!
# returns `None` if address is not the address of the first
# instruction in a defined function. Consider using
# getFunctionContaining() method instead.
addr = getAddress(0x000142e4)
funcName = functionManager.getFunctionAt(addr).getName()
print(funcName)

# check if a specific address resides in a function
addr = getAddress(0x000142e8)
print(functionManager.isInFunction(addr))

# get the function an address belongs to, returns `None` if the address
# is not part of a defined function.
addr = getAddress(0x000142e8)
print(functionManager.getFunctionContaining(addr))
