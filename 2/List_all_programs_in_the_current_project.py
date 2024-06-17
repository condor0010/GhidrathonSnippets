state = getState()
project = state.getProject()
locator = project.getProjectData().getProjectLocator()
projectMgr = project.getProjectManager()
activeProject = projectMgr.getActiveProject()
projectData = activeProject.getProjectData()
rootFolder = projectData.getRootFolder()

print(f"type(state):           {type(state)}")
print(f"type(project):         {type(project)}")
print(f"type(projectMgr):      {type(projectMgr)}")
print(f"type(activeProject):   {type(activeProject)}")
print(f"type(projectData):     {type(projectData)}")
print(f"type(rootFolder):      {type(rootFolder)}")

projectName = locator.getName()
fileCount = projectData.getFileCount()
files = rootFolder.getFiles()

print(f"The project '{projectName}' has {fileCount} files in it:")
for file in files:
	print(f"\t{file}")

