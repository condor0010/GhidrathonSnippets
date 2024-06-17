fm = currentProgram().getFunctionManager()
funcs = fm.getFunctions(True)
for func in funcs:
  if func.getName() == "system":
    print(f"\nFound 'system' @ 0x{func.getEntryPoint()}")
    entry_point = func.getEntryPoint()
    references = getReferencesTo(entry_point)
    for xref in references:
      print(xref)
