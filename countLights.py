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

lightList = ['directionalLight', 'pointLight', 'spotLight', 'ambientLight', 'areaLight', 'volumeLight']
lights = cmds.ls(lights = True)


def countLights (): 

	lightCount = [0] * 6

	
	print "this works"

	# Get all light objects in the scene 
	lights = cmds.ls(lights = True)

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

	return lightCount

def disablePressed ():
	print "pressed" 

	print lights
	for light in lights: 

		lightType = cmds.nodeType(light)

		if lightType == lightList[0]:
			lightName = light.split('Shape')
			lightResult = lightName[0] + lightName[1]
			cmds.setAttr(lightResult + '.visibility', 0)


def ui (): 
	print "this is the ui"

	lightCount = countLights(); 

	win = 'LightAssistant'
	if (cmds.window (win, exists = 1)):
	    cmds.deleteUI (win)
	cmds.window (win, rtf = 1, w = 280, h = 280, t = win, s = 1)
	cmds.columnLayout (adj = 1)
	cmds.text('Light Types', fn = 'boldLabelFont')
	cmds.text('\n')

	cmds.gridLayout( numberOfColumns= 2, cellWidthHeight=(25, 25), cw = 120, aec = 1)

	print lightList
	print lightCount

	i = 0

	for light in lightCount: 
		label = cmds.text(' ' + str(light) + ' ' + lightList[i] + 's', al = 'left', fn = 'boldLabelFont')
		label2 = cmds.button('Disable Lights', c = lambda x: disablePressed())

		i += 1

	cmds.showWindow (win)