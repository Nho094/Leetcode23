# import sys
# from collections import deque

# def solve():
#     input = sys.stdin.read
#     data = input().split()
    
#     if not data:
#         return
    
#     t = int(data[0])
#     idx = 1
    
#     out = []
#     for _ in range(t):
#         n = int(data[idx])
#         h = [int(x) for x in data[idx+1 : idx+1+n]]
#         idx += 1 + n
        
#         ans = [0] * n
        
#         # Thử từng bình i làm bình trống
#         for i in range(n):
#             # Khởi tạo mảng lượng nước lớn nhất có thể (vô cùng)
#             w = [float('inf')] * n
#             w[i] = 0
            
#             # Queue để loang (BFS) cập nhật lại chiều cao nước
#             queue = deque([i])
            
#             while queue:
#                 cur = queue.popleft()
                
#                 # 1. Xét bình bên phải (theo chiều kim đồng hồ)
#                 nxt = (cur + 1) % n
#                 # Điều kiện: nước ở nxt không được vượt quá max(w[cur], h[cur])
#                 limit_right = max(w[cur], h[cur])
#                 if w[nxt] > limit_right:
#                     w[nxt] = limit_right
#                     queue.append(nxt)
                
#                 # 2. Xét bình bên trái (ngược chiều kim đồng hồ)
#                 prev = (cur - 1 + n) % n
#                 # Điều kiện: nước ở prev không được vượt quá max(w[cur], h[prev])
#                 limit_left = max(w[cur], h[prev])
#                 if w[prev] > limit_left:
#                     w[prev] = limit_left
#                     queue.append(prev)
            
#             ans[i] = sum(w)
            
#         out.append(" ".join(map(str, ans)))
        
#     print("\n".join(out))

# if __name__ == '__main__':
#     solve()

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        h = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        ans = [0] * n
        m = n - 1  # Số lượng bình còn lại sau khi bỏ đi 1 bình trống
        
        # Thử từng bình k làm bình trống (w[k] = 0)
        for k in range(n):
            # 1. Tạo danh sách các bình (vertices) theo thứ tự mảng thẳng
            # Ví dụ k=1, n=4 -> vertices = [2, 3, 0]
            vertex = []
            for i in range(m):
                vertex.append((k + 1 + i) % n)
                
            # 2. Xác định giới hạn chặn ở 2 đầu (Caps)
            left_cap = h[k]
            right_cap = h[(k - 1 + n) % n]
            
            # 3. Tạo danh sách các vách ngăn (edges) giữa các bình trên mảng thẳng
            edge = []
            for i in range(m - 1):
                edge.append(h[vertex[i]])
                
            # 4. Tính mảng nước dâng tối đa từ bên trái qua (L)
            L = [0] * m
            L[0] = left_cap
            for i in range(1, m):
                L[i] = max(L[i-1], edge[i-1])
                
            # 5. Tính mảng nước dâng tối đa từ bên phải qua (R)
            R = [0] * m
            R[m-1] = right_cap
            for i in range(m - 2, -1, -1):
                R[i] = max(R[i+1], edge[i])
                
            # 6. Lượng nước tại mỗi bình là min(L[i], R[i])
            total_water = 0
            for i in range(m):
                total_water += min(L[i], R[i])
                
            ans[k] = total_water
            
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()