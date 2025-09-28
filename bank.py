bank = {
    "Checking": [
        {"id": "C001", "holder": "alice kim", "balance": 1200.00, "currency": "USD"},
        {"id": "C002", "holder": "B. Lee", "balance": -50.00, "currency": "USD"},
        {"id": "C003", "holder": "Carlos Diaz", "balance": 500.00, "currency": "KGS"},
        {"id": "C004", "holder": "D. Singh", "balance": 3000.00, "currency": "USD"},
        {"id": "C005", "holder": "D. Toktogul", "balance":15000.00, "currency": "KGS"}
    ]
}

rates = {
    "KGS" : 1,
    "USD" : 87.5
}

# 1. Подсчёт счетов
# count_accounts(bank: dict) -> int — вернуть количество счетов в Checking.
def count_accounts(bank):
    count = 0
    for accounts in bank.values():
        for account in accounts:
            count +=1
    return count

# print(count_accounts(bank))

# 2. Итоговый баланс (в валюте)
# total_balance(bank: dict, currency: str, rates: dict[str, float]) -> float —
# суммировать балансы, конвертировав в целевую валюту по rates.
def total_balance(bank, currency, rates):
    total = 0
    for accounts in bank.values():
        for account in accounts:
            acc_currency = account['currency']
            balance = account['balance']
            balance_in_base = balance * rates[acc_currency]
            balance_in_target = balance_in_base / rates[currency]
            total += balance_in_target
    return round(total, 2)

# print(total_balance(bank, "KGS", rates))

# 3. Найти счёт по ID
# find_account(bank: dict, account_id: str) -> dict | None — вернуть запись счёта или None.
def find_account(bank, account_id):
    for values in bank.values():
        for account in values:
            if account['id'] == account_id:
                return account
    return None

# print(find_account(bank, 'C001'))

# 4. Поиск по префиксу владельца
# search_holders(bank: dict, prefix: str) -> list[dict] — без учёта регистра вернуть счета, где holder начинается с префикса.
def search_holders(bank, prefix):
    list = []
    for values in bank.values():
        for account in values:
            if account['holder'][:len(prefix)].lower() == prefix.lower():
                list.append(account)
    return list

# print(search_holders(bank, 'D'))

# 5. Пополнение
# deposit(bank: dict, account_id: str, amount: float) -> bool — увеличить баланс, если счёт существует и amount > 0.
def deposit(bank, account_id, amount):
    for accounts in bank.values():
        for account in accounts:
            if account['id'] == account_id and amount > 0:
                account['balance'] += amount
                return True

# print(deposit(bank, "C002", 100))

# 6. Снятие
# withdraw(bank: dict, account_id: str, amount: float) -> bool — уменьшить баланс, если достаточно средств и amount > 0.
def withdraw(bank, account_id, amount): 
    for accounts in bank.values():
        for account in accounts:
            if account['id'] == account_id and account['balance'] >= amount:
                account['balance'] -= amount
                return True
    return False

# print(withdraw(bank, 'C001', 159))

# 7. Перевод (одна валюта)
# transfer(bank: dict, from_id: str, to_id: str, amount: float) -> bool —
# перевести при совпадении валют и достаточном балансе; атомарно.
def transfer(bank, from_id, to_id, amount):
    from_acc = None
    to_acc = None

    for accounts in bank.values():
        for account in accounts:
            if account['id'] == from_id:
                from_acc = account
            if account['id'] == to_id:
                to_acc = account
        
        if not from_acc or not to_acc:
            return False
        if from_acc['currency'] != to_acc['currency']:
            return False
        if from_acc['balance'] < amount:
            return False

        from_acc['balance'] -= amount
        to_acc['balance'] += amount
        return True

# print(transfer(bank, 'C001', 'C002', 500), bank.values())

# 8. Перевод с конвертацией
# transfer_fx(bank: dict, from_id: str, to_id: str, amount: float, rates:
# dict[str, float]) -> bool — как transfer, но с конвертацией по rates['FROM->TO']; атомарно.
def transfer_fx(bank, from_id, to_id, amount, rates):
    from_acc = None
    to_acc = None

    for accounts in bank.values():
        for account in accounts:
            if account['id'] == from_id:
                from_acc = account
            if account['id'] == to_id:
                to_acc = account
    if not from_acc or not to_acc:
        return False
    if from_acc['balance'] < amount:
            return False
    
    from_currency = from_acc['currency']
    to_currency = to_acc['currency']

    amount_in_kgs = amount * rates[from_currency]
    converted_amount = amount_in_kgs / rates[to_currency]
    
    from_acc['balance'] -= amount
    to_acc['balance'] += round(converted_amount, 2)
    return True

# print(transfer_fx(bank, 'C003', 'C001', 500, rates), bank.values())

# 9. Top-K по балансу
# top_k_accounts(bank: dict, k: int) -> list[dict] — вернуть до k счетов с наибольшим балансом (по убыванию).
def top_k_account(bank, k):
    all_accounts = []

    for accounts in bank.values():
        all_accounts.extend(accounts)

    sorted_accounts = sorted(all_accounts, key = lambda acc: acc['balance'], reverse = True)
    return sorted_accounts[:k]

# print(top_k_account(bank, 3))

# 10. Минимальный баланс
# lowest_balance(bank: dict) -> dict | None — вернуть счёт с наименьшим балансом или None.
def lowest_balance(bank):
    x = float('inf')
    y = {}
    for accounts in bank.values():
        for account in accounts:
            if account['balance'] < x:
                x = account['balance']
                y = account
    return y

# print(lowest_balance(bank))

# 11. Средний баланс по валютам
# avg_balance(bank: dict) -> dict[str, float] — вернуть средний баланс для каждой валюты.
def avg_balance(bank):
    kgs = []
    usd = []
    for accounts in bank.values():
        for account in accounts:
            if account['currency'] == "USD":
                usd.append(account['balance'])
            elif account['currency'] == "KGS":
                kgs.append(account['balance'])
    avg_kgs = round(sum(kgs) / len(kgs), 2)
    avg_usd = round(sum(usd) / len(usd), 2)
    return f"USD average: {avg_usd}; KGS average: {avg_kgs}"

# print(avg_balance(bank))

# 12. Нормализация имён владельцев
# normalize_holders(bank: dict) -> int — обрезать/сжать пробелы и применить Title Case; вернуть число изменений.
def normalize_holders(bank):
    count = 0
    for accounts in bank.values():
        for account in accounts:
            old_name = account['holder']
            new_name = " ".join(old_name.split()).title()
            if new_name != old_name:
                account['holder'] = new_name
                count += 1
    return count

# print(normalize_holders(bank))

# 13. Смена валюты (конвертация)
# set_currency(bank: dict, account_id: str, new_currency: str, rate: float) ->
# bool — конвертировать баланс по rate и установить новую валюту.
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
            
# print(set_currency(bank, 'C001', 'KGS', 87.5))

# 14. Отчёт по счетам
# report(bank: dict) -> dict — вернуть {'total_accounts': int, 'total_per_currency': {...},
# 'avg_balance': float}.
def report(bank):
    total_accounts = 0
    total_balance = 0
    per_currency = {}

    for accounts in bank.values():
        for account in accounts:
            total_accounts += 1
            total_balance += account['balance']
            curr = account['currency']
            per_currency[curr] = per_currency.get(curr, 0) + 1

    avg_balance = total_balance / total_accounts if total_accounts > 0 else 0
    
    return {
        "total_accounts": total_accounts,
        "total_per_currency": per_currency,
        "avg_balance": round(avg_balance, 2)
    }

# print(report(bank))

# 15. Удалить счёт
# remove_account(bank: dict, account_id: str) -> bool — удалить запись по ID; вернуть успех.
def remove_account(bank, account_id):
    for accounts in bank.values():
        for i, account in enumerate(accounts):
            if account['id'] == account_id:
                accounts.pop(i)
                return True
    return False

# print(remove_account(bank, 'C002'))

# 16. Добавить счёт
# add_account(bank: dict, account_id: str, holder: str, balance: float, currency: str) -> bool — добавить, если ID уникален; вернуть успех.
def add_account(bank, account_id, holder, balance, currency):
    for accounts in bank.values():
        for account in accounts:
            if account['id'] == account_id:
                return False
    
    bank['Checking'].append({
        "id": account_id,
        "holder": holder,
        "balance": balance,
        "currency": currency
    })

    return True

# print(add_account(bank, 'C111', 'John Wick', 100000, "USD"), bank['Checking'])

# 17. Прогноз роста
# project_balance(bank: dict, account_id: str, months: int, monthly_rate: float) -> float | None — посчитать будущий баланс при помесячной капитализации; 
# состояние не менять.
def project_balance(bank, account_id, months, monthly_rate):
    for accounts in bank.values():
        for account in accounts:
            if account['id'] == account_id:
                balance = account['balance']
                balance = balance * monthly_rate ** months
    return round(balance, 2)

# print(project_balance(bank, 'C001', 3, 1.1))

# 18. Отрицательные балансы
# negative_balances(bank: dict) -> list[dict] — вернуть счета с balance < 0.
def negative_balances(bank):
    negative = []
    for accounts in bank.values():
        for account in accounts:
            if account['balance'] < 0:
                negative.append(account)
    return negative

# print(negative_balances(bank))

# 19. Распределение по валютам
# currency_distribution(bank: dict) -> dict[str, int] — вернуть количество счетов на каждую валюту.
def currency_distribution(bank):
    distribution = {}
    for accounts in bank.values():
        for account in accounts:
            curr = account['currency']
            distribution[curr] = distribution.get(curr, 0) + 1
            # if curr not in distribution:
            #     distribution[curr] = 0
            # distribution[curr] += 1
    return distribution

# print(currency_distribution(bank))

# 20. Средний баланс
# average_balance(bank: dict) -> float — вернуть средний баланс по всем счетам.
def average_balance(bank):
    total = 0
    count = 0
    for accounts in bank.values():
        for account in accounts:
            total += account['balance']
            count += 1
    return total / count

# print(average_balance(bank))
