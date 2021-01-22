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

# Global scope
lightList = ['directionalLight', 'pointLight', 'spotLight', 'ambientLight', 'areaLight', 'volumeLight']
lightTable ={'directionalLight' : '1' , 'pointLight': '1' , 'spotLight': '1', 'ambientLight' : '1', 'areaLight' : '1', 'volumeLight' : '1'}
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

def offTog (number):

	print number

	for light in lights: 

		# Get light type circling through lights 
		lightType = cmds.nodeType(light)

		if lightList[number] == lightType: 
			lightName = light.split('Shape')
			lightResult = lightName[0] + lightName[1]
			cmds.setAttr(lightResult + '.visibility', 0)

	lightTable.update({'directionalLight' : '0'})
	

def onTog ():
	
	for light in lights: 

		# Get light type circling through lights 
		lightType = cmds.nodeType(light)

		if lightList[number] == lightType:
			lightName = light.split('Shape')
			lightResult = lightName[0] + lightName[1]
			cmds.setAttr(lightResult + '.visibility', 1)

	lightTable.update({'directionalLight' : '1'})


def ui (): 

	buttonList = []

	lightCount = countLights(); 

	win = 'LightAssistant'
	if (cmds.window (win, exists = 1)):
	    cmds.deleteUI (win)
	    
	cmds.window (win, rtf = 1, w = 280, h = 280, t = win, s = 1)
	cmds.columnLayout (adj = 1)
	cmds.text('Light Assistant', fn = 'boldLabelFont')
	cmds.text('\n')

	cmds.gridLayout( numberOfColumns= 3, cellWidthHeight=(25, 25), cw = 140, aec = 1)

	cmds.text('Light Type', al = 'center', fn = 'boldLabelFont')
	cmds.text('Number in Scene', al = 'center', fn = 'boldLabelFont')
	cmds.text('Visbility for All', al = 'center', fn = 'boldLabelFont')

	i = 0

	for light in lightCount: 
		lightType = cmds.text(lightList[i], al = 'center')
		lightCount = cmds.text(' ' + str(light), al = 'center', fn = 'boldLabelFont')

		#switch = cmds.radioButtonGrp(labelArray2 = ['On', 'Off'], numberOfRadioButtons = 2, cw2 = [60,10], 
			#cal = [2, "right"], ad2 = 1, sl = 1, on2 = lambda x: offTog(buttonList[i-1]), on1 = lambda x: onTog())

		buttonList.append("r{0}".format(i))
		buttonList[i] = createRadioButton(i)

		i += 1

	print buttonList
	cmds.showWindow (win)

def createRadioButton(number): 

	# Create list of radio buttons 
	radioButton = cmds.radioButtonGrp(labelArray2 = ['On', 'Off'], numberOfRadioButtons = 2, cw2 = [60,10], 
		cal = [2, "right"], ad2 = 1, sl = 1, on2 = lambda x: offTog(number), on1 = lambda x: onTog())

	return radioButton;
