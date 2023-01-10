class Solution:
	def longestSubStr(self,s:str)->int:
		n=len(str)
		seenChar={}
		left=0
		right=0
		longest=0

		while(left<0 and right<0):
			current_char=s[right]
			if current_char in seenChar:
				previous_char=seenChar[current_char]
				left=max(left,previous_char+1)

			seenChar[current_char]=right
			longest=max(longest,right-left+1)
			right+=1

		return longest