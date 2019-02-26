##-------------------------------------------------
## trackRoto v1.1
## For bugs please email me at satheesrev@gmail.com
## Compatibility: Nuke v5 - v8 plus
##--------------------------------------------------
## menu.py
## import trackRoto
## n = nuke.toolbar('Nuke')
## n.addCommand('Edit/trackRoto', 'trackRoto.trackRoto()', 'O')
##-------------------------------------------------------------


import nuke, os, re

def trackRoto():
		sel = None
		try:
				sel = nuke.selectedNode()
				X = sel.xpos()
				Y = sel.ypos()
		except ValueError:  # no node selected
				pass
		if sel is None:
				rt = nuke.createNode('Roto')
		if sel:
				NodeType = re.sub(r"\d", "", sel.Class())
				print NodeType
				if NodeType == 'Tracker':
						rt = nuke.createNode('Roto')
						rt.setInput(0, None)
						rt.setXYpos(X+200,Y)
						rt['translate'].fromScript(sel['translate'].toScript())
						rt['rotate'].fromScript(sel['rotate'].toScript())
						rt['scale'].fromScript(sel['scale'].toScript())
						rt['center'].fromScript(sel['center'].toScript())
						rt['opacity'].setValue(1)

				else:
						rt = nuke.createNode('Roto')
