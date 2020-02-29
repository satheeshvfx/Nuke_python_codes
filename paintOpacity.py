'''
Created on 07-august-2013
@author: satheesh-R
mail - satheesrev@gmail.com
'''

import nuke, math, os

def isSelectedNodeType(nodeType):
    try:
        node = nuke.selectedNode()
    except ValueError: # no node selected
        print "No nuke node selected."
        return
    return node.Class() == nodeType

def paintOpacityUp():
    """Bring paint opacity up.
    """
    if not isSelectedNodeType("RotoPaint"):
        return
    for a in nuke.selectedNodes():
        getValue = a['toolbar_opacity'].value()
        newValue = sorted([0, getValue + 0.05, 1])[1]
        setVal = a['toolbar_opacity'].setValue(newValue)


def paintOpacityUpIncrease():
    """Increase in bring up of paint opacity.
    """
    if not isSelectedNodeType("RotoPaint"):
        return

    for a in nuke.selectedNodes():
        getValue = a['toolbar_opacity'].value()
        newValue = sorted([0, getValue + 0.01, 1])[1]
        setVal = a['toolbar_opacity'].setValue(newValue)


def paintOpacityDown():
    """Bring Paint opacity down.
    """
    if not isSelectedNodeType("RotoPaint"):
        return

    for a in nuke.selectedNodes():
        getValue = a['toolbar_opacity'].value()
        newValue = getValue - 0.05
        if newValue < 0: newValue = 0
        setVal = a['toolbar_opacity'].setValue(newValue)


def paintOpacityDecrease():
    """Decrease in bringing down of paint opacity.
    """
    if not isSelectedNodeType("RotoPaint"):
        return

    for a in nuke.selectedNodes():
        getValue = a['toolbar_opacity'].value()
        newValue = getValue - 0.01
        if newValue < 0: newValue = 0
        setVal = a['toolbar_opacity'].setValue(newValue)


def paintOpacityDefault():
    """Set Paint opacity to default.
    """
    if not isSelectedNodeType("RotoPaint"):
        return

    for a in nuke.selectedNodes():
        a['toolbar_opacity'].setValue(1)


def paintOpacityZero():
    """Set paint opacity to zero.
    """
    if not isSelectedNodeType("RotoPaint"):
        return

    for a in nuke.selectedNodes():
        a['toolbar_opacity'].setValue(0)
