### created by satheesh-r, Oct 2014.
### To toggle on & off nuke roto, rotopaint nodes ripple edit function.
### for bugs & reports: satheesrev@gmail.com

import nuke

def rippleEditOnOff():
    selNode = None
    try:
      selNode = nuke.selectedNode()
    except ValueError:  # no node selected 
      pass
    getValue = selNode['toolbar_ripple'].value()
    if getValue == False:
        selNode['toolbar_ripple'].setValue(True)
    if getValue == True:
        selNode['toolbar_ripple'].setValue(False)
    else:
        return