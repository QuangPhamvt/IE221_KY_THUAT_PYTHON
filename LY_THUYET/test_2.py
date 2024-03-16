text = str(input())
def is_symmetry(S):
    if S == S[::-1]:
        return True
    return False

print(is_symmetry(text))

