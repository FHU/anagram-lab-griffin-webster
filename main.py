#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if len(word1) == len(word2):
        list1 = list(word1)
        list2 = list(word2)
        list1 = list1.sort()
        list2 = list2.sort()
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                continue
            else:
                return False
        return True

    elif len(word1) + len(word2) <= 1:
        return False
    else:
        return False



if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word1 = input("Input a word: ")
    word1 = word1.lower()
    word2 = input("Input a word: ")
    word2 = word2.lower()
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    word1 = word1.isalpha()
    word2 = word2.isalpha()
    answer = anagram(word1, word2)
    print(answer)

anagram(word1, word2)


    