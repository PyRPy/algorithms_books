# rectangle_area.py
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0) 
        return (A-C) * (B-D) + (E-G) * (F - H) - overlap 

# test 
A = -3
B = 0 
C = 3
D = 4 
E = 0 
F = -1 
G = 9
H = 2 

sol = Solution() 
print(sol.computeArea(A, B, C, D, E, F, G, H))

# ref : https://www.youtube.com/watch?v=ubPWgYqA3ec