def countWords():
	stringInput=input('Enter a sentence here: ')
	stringInput = stringInput.split()

	frequencyWords={}

	for i in stringInput:
		if i not in frequencyWords.keys():
			frequencyWords[i]=0

		frequencyWords[i]=frequencyWords[i]+1

	return frequencyWords