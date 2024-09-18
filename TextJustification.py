'''
Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        nwords = len(words)

        #add words to rows
        temprow = []
        rowlen = 0
        textlist = [] 

        #put words in proper rows
        for i in words:
            testlen = rowlen + len(i)
            # if test row length is lt or equal to the maxWidth
            if testlen <= maxWidth :
                temprow.append(i)
                rowlen = rowlen + len(i) + 1
            # if test row is greater, save and start new row
            else:
                textlist.append(temprow)
                temprow = []
                rowlen = 0
                temprow.append(i)
                rowlen = rowlen + len(i) + 1
        textlist.append(temprow)

        justlist = []
        #justify

        #for all rows except last
        for r in textlist[:-1]:

            s = ""
            numw = len(r)

            if numw == 1:
                s = str(r[0])
                s = s + " "*(maxWidth-len(s))
                justlist.append(s[0:maxWidth])
            else:
                sumr = sum(len(w) for w in r)
                numpad = maxWidth-sumr
                padding = [" "*(numpad//(numw-1))] * (numw-1)
                padrem = numpad-((numpad//(numw-1))*(numw-1))

                i = 0
                while padrem > 0:
                    padding[i] = padding[i] + " "
                    i += 1
                    padrem -= 1

                j = 0
                for w in r[:-1]:
                    s = s + w + padding[j]
                    j += 1
                s = s + r[-1]
                justlist.append(s)



        #justify last row
        s = ""
        for w in textlist[-1]:
            s = s + str(w) + " "
        s = s + " "*(maxWidth-len(s))
        justlist.append(s[0:maxWidth])

        return justlist
