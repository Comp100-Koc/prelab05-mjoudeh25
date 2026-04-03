def add_bits_manual(b1, b2, carry):
    count = 0
    if b1 == "1": count += 1
    if b2 == "1": count += 1
    if carry == 1: count += 1

    if count == 0: return "0", 0
    if count == 1: return "1", 0
    if count == 2: return "0", 1
    if count == 3: return "1", 1

def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    
    a_bits = a[2:]
    b_bits = b[2:]
    
    res = ""
    carry = 0
    
    max_len = len(a_bits)
    if len(b_bits) > max_len:
        max_len = len(b_bits)
        
    for i in range(1, max_len + 1):
        bit_a = a_bits[-i] if i <= len(a_bits) else "0"
        bit_b = b_bits[-i] if i <= len(b_bits) else "0"
        
        char, carry = add_bits_manual(bit_a, bit_b, carry)
        res = char + res
        
    if carry == 1:
        res = "1" + res

    while len(res) > 1 and res[0] == "0":
        res = res[1:]
        
    return "0b" + res