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
        h = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += n + 1
        ans = []
        for i in range(n): 
            w = [0] * n
            
            # Bước 1: Loang theo chiều kim đồng hồ lấy chặn trên từ tường
            for step in range(1, n): 
                curr = (i + step) % n
                prev = (curr - 1) % n
                w[curr] = h[prev]

            # Bước 2: Loang ngược chiều kim đồng hồ lấy max có thể giữ
            for step in range(1, n): 
                curr = (i - step) % n 
                w[curr] = max(w[curr], h[curr])
            
            # Ép buộc bình i phải trống rỗng
            w[i] = 0
            
            # Bước 3: SỬA LẠI TẠI ĐÂY - Hạ nước xuống nếu vượt quá tường (xuôi)
            for step in range(1, n): 
                curr = (i + step) % n
                prev = (curr - 1) % n 
                if w[curr] > h[prev]:       # Nếu nước cao hơn tường
                    w[curr] = w[prev]       # Nước bị tràn và bằng bình trước
                    
            # Bước 4: SỬA LẠI TẠI ĐÂY - Hạ nước xuống nếu vượt quá tường (ngược)
            for step in range(1, n): 
                curr = (i - step) % n
                nxt = (curr + 1) % n        # Đổi 'next' thành 'nxt'
                if w[curr] > h[curr]:       # Nếu nước cao hơn tường
                    w[curr] = w[nxt]        # Nước bị tràn và bằng bình sau
                    
            ans.append(str(sum(w)))
        out.append(" ".join(ans))
    print("\n".join(out))

if __name__ == "__main__": 
    solve()