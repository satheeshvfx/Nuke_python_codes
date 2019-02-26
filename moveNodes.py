###############
#Move nodes for nuke.
#This code moves the selected nodes by given direction.
#For bugs and reports: satheesrev@gmail.com


#Menu.py code.
#import moveNodes
#menuBar.addCommand('Edit/Node/move/Up', 'moveNodes.moveNodesUp()', 'shift+Up')
#menuBar.addCommand('Edit/Node/move/Down', 'moveNodes.moveNodesDown()', 'shift+Down')
#menuBar.addCommand('Edit/Node/move/Right', 'moveNodes.moveNodesRight()', 'shift+Right')
#menuBar.addCommand('Edit/Node/move/Left', 'moveNodes.moveNodesLeft()', 'shift+Left')
###############


import nuke
import sys

def moveNodesRight():
    for n in nuke.selectedNodes():
        n.setXpos( int(100 + ( n.xpos())) )

def moveNodesLeft():
   for n in nuke.selectedNodes():
        n.setXpos( int(-100 + ( n.xpos())) )

def moveNodesUp():
    for n in nuke.selectedNodes():
        n.setYpos( int(-100 + ( n.ypos())) )

def moveNodesDown():
    for n in nuke.selectedNodes():
        n.setYpos( int(100 + ( n.ypos())) )
