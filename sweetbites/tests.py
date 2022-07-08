from django.test import TestCase
from .models import CustomerInformation
'''from sweetbites.views import MainPage'''

class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'mainpage.html')

    def test_save_post_request(self):
        response = self.client.post('/', {'fullName':'Jennifer Adorable','phoneNo':639683221470, 'Email':'jennifer.adorable@gmail.com',
            'streetNo':'Block 6 Lot 8', 'Barangay':'Sto. Nino', 'Municipal':'Bacoor', 
            'Province':'Cavite', 'zipCode':4114, 'dateDelivery':'04/30/2022', 'timeDelivery':'8:00AM'})
        self.assertEqual(CustomerInformation.objects.count(), 1)

        newCustomerInfo = CustomerInformation.objects.first()

        self.assertEqual(newCustomerInfo.customerName,'Jennifer Adorable')
        self.assertEqual(newCustomerInfo.customerMobileNo, 639683221470)
        self.assertEqual(newCustomerInfo.customerEmail, 'jennifer.adorable@gmail.com')
        self.assertEqual(newCustomerInfo.customerStreet, 'Block 6 Lot 8')
        self.assertEqual(newCustomerInfo.customerBarangay, 'Sto. Nino')
        self.assertEqual(newCustomerInfo.customerMunicipal, 'Bacoor')
        self.assertEqual(newCustomerInfo.customerProvince, 'Cavite')
        self.assertEqual(newCustomerInfo.customerZip, 4114)
        self.assertEqual(newCustomerInfo.customerDate, '04/30/2022')
        self.assertEqual(newCustomerInfo.customerTime, '8:00AM')

    def test_redirect_POST(self):
        response = self.client.post('/', {'fullName':'Jennifer Adorable','phoneNo':639683221470,'Email':'jennifer.adorable@gmail.com',
            'streetNo':'Block 6 Lot 8', 'Barangay':'Sto. Nino', 'Municipal':'Bacoor', 
            'Province':'Cavite', 'zipCode':4114, 'dateDelivery':'04/30/2022', 'timeDelivery':'8:00AM'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(CustomerInformation.objects.count(), 0)
    # def test_responding_POST_request(self):
    #     resp = self.client.post('/', data={'fullName': 'newfullName',
    #         'phoneNo': 'newphoneNo', 'Email': 'newEmail', 'streetNo': 'newstreetNo', 
    #         'Barangay': 'newBarangay', 'Municipal': 'newMunicipal', 'Province': 'newProvince', 
    #         'zipCode': 'newzipCode', 'dateDelivery': 'newdateDelivery', 'timeDelivery': 'newtimeDelivery' })
    #     self.assertIn('fullName', resp.content.decode())
    #     self.assertTemplateUsed(resp,'mainpage.html')

class ORMTEST(TestCase):
    def test_saving_and_retrieving(self):
        samplePersonalInfo = CustomerInformation()
        samplePersonalInfo.customerName = 'Jennifer Adorable'
        samplePersonalInfo.customerMobileNo = 639683221470
        samplePersonalInfo.customerEmail = 'jennifer.adorable@gmail.com'
        samplePersonalInfo.customerStreet = 'Block 6 Lot 8'
        samplePersonalInfo.customerBarangay = 'Sto. Nino'
        samplePersonalInfo.customerMunicipal = 'Bacoor'
        samplePersonalInfo.customerProvince = 'Cavite'
        samplePersonalInfo.customerZip = 4114
        samplePersonalInfo.customerDate = '04/30/2022'
        samplePersonalInfo.customerTime = '8:00AM'
        samplePersonalInfo.save()

        lists = CustomerInformation.objects.all()
        self.assertEqual(lists.count(), 1)

        list1 = lists[0]

        self.assertEqual(list1.customerName,'Jennifer Adorable')
        self.assertEqual(list1.customerMobileNo, 639683221470)
        self.assertEqual(list1.customerEmail, 'jennifer.adorable@gmail.com')
        self.assertEqual(list1.customerStreet, 'Block 6 Lot 8')
        self.assertEqual(list1.customerBarangay, 'Sto. Nino')
        self.assertEqual(list1.customerMunicipal, 'Bacoor')
        self.assertEqual(list1.customerProvince, 'Cavite')
        self.assertEqual(list1.customerZip, 4114)
        self.assertEqual(list1.customerDate, '04/30/2022')
        self.assertEqual(list1.customerTime, '8:00AM')

    def test_template_display_list(self):
        CustomerInformation.objects.create(
            customerName= 'Jennifer Adorable', customerMobileNo= 639683221470, customerEmail='jennifer.adorable@gmail.com',
            customerStreet='Block 6 Lot 8', customerBarangay='Sto. Nino', customerMunicipal='Bacoor',
            customerProvince='Cavite', customerZip='4114', customerDate='04/30/2022', customerTime='8:00AM')

        response = self.client.get('/')
        self.assertIn('1: Jennifer Adorable, jennifer.adorable@gmail.com, 639683221470, Block 6 Lot 8, Sto. Nino, Bacoor, Cavite, 4114, 04/30/2022, 8:00AM', response.content.decode())
