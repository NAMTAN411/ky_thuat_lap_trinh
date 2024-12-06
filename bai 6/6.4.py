cc class RomanToInteger:
    def __init__(self):
        # Bảng ánh xạ các ký tự La Mã với giá trị số nguyên
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, roman):
        total = 0
        prev_value = 0
        
        # Duyệt từ phải sang trái
        for char in reversed(roman):
            value = self.roman_numerals.get(char, 0)
            if value < prev_value:
                total -= value  # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó
            else:
                total += value  # Nếu không, cộng vào tổng
            prev_value = value
        
        return total

# Sử dụng class để chuyển đổi số La Mã
converter = RomanToInteger()
roman_number = "MCMXCIV"  # Ví dụ: 1994
integer_value = converter.convert(roman_number)

print(f"Số La Mã '{roman_number}' chuyển đổi thành số nguyên là: {integer_value}")
