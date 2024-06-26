state = getState()
project = state.getProject()
program = state.getCurrentProgram()
locator = project.getProjectData().getProjectLocator()
print(f"type(state):           {type(state)}")
print(f"type(project):         {type(project)}")
print(f"type(program):         {type(program)}")
print(f"type(locator):         {type(locator)}")
print(f"Project Name:          {locator.getName()}")
print(f"Files in this project: {project.getProjectData().getFileCount()}")
print(f"Is a remote project:   {locator.isTransient()}")
print(f"Project location:      {locator.getLocation()}")
print(f"Project directory:     {locator.getProjectDir()}")
print(f"Lock file:             {locator.getProjectLockFile()}")
print(f"Marker file:           {locator.getMarkerFile()}")
print(f"Project URL:           {locator.getURL()}")
