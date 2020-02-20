"""Connects user selected camera using a Dot node anywhere from the script.
"""
### connect camera v1.0
### For bugs and reports satheesrev@gmail.com
### Thanks to Wouter Gilsing for helping out to make this happen

import nuke

def _cameraPanel(cameras):
	"""Creates a nuke panel and provide selected Camera.

	Arguments:
		cameras (str) : string of camera name seprated by space.
	Returns:
		Camera name of selected else None if user cancels.
	"""
    panel = nuke.Panel("connectCamera", 100)
    panel.addEnumerationPulldown('selectCamera', cameras)
    panel.addButton("cancel")
    panel.addButton("connect")
    if panel.show() != 0:
    	return panel.value("selectCamera")

def connectCamera():
	"""Connects the camera .
	"""
    # Getting all available cameras in the nukescript.
    cameras = ' '.join([n.name() for n in nuke.allNodes('Camera2')])
    if not cameras:
    	msg = '<center>No Camera Found\nimport some camera to connect.'
		nuke.message(msg)
		return

    selCamera = _cameraPanel(cameras)

    if not selCamera:
    	return
    # Creating a Dot node and connect with selected camera
    dot = nuke.createNode("Dot", inpanel=False)
    dot.setInput(0, nuke.toNode(selCamera))
    dot['label'].setValue(' \n'+selCamera)
    dot['note_font_size'].setValue(20)
    dot['note_font'].setValue('Bitstream Vera Sans Bold')
    dot['hide_input'].setValue(True)
