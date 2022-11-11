def before_after(value, a, b):
    
    # Find and validate before-part.
    pos_a = value.find(a)
    # print("texto A:", a)
    # print("pos antes:", pos_a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.find(b)
    # print("texto B ",b)
    # print("pos depois",pos_b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    # print(adjusted_pos_a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    # print(pos_a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]