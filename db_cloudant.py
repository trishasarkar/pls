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


def get_data():
    s1 = {
            '1':{
                'q':'I need to find the way to a shop that a friend has recommended. I would:',
                'V':'find out where the shop is in relation to somewhere I know.',
                'A':'use a map',
                'K':'write down the street directions I need to remember.'
                },
            '2':{
                'q':'I want to find out more about a tour that I am going on. I would:',
                'V':'talk with the person who planned the tour or others who are going on the tour',
                'A':' use a map and see where the places are.',
                'K':'look at details about the highlights and activities on the tour.'
                },
            '3':{
                'q':'I want to find out about a house or an apartment. Before visiting it I would want',
                'V':'to view a video of the property.',
                'A':'a discussion with the owner.',
                'K':'a plan showing the rooms and a map of the area.'
                },
            '4':{
                'q':'I have a problem with my heart. I would prefer that the doctor:',
                'V':'showed me a diagram of what was wrong.',
                'A':'described what was wrong',
                'K':'used a plastic model to show me what was wrong.'
                },
            '5':{
                'q':'I have finished a competition or test and I would like some feedback. I would like to have feedback',
                'V':'from somebody who talks it through with me',
                'A':'using examples from what I have done',
                'K':'using a written description of my results.'
                },
            '6':{
                'q':'A website has a video showing how to make a special graph or chart. There is a person speaking, some lists and words describing what to do and some diagrams. I would learn most from',
                'V':'seeing the diagrams',
                'A':'listening',
                'K':'watching the actions'
                },
            '7':{
                'q':'I want to save more money and to decide between a range of options. I would',
                'V':'consider examples of each option using my financial information.',
                'A':'read a print brochure that describes the options in detail.',
                'K':'talk with an expert about the options.'
                }
            } #
    s3 = {
    '1':{
        'q':'You realized that you have an exam tomorrow. You and your friend decide to do combined studies at your home. How would you tell the address to your friend',
        'V':'Draw the directions on a piece of paper and send it on WhatsApp.',
        'A':'Tell him/her the directions over the phone',
        'K':'Pick up your friend from his/her house'
        },
    '2':{
        'q':'When you meet your friend, how do you greet them?',
        'V':'fist-bump (friendliness/respect/comfort)',
        'A':'Say something (could be witty, insightful, compliment, playful insult)',
        'K':'shakehands/ hug'
        },
    '3':{
        'q':'When you both start preparing for tomorrow’s exam at your house, would you rather',
        'V':'read notes, read headings in a book, and look at diagrams and illustrations',
        'A':'have your friend ask you questions, or repeat facts silently to yourself.',
        'K':'write things out on index cards and make models or diagrams.'
        },
    '4':{
        'q':'When you are anxious about tomorrow’s exam, you would',
        'V':'visualize the worst-case scenarios',
        'A':'talk over your head what worries you the most',
        'K':'can’t sit still, fiddle, and move around constantly'
        },
    '5':{
        'q':'You want to take a break, what would you prefer to do?',
        'V':'watch TV',
        'A':'listen to the radio, play music, or talk with a friend',
        'K':'play sports, work on cars, or go for a walk with your friend.'
        },
    '6':{
        'q':'When you are anxious about tomorrow’s exam, you would',
        'V':'visualize the worst-case scenarios',
        'A':'talk over your head what worries you the most',
        'K':'can’t sit still, fiddle, and move around constantly'
        },
    '7':{
        'q':'You woke up early in the morning to revise for the exam. How would you prefer revising?',
        'V':'write lots of revision notes and diagrams',
        'A':'talk over my notes, alone or with other people ',
        'K':'imagine making the movement or creating the formula'
        },
    '8':{
        'q':'In your examination hall, what disturbs you the most?',
        'V':'People moving in the corridor',
        'A':'Teacher giving instructions or students murmuring during the exam',
        'K':'sensations like hunger, thirst, uncomfortable shoes, or uncomfortable chair.'
        },
    '9':{
        'q':'After completing the exam, you have few doubts regarding the questions given in the exam. You are comfortable',
        'V':'Writing a letter/mail',
        'A':'Discussing the answer over the phone',
        'K':'Go to the staff room/ cabin to clarify your doubts the next day'
        },
    '10':{
        'q':'Having done with your exams, where would you like to go to enjoy yourself',
        'V':'Watching a movie',
        'A':'Attending a concert',
        'K':'An amusement park'
        }} # preparing for an exam with your friend
    s2 = {
    '1':{
        'q':'You’ve decided that you need a table in your room due to the lack of workable space. You decide to leave and go to a hardware store but forget the path to reach the hardware store. How will you figure out the correct road to take?',
        'V':'Follow a map that you have',
        'A':'Ask people for directions ',
        'K':'Follow your instincts and reach the store'
        },
    '2':{
        'q':'Now that you have reached the hardware store, how will you decide which type of table you will buy',
        'V':'Look at a pamphlet',
        'A':'Listen to the recommendations of the customer service',
        'K':'Go around and figure out for yourself'
        },
    '3':{
        'q':'Now that you have decided what type of table you want to buy, how will you finalize the table that you really want?',
        'V':'How it looks, colors, patterns',
        'A':'just by listening to the description of the product that the salesperson offered',
        'K':'by how it felt - its texture and comfor'
        },
    '4':{
        'q':'You want to assemble a wooden table that came in parts. You would learn best from',
        'V':'watching a video of a person assembling a similar toy',
        'A':'talk with an expert about the options',
        'K':'trial and error method'
        }} # getting furniture
    s4 = {
            '1':{
                'q':'Your school has planned an excursion. You want to find out more about a trip that you are going on. You would:',
                'V':'use a map and see where the places are',
                'A':'talk to the person who planned the tour or others who are going with you',
                'K':'Make a blueprint and highlight the activities that you plan on doing on the tour'
                },
            '2':{
                'q':'If you prefer traveling by train over the plane, why would that be the case',
                'V':'Because you can watch the sceneries for a longer time',
                'A':'Because you get a lot of time to talk and enjoy yourself with your friends',
                'K':'Because you feel the train is much safer and reliable than a plane'
                },
            '3':{
                'q':'What is that thing(s), you will not forget carrying with you on any journey?',
                'V':'Tablet to watch films/youtube videos',
                'A':'Earphones/Headphones/iPod',
                'K':'A Rubix cube  '
                },
            '4':{
                'q':'You are tempted to buy an eatable that is being sold in your coach. What might be the preferable reason',
                'V':'The color and how it looks attracted you',
                'A':'You remember your friend telling you how tasty that particular food was.',
                'K':'You would like to try and experiment with new stuff'
                },
            '5':{
                'q':'When you reach your destination, which of the following would you be interested in visiting?',
                'V':'Historical place',
                'A':'A concert',
                'K':'wonderla'
                }
            }

    data = {
    '1': s2,
    '2': s3,
    '3': s4
    }

    return data

##### Create a DB
# response = service.put_database(db='qdata').get_results()
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
  db='qdata',
  doc_id='001'
).get_result()
print(response['data'])
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
