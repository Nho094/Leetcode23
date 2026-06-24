import sys
from collections import deque

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
        
        # Thử từng bình i làm bình trống
        for i in range(n):
            # Khởi tạo mảng lượng nước lớn nhất có thể (vô cùng)
            w = [float('inf')] * n
            w[i] = 0
            
            # Queue để loang (BFS) cập nhật lại chiều cao nước
            queue = deque([i])
            
            while queue:
                cur = queue.popleft()
                
                # 1. Xét bình bên phải (theo chiều kim đồng hồ)
                nxt = (cur + 1) % n
                # Điều kiện: nước ở nxt không được vượt quá max(w[cur], h[cur])
                limit_right = max(w[cur], h[cur])
                if w[nxt] > limit_right:
                    w[nxt] = limit_right
                    queue.append(nxt)
                
                # 2. Xét bình bên trái (ngược chiều kim đồng hồ)
                prev = (cur - 1 + n) % n
                # Điều kiện: nước ở prev không được vượt quá max(w[cur], h[prev])
                limit_left = max(w[cur], h[prev])
                if w[prev] > limit_left:
                    w[prev] = limit_left
                    queue.append(prev)
            
            ans[i] = sum(w)
            
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()