#include /Users/joro/Documents/Phd/UPF/voxforge/myScripts/praat/splitString.rb
# deprecated due to error on opening word-level files... use instead tab2TextGrid
include splitString.rb
##########################form ##################################
form Specify .phraseAnno.TextGrid and wordExtension



comment specify Path
#word pathTofiles /Users/joro/Documents/Phd/UPF/turkish-makam-lyrics-2-audio-test-data/muhayyerkurdi--sarki--duyek--ruzgar_soyluyor--sekip_ayhan_ozisik/1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde
word pathTofiles /Volumes/IZOTOPE/adaptation_data_soloVoice/kani_karaca-cargah-tevsih/

comment specify filename.wordExtension$  but without extension. File should be in specified path above
#word wordFileName  1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde_zemin_from_38.756510_to_77.630188.wordAligned
word wordFileName kani_karaca-cargah_tevsih

comment specify filename with phraseAnnotation  filename.TextGrid but without extension

# word phraseAnno 1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde.phraseAnno.textGrid
word phraseAnno kani_karaca-cargah_tevsih

comment Enter phonemeAligned for phoneme-level and wordAligned for word-level
word wordExtension .wordAligned

comment Enter tierName
word tierName aligned

endform 

############################################ read form form#############
# NOTE: wordFileName$ is input in form. This is name of Table and  Strings


Read Strings from raw text file... 'pathTofiles$'/'wordFileName$''wordExtension$'

Read Table from whitespace-separated file... 'pathTofiles$'/'wordFileName$''wordExtension$'



# text Grid
Read from file... 'pathTofiles$'/'phraseAnno$'.TextGrid


####################################script ############################

selectObject("Table " + wordFileName$)

#print 'wordFileName$'

selectObject("TextGrid " + phraseAnno$)
lastTierNumber = do("Get number of tiers")
do("Insert interval tier...",1, 'tierName$')
 #lastTier$ = do$("Get tier name...", tiers)



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

selectObject("TextGrid " + phraseAnno$)
do("Insert boundary...", lastTierNumber+1, startTs)


# boundary at 0 and end exist by default in praat
for i from 1 to numInervals

	selectObject("Table " + wordFileName$)	

	endTs=do("Get value...", i,"endTs")
	#endTs=do("Get value...", i,"endTs")
	# word1$=do("Get value...",i,"phonemeOrWord")
	# print 'startTs'

	word1$=Get value... i phonemeOrWord
	#conversion does not work because it is meant only for numeric values. So never store text in a table. you can get only "Get value..." from a table.
	#word1$=string$(word1)
	# print 'word1$'

	# selectObject("Strings " + wordFileName$)
	# word$=Get string... i+1

	# split into ts and word using split script
	# @split ("	", word$)
	

	selectObject("TextGrid " + phraseAnno$)

	# TODO :chekc that endTs <= audioLength
	if endTs == endTsPrev
	print 'endTs'
	endTs = endTs + 0.001
	
endif 
	do("Insert boundary...", lastTierNumber+1, endTs)
	# do("Set interval text...",lastTierNumber+1,i,split.array$[2])
	do("Set interval text...",lastTierNumber+1,i+1,word1$)
	
	endTsPrev = endTs



endfor



# save new TextGrid in the same dir as the result aligned
selectObject("TextGrid " + phraseAnno$)
Save as text file... 'pathTofiles$'/'phraseAnno$'.TextGrid