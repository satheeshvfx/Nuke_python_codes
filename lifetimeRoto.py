'''
Created on 07-april-2016
@author: satheesh-R
mail - satheesrev@gmail.com
'''
### to set selected roto shapes lifetime based on the min max keyframes value.

import nuke

def setRotoLifeTime():

	### get selected node
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    if selNode == None:
        nuke.message('make sure your roto node selected')
        return
    ### find selected roto shapes keyframes
    if selNode.Class() == 'Roto':
        for selShape in selNode['curves'].getSelected():
            keyFrame = selShape[0].center.getControlPointKeyTimes()
            keyFrames = [int(i) for i in keyFrame]
            low = (min(keyFrames))
            high = (max(keyFrames))
            ### applying min max keyframe to per shape lifetime
            selNode['lifetime_type'].setValue(4)
            selNode['lifetime_start'].setValue(low)
            selNode['lifetime_end'].setValue(high)
