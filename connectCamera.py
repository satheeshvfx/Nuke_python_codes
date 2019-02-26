### connect camera v1.0
### connects user selected camera using a Dot node anywhere from the script
### for bugs and reports satheesrev@gmail.com

import nuke

def connectCamera():
	###getting list of camera's available in the script
	cameraNames = ''.join([n.name() for n in nuke.allNodes('Camera2')])
	if cameraNames:
		###Creating nuke panel and storing informations
		panel = nuke.Panel("connectCamera", 100)
		panel.addEnumerationPulldown('selectCamera', cameraNames)
		panel.addButton("cancel")
		panel.addButton("connect")
		result = panel.show()
		selCamera = panel.value("selectCamera")

		### return function when user hit cancel
		if result == 0:
			return
		else:
			### creating DOt node and connect with selected camera
			dot = nuke.createNode("Dot", inpanel=False)
			dot.setInput(0, nuke.toNode(selCamera))
			dot['label'].setValue(' \n'+selCamera)
			dot['note_font_size'].setValue(20)
			dot['note_font'].setValue('Bitstream Vera Sans Bold')
			dot['hide_input'].setValue(True)

	else:
		nuke.message('<center>No Camera Found\nimport some camera to connect')

