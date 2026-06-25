import sys 
def solve():
    input = sys.stdin.read
    data  = input().split()

    if not data: 
        return 
    m = int(data[0])

    idx = 1
    out = []
    for _ in range(m): 
        n = int (data[idx])
        h = [int(x) for x in data[idx + 1: idx + n + 1]]
        idx += n + 1

        total = sum(h)
        ones = 0
        slots = 0
        for val in h: 
            if val == 1: 
                ones += 1
            else: 
                slots += (val // 2) - 1
        if ones == n -1: 
            slots += 1
        
        wasted = max(0, ones - slots)
        ans = total - wasted
        if ans < 3: 
            out.append("0")
        else: 
            out.append(str(ans))
    print("\n".join(out))
if __name__ == '__main__':
    solve()