# convert a-tab separated timestap+word file into Praat's TextGrid. 
#  Other praat scripts found here: http://markantoniou.blogspot.com.es/2007/09/praat-christmas.html

#include /Users/joro/Documents/Phd/UPF/voxforge/myScripts/praat/splitString.rb
include splitString.rb
##########################form ##################################
form Specify .phraseAnno.TextGrid and wordExtension



comment specify Path
word pathTofiles /Users/joro/Documents/Phd/UPF/turkish-makam-lyrics-2-audio-test-data-synthesis/muhayyerkurdi--sarki--duyek--ruzgar_soyluyor--sekip_ayhan_ozisik_short/1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde/

comment specify filename.wav  but without extension. File should be in specified path above
word wordFileName 1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde_10_meyan_from_171_044_to_192_962376

comment Enter wordAligned if you want word-level
word wordExtension .wordsDurationSynthAligned


endform 

############################################ read form form#############
# NOTE: wordFileName$ is input in form. This is name of Table and  Strings


Read Strings from raw text file... 'pathTofiles$'/'wordFileName$''wordExtension$'

Read Table from whitespace-separated file... 'pathTofiles$'/'wordFileName$''wordExtension$'

# Read audio from file

Read from file... 'pathTofiles$'/'wordFileName$'.wav
endTime=do("Get end time")

# create text Grid
To TextGrid... 'pathTofiles$'/'wordFileName$'.TextGrid


####################################script ############################

selectObject("Table " + wordFileName$)

#print 'wordFileName$'

selectObject("TextGrid " + wordFileName$)
lastTierNumber = do("Get number of tiers")
# do("Insert interval tier...",lastTierNumber+1, "'wordExtension$'")
do("Insert interval tier...",lastTierNumber+1, "phrases")



selectObject("Table " + wordFileName$)
numInervals = do("Get number of rows")

startTs=do("Get value...", 1,"startTs")

# check that startTs != 0
if startTs == 0.0
	print 'startTs'
	startTs = 0.001
	print 'startTs'
endif
endTsPrev = startTs

selectObject("TextGrid " + wordFileName$)
do("Insert boundary...", lastTierNumber+1, startTs)


# boundary at 0 and end exist by default in praat
for i from 1 to numInervals

	selectObject("Table " + wordFileName$)	

	endTs=do("Get value...", i,"endTs")

	word1$=Get value... i phonemeOrWord

	selectObject("TextGrid " + wordFileName$)

	#  :chekc that endTs <= audioLength
	if endTs > endTime
		endTs = endTime - 0.001
	endif

	if endTs == endTsPrev
		print 'endTs'
		endTs = endTs + 0.001
	
	endif 
	

	

	do("Insert boundary...", lastTierNumber+1, endTs)
	do("Set interval text...",lastTierNumber+1,i+1,word1$)
	
	endTsPrev = endTs



endfor



# save new TextGrid in the same dir as the result aligned. 
# carefully! avoid deleting existing textGrid
selectObject("TextGrid " + wordFileName$)
Save as text file... 'pathTofiles$'/'wordFileName$'.TextGrid