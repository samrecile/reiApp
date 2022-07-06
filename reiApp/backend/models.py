from django.db import models
import numpy as np

# ANALYSIS MODELS
class Property(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='neighborhood')
    property_type = models.CharField(max_length=50, blank=True, null=True)
    sqf = models.IntegerField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True)
    asking = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    cap_rate =  models.FloatField(blank=True, null=True)
    cash_on_cash = models.FloatField(blank=True, null=True)

#ADVANCED METRICS
    # calculates npv of property
    def calculate_npv(self, interest_rate=.05, rent_growth=.02, duration=30):
        cash_flows = []
        ocf = self.duration_noi()
        npv = np.npv(interst_rate, cash_flows)
        return npv

    # calculates cap rate
    def calculate_caprate(self, value=0):
        noi = (self.duration_noi())[0]
        if value == 0:
            value = self.asking
        capRate = (noi*12)/value
        return capRate

    # calculates cash-on-cash return
    def calculate_cashoncash(self):
        before_tax_cf = (self.egi()[0]*12) - (self.bt_opex()[0])
        cashInvestment = (self.asking*.2)
        cash_on_cash = before_tax_cf/cashInvestment
        return cash_on_cash

    # returns an estimate of the property given the location, size, bedrooms, etc.
    def get_estimate():
        pass

# COMPONENT VALUES (values below are used to caluclate the above expressions)
    # returns iterable of property values for duration of 30-years
    def future_values(self, growth_rate=.02):
        value = self.asking
        property_values = []
        growth_rate = self.area.proj_price_appreciation
        for x in range(30):
            property_values.append(value)
            value *= (1+growth_rate)
        return property_values
    
    # returns iterable of MONTHLY gross rents for the duration of 30-years
    def gross_rent(self):
        property_value = self.future_values()[0]
        rent_sf = self.area.rent_sf
        rent_ratio = self.area.rent_over_value
        rent_appreciation = self.area.proj_rent_appreciation
        gross_rents = []
        rent = ((property_value*rent_ratio)+(self.sqf*rent_sf))/2
        for x in range(30):
            gross_rents.append(rent)
            rent*=rent_appreciation
        return gross_rents

    # returns iterable of MOTHLY effective gross income for the 30-years (gross-vacancy)
    def egi(self):
        egi = [float(grossValue*self.area.occupancy) for grossValue in self.gross_rent()]
        return egi
    
    # returns iterable of each future year's MONTHLY operating expenses without taxes for the duration of 30-years
    def bt_opex(self, insurance=.1, management=.1, maintenance=.075, capex=.10, misc=.05):
        gross_rents = self.gross_rent()
        bt_opex = []
        for rent in gross_rents:
            expense = float(rent)*insurance
            expense += (float(rent)*management)
            expense += (float(rent)*maintenance)
            expense += (float(rent)*capex)
            expense += (float(rent)*misc)
            bt_opex.append(expense)
        return bt_opex

    # returns iterable of each future year's MONTHLY operating expenses with taxes for the duration of 30-years
    def at_opex(self, taxRate=.016):
        bt_opex = self.bt_opex()
        gross_rents = self.gross_rent()
        expense = 0
        at_opex = []
        for x in range(len(gross_rents)):
            taxes = (float(gross_rents[x]) * taxRate)
            opex = bt_opex[x] + taxes
            at_opex.append(opex)
        return at_opex


    # returns iterable of each future year's MONTHLY net operating income for the duration of 30-years
    def duration_noi(self):
        egi = self.egi()
        at_opex = self.at_opex()
        noi = []
        for x in range(len(egi)):
            noi_value = egi[x]-at_opex[x]
            noi.append(noi_value)
        return noi

    # returns iterable of each future year's MONTHLY operating cash flow (after debt service) for the duration of 30-years
    def operating_cf(self):
        noi = self.duration_noi()
        monthly_debt_service = self.calculate_mortgage_payment()
        operating_cf = []
        for noi_value in noi:
            op_cf_value = noi_value - monthly_debt_service
            operating_cf.append(op_cf_value)
        return operating_cf
    
#MORTGAGE CALCULATIONS
    # calculates mortgage payment of property
    def calculate_mortgage_payment(self, down_payment=.2, interest=.05, term=30):
        balance = self.asking - (self.asking*down_payment)
        payment = balance*(interest/(12))*(1+.05/12)^(12*term)/(1+interest/12)^(12*term) - 1
        return payment

    # returns how much equity has been built up
    def calculate_principal(self, balance=0, interest=.05, term=30):
        principal = []

# SALE CALCULATIONS
    def calculate_sale_proceeds(self, year=30, closing_costs=.02, misc_costs=0):
        pass
    
    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        super(Property,self).save()
        if not self.cap_rate:
            self.cap_rate = self.calculate_caprate()
            self.save()
        if not self.cash_on_cash:
            self.cash_on_cash = self.calculate_cashoncash()
            self.save()


class Area(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price_sf = models.DecimalField(max_digits=6, decimal_places=2)
    rent_sf = models.DecimalField(max_digits=5, decimal_places=2)
    rent_over_value = models.DecimalField(max_digits=4, decimal_places=3)
    #rent_per_bed = models.DecimalField(max_digits=4, decimal_places=2)
    proj_price_appreciation = models.DecimalField(max_digits=4, decimal_places=2)
    proj_rent_appreciation = models.DecimalField(max_digits=4, decimal_places=2)
    proj_airb_appreciation = models.DecimalField(max_digits=4, decimal_places=2)
    occupancy = models.DecimalField(max_digits=4, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name


# USER/AUTH MODELS
#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE,)
  #  areas = models.ManyToManyField(Area)

