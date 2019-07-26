class ProcessLoan:
    loanInformation = {}
    comparison_value = 0

    def __init__(self, loanInformation, comparison_value):
        self.loanInformation = loanInformation
        self.comparison_value = comparison_value

    def validateLoan(self):
        try:
            requestedamount = int(self.loanInformation['businessInformation']['requestedamount'])
            if requestedamount <= 0:
                return {'message': {'code': 'I', 'name': 'INVALID REQUESTED AMOUNT'}}
            elif requestedamount > self.comparison_value:
                return {'message': {'code': 'D', 'name': 'DECLINED', 'label': 'danger'}}
            elif requestedamount == self.comparison_value:
                return {'message': {'code': 'U', 'name': 'UNDECIDED', 'label': 'secondary'}}
            elif requestedamount < self.comparison_value:
                return {'message': {'code': 'A', 'name': 'APPROVED', 'label': 'success'}}
        except Exception as exception:
            error = 'Error generated {} {}'.format(exception, self.loanInformation)
            return {'message': {'code': error, 'name': 'An error was generated', 'label': 'danger'}}