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
	
	# For all the objects in the directory, we are going to list the number of each light
	for i in objects: 
