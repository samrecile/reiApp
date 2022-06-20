from django.test import TestCase
from .models import Property, Neighborhood, Zipcode

# Create your tests here.
class TestModels(TestCase):
    
    def setUp(self):

        self.Zipcode = Zipcode.objects.create(
            code='70125',
            city='New Orleans',
            state='LA',
            price_sf=150,
            rent_sf=2,
            rent_over_value=.02,
            rent_per_bed=750,
            proj_price_appreciation=.019,
            proj_rent_appreciation=.021,
            proj_airb_appreciation=.022,
            occupancy=.935,
            tax_rate=.0169,
        )

        self.neighborhood = Neighborhood.objects.create(
            name='Midcity',
            city='New Orleans',
            state='LA',
            price_sf=150,
            rent_sf=2,
            rent_over_value=.02,
            rent_per_bed=750,
            proj_price_appreciation=.019,
            proj_rent_appreciation=.021,
            proj_airb_appreciation=.022,
            occupancy=.935,
            tax_rate=.0169,
        )
        


    def test_date_and_active_fields(self):
        pass

    def test_get_property_values(self):
        self.property1 = Property.objects.create(
            address='2431 Broadway St',
            city='New Orleans',
            state='LA',
            neighborhood=self.neighborhood,
            zipcode=self.Zipcode,
            property_type='multi',
            sqf=4000,
            beds=8,
            baths=6,
            asking=200,
        )
        self.assertEquals(self.property1.get_property_values, [200, 204.0, 208.08, 212.2416, 216.486432, 220.81616064000002, 225.23248385280002, 229.737133529856, 234.33187620045314, 239.0185137244622, 243.79888399895145, 248.67486167893048, 253.6483589125091, 258.7213260907593, 263.8957526125745, 269.173667664826, 274.55714101812254, 280.048283838485, 285.6492495152547, 291.3622345055598, 297.189479195671, 303.13326877958445, 309.19593415517613, 315.37985283827965, 321.68744989504523, 328.12119889294615, 334.6836228708051, 341.3772953282212, 348.2048412347856, 355.1689380594813])