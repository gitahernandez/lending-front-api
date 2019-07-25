class ProcessLoan:
    loanInformation = {}

    def __init__(self, loanInformation): 
        self.loanInformation = loanInformation

    def validateLoan(self):
      try:
        requestedamount = int(self.loanInformation['businessInformation']['requestedamount'])
        if requestedamount <= 0:
          return {'message': {'code': 'I', 'name': 'INVALID REQUESTED AMOUNT'}}
        elif requestedamount > 50000:
          return {'message': {'code': 'D', 'name': 'DECLINED', 'label': 'danger'}}
        elif requestedamount == 50000:
          return {'message': {'code': 'U', 'name': 'UNDECIDED', 'label': 'secondary'}}
        elif requestedamount < 50000:
          return {'message': {'code': 'A', 'name': 'APPROVED', 'label': 'success'}}
      except Exception as exception:
          error = 'Error generated {} {}'.format(exception, self.loanInformation)
          return {'message': {'code': 'ERROR', 'name': 'An error was generated', 'label': 'danger' }}