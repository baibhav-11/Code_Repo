class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create a 2D array to represent the glasses and initialize all to 0
        glasses = [[0.0] * (i + 1) for i in range(query_row + 1)]
        
        # Pour the initial amount of champagne into the top glass
        glasses[0][0] = poured
        
        # Simulate the champagne flow
        for row in range(query_row):
            for col in range(row + 1):
                # Calculate the excess champagne that flows to the two glasses below
                excess = max(0, glasses[row][col] - 1)
                flow = excess / 2.0
                
                # Distribute the excess equally to the two glasses below
                glasses[row + 1][col] += flow
                glasses[row + 1][col + 1] += flow
        
        # Ensure the amount of champagne in the target glass is within [0, 1]
        return min(1.0, glasses[query_row][query_glass])
