import json
import requests
import simplejson
json_da = json.dumps = {    
   "Body": {        
      "stkCallback": {            
         "MerchantRequestID": "29115-34620561-1",            
         "CheckoutRequestID": "ws_CO_191220191020363925",            
         "ResultCode": 0,            
         "ResultDesc": "The service request is processed successfully.",            
         "CallbackMetadata": {                
            "Item": [{                        
               "Name": "Amount",                        
               "Value": 1.00                    
            },                    
            {                        
               "Name": "MpesaReceiptNumber",                        
               "Value": "NLJ7RT61SV"                    
            },                    
            {                        
               "Name": "TransactionDate",                        
               "Value": 20191219102115                    
            },                    
            {                        
               "Name": "PhoneNumber",                        
               "Value": 254708374149                    
            }]            
         }        
      }    
   }
}
# json_da = data_request.read()
# data = json.loads(json_data)

# json_da = json.dumps(data_request)
# json_da = json.loads(request.body)

print(json_da)

resultcode = json_da['Body']['stkCallback']['ResultCode']
resultdesc = json_da['Body']['stkCallback']['ResultDesc']
# phone = json_da["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
mpesa_reciept = "MPESA"



print("Your statu code is", resultcode)


# import json
# json_data = '{"Body":{"stkCallback":{"MerchantRequestID":"22531-976234-1","CheckoutRequestID":"ws_CO_DMZ_250600506_23022019144745852","ResultCode":0,"ResultDesc":"The service request is processed successfully.","CallbackMetadata":{"Item":[{"Name":"Amount","Value":1.00},{"Name":"MpesaReceiptNumber","Value":"NBN52K8A1J"},{"Name":"Balance"},{"Name":"TransactionDate","Value":20190223144807},{"Name":"PhoneNumber","Value":254725696042}]}}}}'
# data = json.loads(json_data)

# # paid = ""
# # faild = ""

# json_da = data['Body']
# # mpesa = (json_da["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"])


# # list_data = data['CallbackMetadata']

# # for item in json_da["stkCallback"]["CallbackMetadata"]["Item"]:
# # 	if item["Name"] == "MpesaReceiptNumber":
# # 		mx = (item["Value"])

# # print (mx)

# print (json_da)

# # print (list_data)

# merchant = json_da['stkCallback']['MerchantRequestID']
# resultcode = json_da['stkCallback']['ResultCode']
# checkout = json_da['stkCallback']['CheckoutRequestID']
# resultdesc = json_da['stkCallback']['ResultDesc']
# # mpesa = json_da["stkCallback"]["Item"][1]["Value"]
# # phone = json_da["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]

# def status():
# 	if resultcode == 0:
# 		return "paid"
# 	elif resultcode == 1:
# 		return "failed"
# 	else:
# 		return "badrequest"




# print()
# print('mat' " " + merchant)
# print(resultcode)
# print(checkout)
# print(resultdesc)
# print()
# print(mpesa)
# print()

# p =  status()
# print (p)

# print(phone)


# import requests, time
# r = requests.get('https://mainaboutique.herokuapp.com/callbackurl')

# print (r.status_code)
# print (r.content)