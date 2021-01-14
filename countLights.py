import maya.cmds as cmds 
import maya.mel as mel 
import sys 

# The five types of lights in Maya: 
# directionallight, ambientlight, pointlight, spotlight, arealight
# We want to: 
# Count the number of lights in a scene 
	# Separate by type (count by type)
	# Show if disabled or not, maybe disable by type? 

# Essential a quick lighting control panel

# Count lights in a scene 
# Loop through items in a scene, and if any of those 5, add to the count. 
 	# Sort by type name

def countLights(): 

	lightList[] = ['directionalLight', 'pointLight', 'spotLight', 'ambientLight', 'areaLight', 'volumeLight']
	print "this works"

	objects = cmds.ls()	

	# Get all light objects in the scene 
	lights = cmds.ls(lights = True)

	# For all the objects in the directory, we are going to list the number of each light
	for light in  lights: 
		
		lightType = cmds.nodeType(light)

		if lightType == lightList[0]:
			lightCount[0] += 1

		elif lightType == lightList[1]:
			lightCount[1] += 1

		elif lightType == lightList[2]:
			lightCount[2] += 1

		elif lightType == lightList[3]:
			lightCount[3] += 1

		elif lightType == lightList[4]:
			lightCount[4] += 1

		elif lightType == lightList[5]:
			lightCount[5] += 1

	print lightCount
