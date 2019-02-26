import sys
import nuke

'''
Created on 2 Jan 2013

@author: satheesh.R
contact: satheesrev@gmail.com
'''
## creating panel
def  shuffleAlpha():
    sa = nuke.Panel("shuffleAlpha.......  by satheesh-r", 400)
    sa.addEnumerationPulldown('selectChannel to shuffle', 'red green blue alpha rgba')
    sa.addBooleanCheckBox("to All channels", False)
    sa.addButton("cancel")
    sa.addButton("ok")
    result = sa.show()
    channel=sa.value("selectChannel to shuffle")
    value=sa.value("to All channels")
    ## continue the function if user hit ok
    if result == 0 :
        return

    if channel == 'rgba' :
        ex = nuke.createNode('Expression', inpanel = False)
        ex['expr3'].setValue('clamp(r+g+b+a)')
        ex['label'].setValue(channel+ ' ---> alpha')


    ## Create shuffle node and set selected channel to all channels
    elif value == True :
        sh = nuke.createNode("Shuffle", inpanel = False)
        sh['alpha'].setValue(channel)
        sh['red'].setValue(channel)
        sh['green'].setValue(channel)
        sh['blue'].setValue(channel)
        sh['label'].setValue(channel+'-->All')


    ## Create shuffle node and set selected channel to alpha channel only, keep other channels black
    elif value == False :
        sh = nuke.createNode("Shuffle", inpanel = False)
        sh['alpha'].setValue(channel)
        sh['red'].setValue('black')
        sh['green'].setValue('black')
        sh['blue'].setValue('black')
        sh['label'].setValue(channel+'-->alpha')


        ## setting node tile color based on user selection
        if channel == "red" :
            sh['tile_color'].setValue(4278190335)
        if channel == "green" :
            sh['tile_color'].setValue(16711935)
        if channel == "blue" :
            sh['tile_color'].setValue(65535)
        if channel == "alpha" :
            sh['tile_color'].setValue(4278124287)

    else:
        return
