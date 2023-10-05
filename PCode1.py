
def is_perfect_square_cube(factorization):
    square_factors = {}
    cube_factors = {}
    // 111111111111
    for num, factor in factorization:
        if factor % 2 == 0: 
            square_factors[num] = factor // 2
        if factor % 3 == 0:
            cube_factors[num] = factor // 3

    return all(num in square_factors and num in cube_factors for num in set(square_factors) | set(cube_factors))

def main():
    n = int(input())
    factorization = []

    for _ in range(n):
        num, factor = map(int, input().split())
        factorization.append((num, factor))

    if is_perfect_square_cube(factorization):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()


