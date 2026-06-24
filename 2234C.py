import sys

def solve():
    # Đọc nhanh toàn bộ dữ liệu từ đầu vào
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        h = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        ans = [0] * n
        m = n - 1

        for k in range(n):
            # vector<long long> vertex(m);
            vertex = [0] * m
            for i in range(m):
                vertex[i] = (k + 1 + i) % n

            left_cap = h[k]
            right_cap = h[(k - 1 + n) % n]

            # vector<long long> edge(m - 1);
            edge = [0] * (m - 1)
            for i in range(m - 1):
                edge[i] = h[vertex[i]]

            # vector<long long> L(m);
            L = [0] * m
            L[0] = left_cap
            for i in range(1, m):
                L[i] = max(L[i - 1], edge[i - 1])

            # vector<long long> R(m);
            R = [0] * m
            R[m - 1] = right_cap
            for i in range(m - 2, -1, -1):
                R[i] = max(R[i + 1], edge[i])

            total_sum = 0
            for i in range(m):
                total_sum += min(L[i], R[i])

            ans[k] = total_sum

        # Lưu kết quả của test case hiện tại
        out.append(" ".join(map(str, ans)))
        
    # In ra toàn bộ kết quả một lượt
    print("\n".join(out))

if __name__ == '__main__':
    solve()