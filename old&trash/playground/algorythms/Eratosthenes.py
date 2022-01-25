def eratosthenes(n):
    """
    ��������� �����, �� ������� ����� ����� ������� �����
    ����������� ������ � ������������ �������
    """
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, n + 1):
        if not i:
            continue
        for j in range(i * i, n + 1, i):
            prime[j] = False

    return prime


def get_prime_numbers(arr):
    """
    ��������� ������ � ������������ �������
    ���������� ������ ������� �����
    """
    prime_numbers = []
    for i in enumerate(arr):
        if arr[1]:
            prime_numbers.append(arr[0])

    return prime_numbers
