from math import isfinite, sqrt


def main() -> None:
    try:
        coefficients = list(map(float, input("Введите коэффициенты a, b, c: ").split()))
        while len(coefficients) < 3:
            coefficients.extend(map(float, input().split()))
        a, b, c = coefficients
        if not all(map(isfinite, coefficients)):
            raise ValueError
    except (EOFError, ValueError):
        raise SystemExit("Ошибка: введите три конечных числа.") from None

    if a == 0:
        if b != 0:
            print(f"Корень: {-c / b}")
        elif c == 0:
            print("Уравнение выполняется при любом x.")
        else:
            print("Решений нет.")
        return

    discriminant = b * b - 4 * a * c
    if not isfinite(discriminant):
        raise SystemExit("Ошибка: не удалось вычислить дискриминант.")
    denominator = 2 * a
    if discriminant < 0:
        print("Действительных корней нет.")
    elif discriminant == 0:
        print(f"Двойной корень: {-b / denominator}")
    else:
        radical = sqrt(discriminant)
        print(f"Два корня: {(-b - radical) / denominator} и {(-b + radical) / denominator}")


if __name__ == "__main__":
    main()
