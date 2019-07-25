from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import os
from controller.ProcessLoan import ProcessLoan

class Information(RequestHandler):

  def set_default_headers(self):
    print("setting headers!!!")
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
    self.set_header('Access-Control-Allow-Methods', ' PUT, DELETE, OPTIONS')

  def post(self):
    processLoan = ProcessLoan(json.loads(self.request.body))
    result = processLoan.validateLoan()
    self.write(result['message'])

  def get(self):
    processLoan = ProcessLoan(json.loads(self.request.body))
    result = processLoan.validateLoan()
    self.write(result['message'])

  def options(self):
    self.finish()
  
def make_app():
  urls = [
    ("/apis/Loan/setInformation", Information),
  ]
  return Application(urls, debug=True)

if __name__ == '__main__':
  application= make_app()
  application.listen(int(os.environ.get("PORT", 5000)))
  print("Listening...")
  IOLoop.instance().start()
