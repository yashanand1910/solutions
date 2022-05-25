class Solution:
    def trap(self, elevations: List[int]) -> int:
        n = len(elevations)
        left_walls = [0] * n
        right_walls = [0] * n

        left_max_wall = 0
        for i in range(n):
            left_walls[i] = left_max_wall
            left_max_wall = max(left_max_wall, elevations[i])

        right_max_wall = 0
        for i in reversed(range(n)):
            right_walls[i] = right_max_wall
            right_max_wall = max(right_max_wall, elevations[i])

        water = 0
        for i in range(n):
            water += max(0, min(left_walls[i], right_walls[i]) - elevations[i])

        return water
