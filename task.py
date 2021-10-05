class CreditCalculation:
    def __init__(self, loan_amount, total_of_commissions, percentages):
        self.loan_amount = loan_amount
        self.total_of_commissions = total_of_commissions
        self.percentages = percentages
        self.credit = 0

    def hello(self):
        self.hi = 'hi'
        return self.hi

    @property
    def credit_calc(self):
        self.percentages = self.loan_amount/100 * self.percentages
        self.credit = self.loan_amount + self.total_of_commissions + self.percentages
        return self.credit
        
    def get_data(self):
        return f'''
Сумма кредита: {self.loan_amount}
Сумма всех комиссий (разовых и ежемесячных): {self.total_of_commissions}
Проценты по кредиту: {self.percentages}%

Финальная сумма кредита: {self.credit_calc}
        '''

    
c = CreditCalculation(10000, 220, 10)

print(c.hello())
print(c.get_data())

# нижний метод работает, просто чтобы в терминале лишнего не было
# print(c.credit_calc)
