#!/usr/bin/python

#----------------------------------------------------------------------
#                           bits2asc.py
#----------------------------------------------------------------------
#   Converts an array of 32 bit integers into an acsii file formated 
#   for conversion to midi file.
#
#   Bit format:
#   XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX
#    TR   CH  Instrumet  Duration    Note
#
#   TR = Track number, 0-15
#   CH = Channel number, 0-15. CH 10 = percussion!
#----------------------------------------------------------------------

import sys  # For command line arguments
import os   # To check if file exist
import midiNote
import writeNote as wn




#----------------------------------------------------------------------
#   Input   : empty
#   Output  : Dictonary with note bindings
#----------------------------------------------------------------------
def noteToStr():
    ns = ("A-----", "A#-----", "B-----", "C-----", "C#-----", "D-----", "D#-----", "E-----", "F-----", "F#-----", "G-----", "G#-----",\
          "A-----", "A#-----", "B-----", "C----", "C#----", "D----", "D#----", "E----", "F----", "F#----", "G----", "G#----",\
          "A----", "A#----", "B----", "C---", "C#---", "D---", "D#---", "E---", "F---", "F#---", "G---", "G#---",\
          "A---", "A#---", "B---", "C--", "C#--", "D--", "D#--", "E--", "F--", "F#--", "G--", "G#--",\
          "A--", "A#--", "B--", "C-", "C#-", "D-", "D#-", "E-", "F-", "F#-", "G-", "G#-",\
          "A-", "A#-", "B-", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#",\
          "A", "A#", "B", "C'", "C#'", "D'", "D#'", "E'", "F'", "F#'", "G'", "G#'",\
          "A'", "A#'", "B'", "C''", "C#''", "D''", "D#''", "E''", "F''", "F#''", "G''", "G#''",\
          "A''", "A#''", "B''", "C'''", "C#'''", "D'''", "D#'''", "E'''", "F'''", "F#'''", "G'''", "G#'''",\
          "A'''", "A#'''", "B'''", "C''''", "C#''''", "D''''", "D#''''", "E''''", "F''''", "F#''''", "G''''", "G#''''",\
          "A''''", "A#''''", "B''''", "C", "C#", "D", "D#", "E")
    noteDict = dict(zip(range(0,128), ns))
    return noteDict
    
    
    
#----------------------------------------------------------------------
#   MAIN
#----------------------------------------------------------------------

# Read directory path from command line
if len(sys.argv) == 2:
    filename = str(sys.argv[1])
else:
    print "[!] Need to enter directory path as command line argument"
    quit()
    
# Open the file and check if it exists
if os.path.isfile(filename):
    f = open(filename, 'r')
else:
    print "[!] "+ filename + " doesn't exist."
    quit()

noteDict = noteToStr()

filename = str(sys.argv[1]+".txt")
g = open(filename,"w")    
g.write("format=1 tracks=15 division=120\n")
g.write("FOL  TR  0   CH 16   Tempo 180\n")
g.write("FOL  TR  0   CH 16   End of track\n")
for line in f:
    note = int(line)
    wn.writeNote(note, noteDict, g)

for j in range(2):
    g.write("FOL  TR  %d   CH %d   End of track\n" % (j+1,j+1))
g.close()

    








