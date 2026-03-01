# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/1932230352#

class Solution:
    def numSteps(self, s: str) -> int:
        s = "0" + s
        # note down 0
        zeros = []
        for i, c in enumerate(s):
            if c == '0':
                zeros.append([i, 0])
        
        steps = 0
        for i, c in reversed(list(enumerate(s))):
            if i == 0: break
            if i == 1 and zeros[-1][1] == 0: break

            if c == '0':
                currzero = zeros.pop()
                if currzero[1] == 1:
                    zeros[-1][1] = 1
                    steps += 2
                else:
                    steps += 1
            else:
                # if the current char is 1, then check if the last zero was set to 1
                # if so, skip it
                if zeros[-1][1] == 1:
                    steps += 1
                else:
                    zeros[-1][1] = 1
                    steps += 2
                
            # print(i, steps, zeros)
        
        return steps

# Time complexity: O(n) where n is the length of the binary string
# Space complexity: O(n) for the list of zeros
