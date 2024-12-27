def correct_brackets(pattern):
    if pattern.count('(') == pattern.count(')'):
        return True
    else:
        return False

print(correct_brackets("()(())"))
    