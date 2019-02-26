""" lockNde v1.4
	created 10th may 2012
	for bugs and reports: satheesrev@gmail.com
	To lock & unlock nuke knobs inside the nuke current session.

propertiesmenu = nuke.menu('Properties')
propertiesmenu.addSeparator()

propertiesmenu.addCommand('lock_knobs', "lockNode.lock_knobs()")
propertiesmenu.addCommand('unlock_knobs', "lockNode.unLock_knobs()")

def oc():
  nodes = nuke.allNodes()
  for selNode in nodes:
    selNode.setSelected(True)
    allknobs=selNode.allKnobs()
    label = selNode['label'].getValue()
    labCheck = label.rsplit(None, 1)[-1]
    if labCheck == 'Node_Locked':
      for knob in allknobs:
          knob.setEnabled(False)
nuke.addOnScriptLoad(oc)
"""

import nuke

def lock_knobs():
    selNode = nuke.selectedNode()
    allknobs=selNode.allKnobs()
    for knob in allknobs:
          knob.setEnabled(False)
    labelVal = selNode['label'].getValue()
    labCheck = labelVal.rsplit(None, 1)
    if labCheck:
      labCheck = labCheck[-1]
    if labCheck == 'Node_Locked':
        return
    else:   
        selNode['label'].setValue(labelVal+'\nNode_Locked')



def unLock_knobs():
    selNode = nuke.selectedNode()
    allknobs=selNode.allKnobs()
    for knob in allknobs:
          knob.setEnabled(True)

    labelVal = selNode['label'].getValue()
    labCheck = labelVal.rsplit(None, 1)
    if labCheck:
      labCheck = labCheck[-1]
    if labCheck == 'Node_Locked':
        updated = [each.replace(each, "%s\n" % each) for each in labelVal.split("\n")[:-1]]
        selNode['label'].setValue(" ".join(updated))
    else:
      return
    