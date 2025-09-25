bank = {
    "Checking": [
        {"id": "C001", "holder": "Alice Kim", "balance": 1200.00, "currency": "USD"},
        {"id": "C002", "holder": "B. Lee", "balance": -50.00, "currency": "USD"},
        {"id": "C003", "holder": "Carlos Diaz", "balance": 500.00, "currency": "KGS"},
        {"id": "C004", "holder": "D. Singh", "balance": 3000.00, "currency": "USD"},
        {"id": "C005", "holder": "E. Toktogul", "balance":15000.00, "currency": "KGS"}
    ]
}

def set_currency(bank: dict, account_id: str, new_currency: str, rate: float):
    for accounts in bank.values():
        for v in accounts:
            if v['id'] == account_id:
                v['currency'] = new_currency
                if new_currency == 'USD':
                    v['balance'] = v['balance'] / rate
                elif new_currency == 'KGS':
                    v['balance'] = v['balance'] * rate
                return True
    return False
            

print(set_currency(bank, 'C001', 'KGS', 87.5))
print(set_currency(bank, 'C002', 'KGS', 87.5))
print(set_currency(bank, 'C003', 'USD', 87.5))
print(bank.values())

