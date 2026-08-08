class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)

        righthandsidematchlength = [0]*m
        i, j = m-1, n-1
        rightmatched = 0

        while i >= 0:
            if j >=0 and word1[i] == word2[j]:
                rightmatched += 1
                j -= 1
            righthandsidematchlength[i] = rightmatched
            i -= 1

        seq = []
        i, j = 0, 0
        changepower = True

        while i < m and j < n:
            if word1[i] == word2[j]:
                seq.append(i)
                j += 1

            elif changepower == True and i+1 < m and righthandsidematchlength[i+1] >= n-j-1:
                seq.append(i)
                changepower = False
                j += 1

            i += 1

        if j == n:
            print(seq)
        
        print("[]")
            