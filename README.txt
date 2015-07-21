THE final project can use evolutionary algorithms to try and create the best song.

Use the format specified by the asc2mid.c program you found. (I guess ask the author if you can use it)

Have the code store each note and time as an integer. use the bits in said integer and the shifting of them to change the song.

This would be neat because the fitness function should have a very small basin of attraction since a really good song that is changed very slightly will sound terrible.

So The program runs and simply evaluates a set of integers according to rules. Then to check the best-of-run, use your set of integers that represent the song and output it to fit with the asc2mid standards. Then, use the code to convert it to a midi and listen.

!!!
   >> Use fluidsynth -F out.wav /usr/share/sounds/sf2/FluidR3_GM.sf2 filename.mid
   to convert the midi file into something that sounds nice!
!!!

WEBSITE SOURCE OF .c CODE

http://www.archduke.org/midi/index.html


NOTES
One instrument type per CHannel
One note playing per timing on each TRack (i.e can have a chord, but it can't be sustained whist playing another chord, the second chord has to be on a seperate TRack).



CHANNEL INSTRUMENT LIST
CH 10     - Percussion

