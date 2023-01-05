from email import message
from locale import setlocale
import json

class ServiceResult:
    code = 200
    msg = ""
    data = dict()

    def __init__(self, code = code, msg = msg, data = data):
        self.code = code
        self.msg = msg
        self.data = data

    
    def make_response(self):
        code = self.code
        msg = self.msg
        results = self.data
        o_m = msg
        status = ""

        if results == None:
            return {
                status  : "error",
                code    : 500,
                message : "Something went wrong, Please try again later"
            }
        if( code == 200 or code == 201 or code == 202 or code == 204 ):
            status = "success"
            if code == 200:
                msg = "Fetched Successfully"
            if code == 201:
                msg = "Added successfully"
            if code == 202:
                msg = "Updated successfully"
            if code == 204:
                msg = "Deleted successfully"
            
        else:
            status = "error"
            if code == 404:
                msg = "Resource not found"
            if code == 400:
                msg = "Validation error"
            if code == 401:
                msg = "Invalid Access Token" 
            if code == 403:
                msg = "Access denied"
            if code == 409:
                msg = "Request caused a conflict."
            if code == 500:
                msg = "Something went wrong"
            
        if msg is None:
            msg = o_m

        return {
            "status"  : status,
            "code"    : code,
            "message" : msg,
            "results" : results
        }

