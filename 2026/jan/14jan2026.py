# https://leetcode.com/problems/separate-squares-ii/

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Step 1: Build events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # entering
            events.append((y + l, -1, x, x + l)) # leaving
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        # Step 2: Coordinate compression
        x_id = {x: i for i, x in enumerate(xs)}

        # Segment Tree to maintain union length
        n = len(xs) - 1
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)

            if count[node] > 0:
                length[node] = xs[r] - xs[l]
            else:
                length[node] = (
                    length[node * 2] + length[node * 2 + 1]
                    if l + 1 < r else 0
                )

        # Step 3: Sweep line
        prev_y = events[0][0]
        total_area = 0
        slabs = []

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                area = dy * length[1]
                slabs.append((prev_y, y, length[1], area))
                total_area += area

            update(1, 0, n, x_id[x1], x_id[x2], typ)
            prev_y = y

        # Step 4: Find minimal y where area reaches half
        half = total_area / 2
        acc = 0

        for y1, y2, width, area in slabs:
            if acc + area >= half:
                return y1 + (half - acc) / width
            acc += area

        return prev_y