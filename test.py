import capgain

p = capgain.Portfolio()
p.read_transactions('transaction.csv')
p.get_capgain('Larsen')
