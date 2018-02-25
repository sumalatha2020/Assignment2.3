# Python program to reverse the user provided input
#Accept a word from user and save it in word variable

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
#Print the word in reverse format
print("\n")