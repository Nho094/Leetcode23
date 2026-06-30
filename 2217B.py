<<<<<<< HEAD
import sys 

def solve(): 
    input_data = sys.stdin.read().split()
    if not input_data: 
        return 
    
    iterator = iter(input_data)
    m = int(next(iterator))
    out = []
    
    for _ in range(m): 
        n = int(next(iterator))
        k = int(next(iterator)) 
        
        h = [int(next(iterator)) for _ in range(n)]
        p = int(next(iterator)) - 1 
        
        target = h[p]
        flips = 0
        
        L = 0
        R = n - 1
        
        # Duyệt đồng thời từ 2 phía rìa ngoài dồn dần vào vị trí p
        while L < p or R > p:
            # Nếu con trỏ bên trái chưa chạm tới p
            if L < p:
                current_L = h[L] ^ (flips % 2)
                if current_L != target:
                    flips += 1  # Lật phát này ảnh hưởng đến toàn bộ phần còn lại (gồm cả R)
                L += 1
                
            # Nếu con trỏ bên phải chưa chạm tới p
            if R > p:
                current_R = h[R] ^ (flips % 2)
                if current_R != target:
                    flips += 1  # Lật phát này ảnh hưởng đến toàn bộ phần còn lại (gồm cả L)
                R -= 1
                
        out.append(str(flips))
        
    print('\n'.join(out))

if __name__ == '__main__':
=======
import sys

def solve(): 
    # SỬA: Thêm () vào sau read và đổi tên biến tránh trùng keyword
    input_data = sys.stdin.read().split()
    if not input_data: 
        return 
    m = int(input_data[0])

    idx = 1
    out = []
    for _ in range(m): 
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        a = [int(x) for x in input_data[idx: idx + n]]
        idx += n 
        p = int(input_data[idx]) - 1
        idx += 1
        
        L = 0
        for i in range(p): 
            if a[i] != a[i + 1]: 
                L += 1
                
        R = 0
        for i in range(p, n - 1):
            if a[i] != a[i + 1]: 
                R += 1
                
        ans = max(L, R)

        if ans % 2 != 0: 
            ans += 1
        out.append(str(ans))
        
    print('\n'.join(out))

# SỬA: Chuyển thành câu lệnh if đúng cú pháp
if __name__ == '__main__': 
>>>>>>> a8ddda979c3dba82bc72d55d2e86291ce492790d
    solve()