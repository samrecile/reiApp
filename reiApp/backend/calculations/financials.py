# THIS PAGE DEFINES ALL THE MODEL METHODS AS STANDALONE FUNCTIONS
# FOR USE IN VIEWS


#ADVANCED METRICS
    # calculates npv of property
def calculate_npv(interest_rate=.05, rent_growth=.02):
    npv = 0

    # calculates cap rate
def calculate_caprate():
    cap_rate = 0

    # calculates cash-on-cash return
def calculate_cashoncash():
    cash_on_cash = 0

    # returns an estimate of the property given the location, size, bedrooms, etc.
def get_estimate():
    pass

# COMPONENT VALUES (values below are used to caluclate the above expressions)
    # returns iterable of property values for duration of 30-years
def get_property_values(growth_rate=.02, value=0):
    property_values = []
    for x in range(30):
        property_values.append(value)
        value *= (1+growth_rate)
    return property_values
    
    # returns iterable of rents for the duration of 30-years
def get_gross_rent(growth_rate=.02, rent=0):
    property_values = self.get_property_values
    gross_rent = []

    # returns iterable of effective gross income for the 30-years (gross-vacancy)
def get_egi(gross_rent, vacancy=.07):
    pass
    
    # returns iterable of each future year's operating expenses for the duration of 30-years
def get_opex(taxRate=0, insurance=0, management=0, maintenance=0, capex=0, misc=0):
    opex = []
    gross_rents = []

    # returns iterable of each future year's net operating income for the duration of 30-years
def get_duration_noi():
    noi=0

def get_operating_cf(noi):
    pass
    
#MORTGAGE CALCULATIONS
    # calculates mortgage payment of property
def calculate_mortgage_payment(down_payment=.2, interest=.05, term=30):
    balance = self.asking - (self.asking*down_payment)
    payment = balance*(interest/(12))*(1+.05/12)^(12*term)/(1+interest/12)^(12*term) - 1
    return payment

    # returns iterable of principal amounts
def calculate_principal(balance=0, interest=.05, term=30):
    principal = []

    # returns iterable of interest payments
def calculate_interest(balance=0, interest=.05, term=30):
    interest = []

def calculate_debt_balance(ibalance, interest, term, year=0):
    pass

# SALE CALCULATIONS
def calculate_sale_proceeds(year=30, closing_costs=.02, misc_costs=0):
    pass