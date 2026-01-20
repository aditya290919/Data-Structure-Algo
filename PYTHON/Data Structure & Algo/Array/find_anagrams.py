# Brute force
def find_anagrams(s, p):
	result = []
	p_len = len(p)
	sorted_p = sorted(p)

	for i in range(len(s)-k+1):
		if s[i:i+k] == sorted_p:
			result.append(i)

	return result

