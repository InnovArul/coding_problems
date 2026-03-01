# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii

class Solution:
    def minimumPairRemoval(self, l: List[int]) -> int:
        n = len(l)
        l.append(inf)  # Sentinel value to simplify edge handling
        le, ri = list(range(-1, n)), list(range(1, n + 1))  # Doubly linked list simulation
        h = [(a + b, i) for i, (a, b) in enumerate(pairwise(l))]  # Min-heap of (sum, index)
        heapify(h)

        ans = 0  # Operation count
        rest = n - sum(1 for a, b in pairwise(l) if a <= b)  # Count of violating pairs

        while rest > 0:
            v, i = heappop(h)
            r = ri[i]
            # Skip if this pair is outdated
            if le[r] != i or l[i] + l[r] != v:
                continue

            rr = ri[r]
            # Temporarily add back previously satisfied relationships
            rest += (l[le[i]] <= l[i]) + (l[i] <= l[r]) + (l[r] <= l[rr])
            
            # Merge the pair
            le[rr], ri[i] = i, rr
            l[i] = v
            
            # Subtract satisfied relationships with new value
            rest -= 1 + (l[le[i]] <= l[i]) + (l[i] <= l[rr])

            # Push updated adjacent pairs into heap
            if i:
                heappush(h, (l[le[i]] + l[i], le[i]))
            if rr < n:
                heappush(h, (l[i] + l[rr], i))

            ans += 1
        
        return ans