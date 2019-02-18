#--------------------------------------------------
# Libraries 
#--------------------------------------------------

import subprocess
from subprocess import PIPE
import maya.cmds as cmds
import os,sys

#--------------------------------------------------
# Set environment paths for the mayapy environment
#--------------------------------------------------

os.environ["PYTHONHOME"] = "/usr/bin/python2.7/"
os.environ["PYTHONPATH"] = "/usr/lib64/python2.7/"

pathToProject = cmds.workspace( q=True, rd=True )
pathToStyle = pathToProject + str("")
pathToScript = pathToProject + "StyleTransfer/runStyleTransfer.sh"
sceneTextures = []
#--------------------------------------------------
# Utility #
#--------------------------------------------------

#Add/Remove conversion Tags     
def addTag():
    
    selectedObjects = []
    selectedObjects.append(cmds.ls(selection = True))
    
    for i in range(0,len(selectedObjects[0])):
        if selectedObjects[0][i].endswith('CNV'):
            print 'The "CNV" tag is already applied!'
        else:
            cmds.rename(selectedObjects[0][i]+'_CNV')
            print 'The tag has been applied!'
            sceneTextures.append(cmds.ls(textures=True))
            collectedTextures = []

def deleteTag():    
    selectedObjects = []
    wrongName = []    
    selectedObjects.append(cmds.ls(selection = True))
    for i in range(0,len(selectedObjects[0])):
        if selectedObjects[0][i].endswith('CNV'):
            objectName = str(selectedObjects[0][i]).split('_CNV')[0] #get the name
            cmds.rename(objectName)
        else:
            print 'No tag applied to selection!' 

#--------------------------------------------------
# Run Shell Script #
#--------------------------------------------------
def convertTextures(selectedStyle):
    
    # Query style # 
    StyleSelection=" "    
    if selectedStyle == "LaMuse":
        StyleSelection="la_muse.ckpt"
    elif selectedStyle == "RainPrincess":
        StyleSelection="rain_princess.ckpt"
    elif selectedStyle == "ShipWreck":
        StyleSelection="shipwreck.ckpt"
    elif selectedStyle == "TheScream":
        StyleSelection="the_scream.ckpt"
    elif selectedStyle == "Udnie":
        StyleSelection="udnie.ckpt"
    else:
        StyleSelection="wave.ckpt"
        
    # Collecting scene data #
    currentStyle = ""
    selectedStyle = []
    texturePaths = []
    textureArgs = ""
    sceneTextures = []
    
    sceneTextures.append(cmds.ls(textures=True))
    collectedTextures = []
    
    for i in range(0,len(sceneTextures[0])):
        if "CNV" in sceneTextures[0][i]:
            collectedTextures.append(sceneTextures[0][i])
    
    print "The following textures have been collected:\n"
    texturePaths = []
    for i in range(0,len(collectedTextures)):
        texturePaths.append(cmds.getAttr(collectedTextures[i]+'.fileTextureName'))
        print "["+str(i)+"]:"
        print "Texture Name:" + collectedTextures[i]
        print "Texture Path:" + texturePaths[i]
        print "-------------------------------------------------------------------"    
        textureArgs+= " " + texturePaths[i]            
        
    print "The style which will be used for the conversion is: " + StyleSelection        

    # Start conversion #    
    print "The texture conversion starts now. A confirmation message will show when the conversion has been done!"
    print "Check the commandLine for further information"
    p = subprocess.Popen(["sh", pathToScript, pathToProject, str(StyleSelection) ,str(textureArgs[1:])], stdout = subprocess.PIPE)
    p.communicate()
    
    print "Your conversion is done. Importing the new textures"
    for i in range(0, len(collectedTextures)):
        toSplit = cmds.getAttr(collectedTextures[i]+".fileTextureName")
        splitArray = toSplit.split("/")
        texName = str(pathToProject) + "convertedTX/Converted_" + splitArray[len(splitArray)-1]    
        print texName
        cmds.setAttr(str(collectedTextures[i])+".fileTextureName", texName , type="string")  
    
    print "You have successfully processed and linked the textures!"

#--------------------------------------------------
# UI #
#--------------------------------------------------
selectedStyle = []   

def createUI():

    windowID = 'Texture Stylizer'        
    styleList = ['LaMuse','RainPrincess','ShipWreck','TheScream','Udnie','Wave']
   
    # Style Change Command #
    
    def updateSelectedItem( item ):
        del selectedStyle[:]
        selectedStyle.append(item)
        print 'The style "' + selectedStyle[0] + '" was selected.' 
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    
    # UI layout #
        
    cmds.window( windowID, title='TextureStylize', sizeable=True, resizeToFitChildren=True)
    
    column = cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1,300), (2,100), (3,20)])
    
    cmds.text( label='---------------------------------------------------------------------------')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.text( label='Assign the "CNV" tag to the textures you would like to convert!')   
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.text( label='---------------------------------------------------------------------------')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )

    cmds.text( label='Assigns the "CNV" tag to the texture(s):' )
    cmds.button( label='Assign Tag', c = 'addTag()')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )

    cmds.text( label='Deletes the "CNV" tag from the texture(s):' )
    cmds.button( label='Delete Tag', c = 'deleteTag()' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.text( label='---------------------------------------------------------------------------')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.text( label='Select the style that you would like to use')   
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.text( label='---------------------------------------------------------------------------')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.text( label='Select the style you would like to apply:' )
    cmds.optionMenu( changeCommand=updateSelectedItem )
    for i in range (0, len(styleList)):
        cmds.menuItem( label=styleList[i] )

    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )

    
    cmds.text( label='---------------------------------------------------------------------------')
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.text( label='Convert the textures!')   
    cmds.button( label='Convert', c = 'convertTextures(selectedStyle[0])')
    cmds.separator( h=10, style='none' )
    cmds.text( label='---------------------------------------------------------------------------')


    # Close program #    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )

selectedStyle = ['LaMuse']   
createUI()
cmds.showWindow()

#Main Loop    
def main():   
    createUI()

if __name__ == "__main__":
    main()