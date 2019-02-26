'''
Created on 07-august-2013
@author: satheesh-R
mail - satheesrev@gmail.com
'''


import nuke, math, os

def paintOpacityUp():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            getValue = a['toolbar_opacity'].value()
            newValue = sorted([0, getValue + 0.05, 1])[1]
            setVal = a['toolbar_opacity'].setValue(newValue)
    else:
        return

def paintOpacityUpIncrease():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            getValue = a['toolbar_opacity'].value()
            newValue = sorted([0, getValue + 0.01, 1])[1]
            setVal = a['toolbar_opacity'].setValue(newValue)
    else:
        return


def paintOpacityDown():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            getValue = a['toolbar_opacity'].value()
            newValue = getValue - 0.05
            if newValue < 0: newValue = 0
            setVal = a['toolbar_opacity'].setValue(newValue)
    else:
        return

def paintOpacityDecrease():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            getValue = a['toolbar_opacity'].value()
            newValue = getValue - 0.01
            if newValue < 0: newValue = 0
            setVal = a['toolbar_opacity'].setValue(newValue)
    else:
        return

def paintOpacityDefault():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            a['toolbar_opacity'].setValue(1)

    else:
        return

def paintOpacityZero():
    selNode = None
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    cls = selNode.Class()

    if cls  == 'RotoPaint':
        for a in nuke.selectedNodes():
            a['toolbar_opacity'].setValue(0)

    else:
        return