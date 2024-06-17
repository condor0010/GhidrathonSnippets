# Note that multiple functions can share the same name, so Ghidra's API
# returns a list of `Function` types. Just keep this in mind.
name = "main"
funcs = getGlobalFunctions(name)
print(f"Found {len(funcs)} function(s) with the name '{name}'")
for func in funcs:
	print(f"{func.getName()} is located at 0x{func.getEntryPoint()}")
