from typing import List


def eh_primo(numero: int) -> bool:
    """Checks if a given integer is a prime number.

    Uses square root optimization for better performance. Time complexity: O(√n).
    Space complexity: O(1).

    Args:
        numero (int): The integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, recebido {type(numero).__name__}")
    
    if numero <= 1:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    limite_superior = int(numero ** 0.5) + 1
    
    for divisor_teste in range(3, limite_superior, 2):
        if numero % divisor_teste == 0:
            return False
    
    return True


def listar_primos(inicio: int, fim: int) -> List[int]:
    if not isinstance(inicio, int) or not isinstance(fim, int):
        raise TypeError("Ambos os argumentos devem ser inteiros")
    
    if inicio > fim:
        return []
    
    return [num for num in range(inicio, fim + 1) if eh_primo(num)]


def contar_primos(inicio: int, fim: int) -> int:
    return len(listar_primos(inicio, fim))


if __name__ == "__main__":
    print("=" * 60)
    print("VERIFICAÇÃO DE NÚMEROS PRIMOS")
    print("=" * 60)
    
    numeros_teste = [1, 2, 3, 4, 5, 10, 17, 20, 29, 100, 97, 121]
    
    print("\n📊 Teste Individual:")
    print("-" * 60)
    
    for num in numeros_teste:
        eh_primo_resultado = eh_primo(num)
        status = "✓ PRIMO" if eh_primo_resultado else "✗ NÃO PRIMO"
        print(f"  {num:3d} → {status}")
    
    print("\n" + "=" * 60)
    print("PRIMOS EM INTERVALOS")
    print("=" * 60)
    
    intervalos = [(1, 20), (20, 50), (100, 120)]
    
    for inicio, fim in intervalos:
        primos = listar_primos(inicio, fim)
        quantidade = len(primos)
        print(f"\n📍 De {inicio} até {fim}: {quantidade} primo(s)")
        print(f"   {primos}")
    
    print("\n" + "=" * 60)
    print("CONTAGEM DE PRIMOS")
    print("=" * 60)
    
    ranges = [(1, 10), (1, 100), (1, 1000)]
    
    for inicio, fim in ranges:
        quantidade = contar_primos(inicio, fim)
        print(f"  Primos de {inicio:4d} até {fim:4d}: {quantidade:4d}")
    
    print("\n" + "=" * 60)
    print("VALIDAÇÃO DE ENTRADA")
    print("=" * 60)
    
    print("\n  Testando com argumento inválido:")
    try:
        eh_primo("17")
    except TypeError as erro:
        print(f"  ❌ Erro capturado: {erro}")
    
    print("\n✅ Todos os testes completados com sucesso!")
