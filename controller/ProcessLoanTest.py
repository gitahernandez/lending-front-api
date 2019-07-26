import unittest
from ProcessLoan import ProcessLoan
import json
import os


class TestMyModule(unittest.TestCase):
    loanInformation = {}
    comparison_value = 0

    def test_validate_APPROVED(self):
        requested_amount = 20000
        self.loanInformation = {"businessInformation": {"Id": "123", "name": "Felipe", "Address": "", "city": "", "state": "", "postalCode": "", "requestedamount": requested_amount}, "OwnerInformation": {"SocialSecurityNumber": "", "name": "", "email": "", "address": "", "city": "", "state": "", "postalCode": ""}}
        self.comparison_value = 50000
        processLoan = ProcessLoan(self.loanInformation, self.comparison_value)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "A")
    
    def test_validate_REQUESTED_AMOUNT_AS_STRING(self):
        requested_amount = "20000"
        self.loanInformation = {"businessInformation": {"Id": "123", "name": "Felipe", "Address": "", "city": "", "state": "", "postalCode": "", "requestedamount": requested_amount}, "OwnerInformation": {"SocialSecurityNumber": "", "name": "", "email": "", "address": "", "city": "", "state": "", "postalCode": ""}}
        self.comparison_value = 50000
        processLoan = ProcessLoan(self.loanInformation, self.comparison_value)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "A")

    def test_validate_DECLINED(self):
        requested_amount = 2500000
        self.loanInformation = {"businessInformation": {"Id": "123", "name": "Felipe", "Address": "", "city": "", "state": "", "postalCode": "", "requestedamount": requested_amount}, "OwnerInformation": {"SocialSecurityNumber": "", "name": "", "email": "", "address": "", "city": "", "state": "", "postalCode": ""}}
        self.comparison_value = 50000
        processLoan = ProcessLoan(self.loanInformation, self.comparison_value)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "D")

    def test_validate_UNDECIDED(self):
        requested_amount = 50000
        self.loanInformation = {"businessInformation": {"Id": "123", "name": "Felipe", "Address": "", "city": "", "state": "", "postalCode": "", "requestedamount": requested_amount}, "OwnerInformation": {"SocialSecurityNumber": "", "name": "", "email": "", "address": "", "city": "", "state": "", "postalCode": ""}}
        self.comparison_value = 50000
        processLoan = ProcessLoan(self.loanInformation, self.comparison_value)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['code'], "U")

    def test_validate_ERROR(self):
        requested_amount = "TEST"
        self.loanInformation = {"businessInformation": {"Id": "123", "name": "Felipe", "Address": "", "city": "", "state": "", "postalCode": "", "requestedamount": requested_amount}, "OwnerInformation": {"SocialSecurityNumber": "", "name": "", "email": "", "address": "", "city": "", "state": "", "postalCode": ""}}
        self.comparison_value = 50000
        processLoan = ProcessLoan(self.loanInformation, self.comparison_value)
        result = ProcessLoan.validateLoan(self)
        self.assertEqual(result['message']['name'], "An error was generated")

if __name__ == "__main__":
    unittest.main()
