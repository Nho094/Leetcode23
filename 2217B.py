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
    solve()