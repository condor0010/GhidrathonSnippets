blocks = currentProgram().getMemory().getBlocks()
for block in blocks:
	print(f"Name: {block.getName()}, Size: {block.getSize()}")
