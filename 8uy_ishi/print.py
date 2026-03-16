n = 5

print("hello\n"*n)

print(*range(1,n+1))

print(*[i * j for i in range(1, n+1) for j in range(1,n+1)], sep=" ")

print(*range(1,n+1), "*", *range(1,n+1), "=", *[i * j for i in range(1, n+1) for j in range(1,n+1)])

print(*[i for i in range(1, n+1)],"*",*[i for i in range(1, n+1)], "=",*[i * j for i in range(1, n+1) for j in range(1,n+1)] )

print(*["*"*i for i in range(1, n+1)], sep="\n", end="\n\n")

print(*["*"*i for i in range(n, 0, -1)], sep="\n", end="\n\n")

print(*["*"*i for i in range(1, n+1)],*["*"*i for i in range(n-1, 0, -1)] , sep="\n", end="\n\n")

print(*(*["*"*i for i in range(1, n+1)] , *["*"*i for i in range(n-1, 0, -1)])* 2 , sep="\n", end="\n\n")

n = 9
print(*[" ".join(f"{i}*{j}={i*j:2}" for j in range(1, n+1)) for i in range(1, n+1)], sep="\n", end="\n\n")

n = 9
print(*[" | ".join(f"{i}*{j}={i*j:3}" for j in range(1, n+1)) for i in range(1, n+1)], sep="\n", end="\n\n")

n = 12
print(*["|".join(f"{i:2}*{j:2}={i*j:3}" for j in range(1, n+1)) for i in range(1, n+1)], sep="\n", end="\n\n")

n = 5
print(*[" "*(n-i) + "*"*i for i in range(1, n+1)], sep="\n", end="\n\n")

print(*[" "*(n-i) + "*"*i for i in range(n, 0, -1)], sep="\n", end="\n\n")

print(*[" "*(n-i) + "*"*i for i in range(1, n+1)], *[" "*(n-i) + "*"*i for i in range(n-1, 0, -1)],sep="\n", end="\n\n")

print(*[" "*(n-i//2) + "*"*i for i in range(1, n*2, 2)], sep="\n", end="\n\n")

print(*[" "*(n-i//2) + "*"*i for i in range(n*2-1, 0, -2)], sep="\n", end="\n\n")

print(*[" "*(n-i//2) + "*"*i for i in range(1, n*2, 2)], *[" "*(n-i//2) + "*"*i for i in range((n-1)*2-1, 0, -2)],sep="\n", end="\n\n")

print(*["".join(f"{'@ '}{'   ' * (n-i-1)}{' * '*(i+2)}") for i in range(n)], sep = "\n")