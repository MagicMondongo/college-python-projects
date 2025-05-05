def fibonacci(n):
    fib = 0  # única variável
    for i in range(n + 1):
        if i == 0:
            fib = 0
        elif i == 1:
            fib = 1
        else:
            # Fórmula de Binet (φ^n - ψ^n)/√5
            phi = (1 + 5**0.5) / 2
            fib = round(phi**i / 5**0.5)
        print(f"F({i}) = {fib}")

fibonacci(10)