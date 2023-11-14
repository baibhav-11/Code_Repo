from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points = set()
        total_area = 0

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            total_area += (x2 - x1) * (y2 - y1)

            bottom_left = (x1, y1)
            bottom_right = (x2, y1)
            top_left = (x1, y2)
            top_right = (x2, y2)

            for point in [bottom_left, bottom_right, top_left, top_right]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        if len(points) != 4:
            return False

        # Check if the four corners form a valid rectangle
        corners = sorted(list(points))
        expected_area = (corners[3][0] - corners[0][0]) * (corners[3][1] - corners[0][1])
        
        return total_area == expected_area