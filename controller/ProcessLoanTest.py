import unittest
from ProcessLoan import ProcessLoan
import json
import os

class TestMyModule(unittest.TestCase):
    loanInformation = {}
    
    def test_validate_APPROVED(self):
        requested_amount = 20000
        self.loanInformation = { "BusinessInformation":{ "Id": "123", "name": "Felipe", "Address":"", "city":"", "state":"", "postalCode":"", "Requestedamount": requested_amount }, "OwnerInformation":{ "SocialSecurityNumber": "", "name": "", "email": "", "address":"", "city": "", "state": "", "postalCode": "" } }
        processLoan = ProcessLoan(self.loanInformation)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "A")


    def test_validate_DECLINED(self):
        requested_amount = 2500000
        self.loanInformation = { "BusinessInformation":{ "Id": "123", "name": "Felipe", "Address":"", "city":"", "state":"", "postalCode":"", "Requestedamount": requested_amount }, "OwnerInformation":{ "SocialSecurityNumber": "", "name": "", "email": "", "address":"", "city": "", "state": "", "postalCode": "" } }
        processLoan = ProcessLoan(self.loanInformation)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "D")


    def test_validate_UNDECIDED(self):
        requested_amount = 50000
        self.loanInformation = { "BusinessInformation":{ "Id": "123", "name": "Felipe", "Address":"", "city":"", "state":"", "postalCode":"", "Requestedamount": requested_amount }, "OwnerInformation":{ "SocialSecurityNumber": "", "name": "", "email": "", "address":"", "city": "", "state": "", "postalCode": "" } }
        processLoan = ProcessLoan(self.loanInformation)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "U")

    def test_validate_ERROR(self):
        requested_amount = "455"
        self.loanInformation = { "BusinessInformation":{ "Id": "123", "name": "Felipe", "Address":"", "city":"", "state":"", "postalCode":"", "Requestedamount": requested_amount }, "OwnerInformation":{ "SocialSecurityNumber": "", "name": "", "email": "", "address":"", "city": "", "state": "", "postalCode": "" } }
        processLoan = ProcessLoan(self.loanInformation)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['name'], "ERROR")

if __name__ == "__main__":
    unittest.main()