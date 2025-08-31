def validar_voucher(valor: float) -> bool:
    """
    Verifica se um valor de compra é elegível para um voucher.
    Válido para valores entre 50.00 e 500.00 (inclusive).
    
    Args:
        valor (float): Valor da compra
        
    Returns:
        bool: True se elegível para voucher, False caso contrário
    """
    return 50.00 <= valor <= 500.00