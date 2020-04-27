def mutate_string(string, position, character):
    s_new=list(string)
    s_new[int(i)]=c
    string="".join(s_new)
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
