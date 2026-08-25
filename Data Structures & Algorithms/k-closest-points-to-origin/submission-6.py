class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        for loop in range(n):
            point = points[loop]
            dis = point[0]**2 + point[1]**2
            point.append(dis)
        print(points)
        points.sort(key = lambda p:p[2])
        print(points)
        for loop in range(n):
            points[loop].pop()
        return points[:k]
            




         
        