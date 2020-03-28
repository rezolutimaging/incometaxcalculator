
import pytest

class Tax:
    
    def __init__(self, ord_income=0, st_cap_gains=0, lt_cap_gains_income=0, deduction=12200):
        
        self.tot_ord_inc = ord_income + st_cap_gains 
        self.ord_taxable_inc = max(ord_income - deduction, 0)
        self.lt_cap_tax_inc = max(self.ord_taxable_inc + lt_cap_gains_income, 0)

        self.ord_income_brackets = [9700,39475,84200,160725,204100, 510300, 1000000000000]
        self.lt_cap_gains_brackets = [39375, 434500, 100000000000]

        self.ord_income_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
        self.lt_cap_gains_rates = [0, 0.15, 0.2] 

        self.tax_due = Tax.liability(self, self.ord_taxable_inc, self.ord_income_brackets, self.ord_income_rates)
        self.tax_due += (self.liability(self.lt_cap_tax_inc, self.lt_cap_gains_brackets, self.lt_cap_gains_rates)-self.liability(self.ord_taxable_inc, self.lt_cap_gains_brackets, self.lt_cap_gains_rates))

    def liability(self, income, tax_brackets=[], tax_rates=[]):

        liability = 0 
        for i in list(range(len(tax_brackets))):
            max_income = tax_brackets[i]
            if i==0:
                min_income = 0 
            else:
                min_income = tax_brackets[i-1]+0.0001
            rate = tax_rates[i]
            
            #calculate tax due for this bracket i
            bracket_top_income = max(min(income, max_income), min_income)   
            bracket_taxable_income = bracket_top_income - min_income
            liability += (bracket_taxable_income*rate)

        return liability


    #tests
    def test_liability():
        assert int(Tax(127002).tax_due) == 2172
