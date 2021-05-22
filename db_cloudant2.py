from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

CLOUDANT_URL="https://apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt:f70c9a73c52d287d3271ddc3dba6a30a@dc1a5ff5-996b-475c-8b7e-da87f4bf33a3-bluemix.cloudantnosqldb.appdomain.cloud"
CLOUDANT_APIKEY="C8J8TcTL_T9YlMtyA6itWueAqAdkgGXbwOc8RA2omfCd"
CLOUDANT_USERNAME="apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt"
CLOUDANT_PASSWORD="f70c9a73c52d287d3271ddc3dba6a30a"

authenticator = IAMAuthenticator(CLOUDANT_APIKEY)
service = CloudantV1(authenticator=authenticator)
service.set_service_url(CLOUDANT_URL)
response = service.get_server_information().get_result()


##### Create a DB
# response = service.put_database(db='usessions')
# print(response)
#####

##### Create a document
# products_doc = Document(
#   id="001",
#   data = get_data()
#   )
#
# response = service.post_document(db='qdata', document=products_doc).get_result()
# print(response)
#####

#### Get data
response = service.get_document(
  db='usessions',
  doc_id='mCWSwjuLuH'
).get_result()
print(response)
_rev = response['_rev']
####

##### Update data
# new_doc = Document(
#     rev=_rev,
#     data=get_data()
# )
# response = service.put_document(
#   db='qdata',
#   doc_id = '001',
#   document=new_doc
# ).get_result()

#####



# def create_question(request_dict):
#   question=Document(
#       id=request_dict['id'],
#       type="question",
#       question_text=request_dict['text'],
#       options=request_dict['options']
#       )
#   response = service.post_document(db='questions_db', document=question).get_result()
#   print(response)
#
# req={"id":"q003",
#      "text":"This is the first question",
#      "options":['option 1', 'option 2','option 3']
# }
#
# create_question(req)
#
# def update_question(doc_id, request_dict):
#   question=Document(
#       rev=request_dict['rev'],
#       type="question",
#       question_text=request_dict['text'],
#       options=request_dict['options']
#   )
#   response = service.put_document(db='questions_db', doc_id=doc_id,document=question).get_result()
#   print(response)
#
# req={
#     "rev":"2-7b23212b63dd888e94c7379a109a30cf",
#     "text":"This is not the first question",
#      "options":['Noption 1', 'Noption 2','Noption 3']}
#
# doc_id="q003"
# update_question(doc_id, req)
