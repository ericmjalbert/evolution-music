#!/usr/bin/python

#----------------------------------------------------------------------
#                           midiBit.py
#----------------------------------------------------------------------
#   Series of functions for extracting MIDI note info from a 32-bit 
#   integer.
#
#   Bit format:
#   XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX
#    TR   CH   Volume    Duratio    pitch
#
#   TR = Track number, 0-15
#   CH = Channel number, 0-15. CH 10 = percussion!
#
#----------------------------------------------------------------------


#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#   Output: 4-bit integer, just track info for midi note.
#----------------------------------------------------------------------
def getTrack(note):
    val = note & int('f0000000', 16)
    return val >> 28


#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#   Output: 4-bit integer, just channel info for midi note.
#----------------------------------------------------------------------
def getChan(note):
    val = note & int('0f000000', 16)
    return val >> 24
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#   Output: 8-bit integer, just instrument info for midi note.
#----------------------------------------------------------------------
def getInst(note):
    val = note & int('00ff0000', 16)
    return val >> 16
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#   Output: 8-bit integer, just duration info for midi note.
#----------------------------------------------------------------------
def getDur(note):
    val = note & int('0000ff00', 16)
    return val >> 8
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#   Output: 8-bit integer, just pitch info for midi note.
#----------------------------------------------------------------------
def getPitch(note):
    return note & int('00000ff', 16)

#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#           4-bit integer, track number
#   Output: 32-bit integer, midi note info with updated track
#----------------------------------------------------------------------
def setTrack(note,track):
    val = note & int('0fffffff', 16)    # Empty current track
    val = val | (track << 28)         # Set track
    return val


#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#           4-bit integer, channel number
#   Output: 32-bit integer, midi note info with updated channel
#----------------------------------------------------------------------
def setChan(note,channel):
    val = note & int('f0ffffff', 16)    # Empty current track
    val = val | (channel << 24)         # Set track
    return val
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#           4-bit integer, instrument number
#   Output: 32-bit integer, midi note info with updated instrumetn
#----------------------------------------------------------------------
def setInst(note,instrument):
    val = note & int('ff00ffff', 16)    # Empty current track
    val = val | (instrument << 16)      # Set instrument
    return val
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#           4-bit integer, duration value
#   Output: 32-bit integer, midi note info with updated duration
#----------------------------------------------------------------------
def setDur(note,duration):
    val = note & int('ffff00ff', 16)    # Empty current track
    val = val | (duration << 8)         # Set duration
    return val
    
#----------------------------------------------------------------------
#   Input : 32-bit integer, the info for midi note.
#           4-bit integer, pitch value
#   Output: 32-bit integer, midi note info with updated pitch
#----------------------------------------------------------------------
def setPitch(note,pitch):
    val = note & int('ffffff00', 16)    # Empty current track
    val = val | pitch                 # Set pitch
    return val
    
