n, m = [int(num) for num in input().split()]

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

output = n_set.intersection(m_set)
print(*output, sep="\n")
