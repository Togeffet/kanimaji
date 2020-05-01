# Python program to remove characters from first string which 
# are present in the second string 
NO_OF_CHARS = 256

# Utility function to convert from string to list 
def toList(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 

# Utility function to convert from list to string 
def toString(List): 
	return ''.join(List) 

# Returns an array of size 256 containing count of characters 
# in the passed char array 
def getCharCountArray(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 

# removeDirtyChars takes two string as arguments: First 
# string (str) is the one from where function removes dirty 
# characters. Second string is the string which contain all 
# dirty characters which need to be removed from first string 
def removeDirtyChars(string, mask_string): 
	count = getCharCountArray(mask_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = toList(string) 

	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1

	# After above step string is ngring. 
	# Removing extra "iittg" after string 
	return toString(str_list[0:res_ind]) 

# Driver function to test the above functions 
mask_string = "濡 嘘 賑 剃 喧 嘩 叩 噛 姪 苺 逢 糊 鋏 鞄 飴 揃 噂 賑 蝶 漕 鳩 囁 咳 吊 屑 掻 撫 汲 溜 遥 焚 詫 釘 錆 騙 雀 甥 炒 嬉"
string =      "漕 汲 嘩 詫 吊 騙 喧 焚 揃 釘 姪 遥 掻 錆 糊 嬉 屑 叩 噛 蝶 甥 噂 囁 雀 剃 鋏 炒 咳 苺 賑 溜 鳩 撫 濡 飴 嘘 逢 鞄"
print removeDirtyChars(string, mask_string) 

# This code is contributed by Bhavya Jain 