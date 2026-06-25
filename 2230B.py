import sys 

def solve():
    # Đọc toàn bộ dữ liệu từ input cùng một lúc
    input_data = sys.stdin.read().split()

    if not input_data: 
        return 
    
    # data[0] chính là số lượng test cases (t)
    t = int(input_data[0])
    out = []
    
    # Duyệt qua từng test case từ vị trí 1 đến t
    for k in range(1, t + 1):
        s = input_data[k]  # SỬA TỪ: input[k] THÀNH input_data[k]
        count_4 = 0 
        fil = []
        
        # Bước 1: Lọc bỏ chữ số '4'
        for char in s: 
            if char == '4': 
                count_4 += 1
            else: 
                fil.append(char)
        l = len(fil)

        if l == 0: 
            out.append(str(count_4))
            continue

        # Bước 2: Tạo mảng tiền tố đếm '1' và '3'
        prefix_13 = [0] * (l + 1)
        for i in range(l): 
            is_13 = 1 if (fil[i] == '1' or fil[i] == '3') else 0
            prefix_13[i + 1] = prefix_13[i] + is_13
            
        total_13 = prefix_13[l]
        min_deleted_in_fil = l - total_13  # Số ký tự xóa nhỏ nhất trong chuỗi fil
        
        # Bước 3: Tìm vách ngăn tối ưu
        for i in range(l + 1):
            left_13 = prefix_13[i]
            right_13 = total_13 - left_13
            right_2 = (l - i) - right_13   # SỬA LỖI CHÍNH TẢ: righ_2 -> right_2
            
            curr = left_13 + right_2
            if curr < min_deleted_in_fil:
                min_deleted_in_fil = curr
                
        out.append(str(count_4 + min_deleted_in_fil))
        
    # In toàn bộ kết quả
    print("\n".join(out))

if __name__ == '__main__':
    solve()