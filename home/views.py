from django.shortcuts import render, redirect, HttpResponse
from django.utils.safestring import mark_safe
from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import random, string
import requests

def choose_category():
    value = '''

    <div class="received-chats old-chats"><div class="received-chats-img"><img src="https://data.cometchat.com/assets/images/avatars/captainamerica.png" alt="Avatar" class="avatar"></div>
    <div class="received-msg"><div class="received-msg-inbox">

    <p>
    <span id="message-sender-id">PLS bot</span><br>
    Welcome to IBM's PLS bot.
    </p>

    </div></div></div>

    <div class="received-chats old-chats"><div class="received-chats-img"><img src="https://data.cometchat.com/assets/images/avatars/captainamerica.png" alt="Avatar" class="avatar"></div>
    <div class="received-msg"><div class="received-msg-inbox">

    <p>
    <span id="message-sender-id">PLS bot</span><br>
    Please select the category to continue <br><br>

    <input type="checkbox" name="1" value="1" id='1'>
    <label style="color:rgb(100,100,100);font-weight:normal;" for="1">Outdoor Classroom Experience</label><br>
    <input type="checkbox" name="2" value="2">
    <label style="color:rgb(100,100,100);font-weight:normal;" for="2">Under Lockdown</label><br>
    <input type="checkbox" name="3" value="3">
    <label style="color:rgb(100,100,100);font-weight:normal;" for="3">Rockclimbing</label><br><br>

    <button style="color:rgb(225,225,225);font-weight:normal;" class="login-btn" type="submit">Next</button>
    </p>
    </div></div></div>

    '''
    return value
def get_data():

    # CLOUDANT_USERNAME="apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt"
    # CLOUDANT_PASSWORD="f70c9a73c52d287d3271ddc3dba6a30a"
    #
    # authenticator = IAMAuthenticator("C8J8TcTL_T9YlMtyA6itWueAqAdkgGXbwOc8RA2omfCd")
    # service = CloudantV1(authenticator=authenticator)
    # service.set_service_url("https://apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt:f70c9a73c52d287d3271ddc3dba6a30a@dc1a5ff5-996b-475c-8b7e-da87f4bf33a3-bluemix.cloudantnosqldb.appdomain.cloud")
    # response = service.get_server_information().get_result()
    #
    # response = service.get_document(db='qdata', doc_id='001').get_result()

    url = "https://api.npoint.io/c4b4edd3640ed8357987"

    r = requests.get(url)
    data = r.json()

    return data #response['data']
def get_scene():
    scene = {
    '1':'Outdoor Classroom Experience',
    '2':'Under Lockdown',
    '3':'Rockclimbing'
    }
    return scene

def home(request):
    return render(request, 'home/home.html')

def info(request):
    request.session['responses'] = list('')
    request.session['unanswered'] = list('')
    request.session['ansd'] = list('')
    request.session['ansd2'] = list('')
    return render(request, 'home/info.html')

def scenario(request):
    if request.method == 'POST':
        return render(request, 'home/quiz.html')

    return render(request, 'home/scenario.html')

def resultsPage(request):
    responses = list(request.session['responses'])
    responses = [i for i in responses if i != ['']]
    responses = [i for i in responses if i != ['jump']]
    responses = [i for i in responses if i != ['exit']]

    res = [sum(i)/len(responses) for i in zip(*responses)]

    ansd = list(request.session['ansd'])
    ansd = [i for i in ansd if i != ['']]
    ansd = [i for i in ansd if i != ['jump']]
    ansd = [i for i in ansd if i != ['exit']]

    tlist = []
    data = get_data()

    results = request.session['results']
    n_s = len(results) # no of scenarios selected

    for x in results:
        q_data = data[x]
        n = len(q_data)
        for y in range(1, n+1):
            tlist.append([x, y])

    x, y = tlist, ansd

    for i in x[:]:
      if i in y:
          x.remove(i)
          y.remove(i)

    unansd = tlist

    # code = ' you have not answered the following <br> '

    tp = []
    un_sec = {} #unanswered sections
    for i in unansd:
        tp.append(int(i[0]))

    tp = list(set(tp))

    ##### finding lengths of tp
    data = get_data()
    leng = {}
    for i in tp:
        n = len(data[str(i)])
        leng[str(i)] = n
    #####

    for i in tp:
        # i is the section number
        un_sec[str(i)] = []
        for j in unansd:
            if j[0] == str(i):
                un_sec[str(i)].append(j[1])

    uns_p = {}
    for i in tp:
        un_p = len(un_sec[str(i)]) / float(leng[str(i)])
        un_p = int(un_p * 100)
        uns_p[str(i)] = un_p

    print(uns_p)

    ##### Generarting code #####

    code = '<br><br><br>'

    for i in tp:
        code = code + 'you have not answered ' + str(uns_p[str(i)]) + '% of section ' + str(str(i)) + '. Revisit? <input type="submit" name="action" value="'+str(str(i))+'"> <br>'
    code = code + '<br><br>'

    return render(request, 'home/results.html', {'V':int(res[0]), 'A':int(res[1]), 'K':int(res[2]), 'code':mark_safe(code)})

# Create your views here.
def quiz(request):

    if request.method == 'POST':
        results = list(request.POST.keys())
        results = results[1:]
        n_s = len(results)
        request.session['results'] = results
        request.session['s'] = 0
        q_data = get_data()
        n = len(q_data)
        request.session['c'] = 1
        progress = 0
        scene = get_scene()[(results[0])]

        return render(request, 'home/scenario.html', {'scene':scene, 's':int(1)})
    else:
        progress = 0
        request.session['c'] = 0
        code = choose_category()

    return render(request, 'home/quiz.html', {'content': mark_safe(code), 'progress':progress, 'q':'PLS bot'})

def quiz2(request):
    try:
        if request.POST['action']:
            if request.POST['action'] == 'jump':
                code =  ''
                request.session['s'] += 1
                request.session['c'] = 1

                if (s+1) == n_s:
                    return render(request, 'home/dummy.html')

                s = request.session['s']
                scene = get_scene()[(results[s])]
                return render(request, 'home/scenario.html', {'scene':scene, 's':int(s+1)})

            elif request.POST['action'] == 'exit':
                return render(request, 'home/dummy.html')
    except:
        a = 0

    s = int(request.session['s'])
    c = request.session['c']
    responses = list(request.session['responses'])
    results = list(request.session['results'])

    try:

        answers = list(request.POST.values())
        answers = answers[1:]

        if len(answers) != 1:
            answers = [int(float(i)) for i in answers]
            if answers[0] == answers[1] == answers[2] == 33:
                unans = list(request.session['unanswered'])
                li = [s, int(int(c)-1)]
                unans.append(li)
                request.session['unanswered'] = unans
            else:
                ansd = list(request.session['ansd'])
                li = [str(results[s]), int(int(c)-1)]####################!
                ansd.append(li)
                request.session['ansd'] = ansd

                ansd2 = list(request.session['ansd2'])
                li = [str(results[s]), int(int(c)-1)]####################!
                ansd2.append(li)
                request.session['ansd2'] = ansd2

        responses.append(answers)
        request.session['responses'] = responses
    except:
        v=0
    n_s = len(results)

    if s == n_s:
        return render(request, 'home/dummy.html')
    data = get_data()
    q_data = data[(results[s])]

    ansd2 = list(request.session['ansd2'])
    print(ansd2)

    n = len(q_data)
    n_a = len(ansd2)
    n_u = c - n_a - 1
    pa = n_a * 100 / n
    pu = n_u * 100 / n
     ### c questions are done
    ### make a code for c 'th question
    progress = int((c-1)/(n)*100)
    progress2 = int((s)*100/n_s)

    if n < c:
        code =  ''
        request.session['s'] += 1
        request.session['c'] = 1
        request.session['ansd2'] = list('')

        if (s+1) == n_s:
            return render(request, 'home/dummy.html')

        s = request.session['s']
        scene = get_scene()[(results[s])]
        return render(request, 'home/scenario.html', {'scene':scene, 's':int(s+1)})
    else:
        code = '''
                    <div class="">
                    <div class=""><div class="">
                    <p>
                    <br>''' + q_data[str(int(c))]['q'] + '''
                    <br><br>
                    1. ''' + q_data[str(int(c))]['V'] + '''<br>

                    <div class="slider one slide-option">
                      <div class="slide">
                        <div class="control">
                          <div class="switch">
                              <input type="number" class="value_in hidden" value="0" name="charity_one" min="0" max="100">
                          </div>
                          </div>
                      </div>
                      <br>

                    2. ''' + q_data[str(int(c))]['A'] + '''<br>

                    <div class="slider two">
                      <div class="slide">
                         <div class="control">
                           <div class="switch">
                              <input type="number" class="value_in hidden" value="0" name="charity_two" min="0" max="100">
                          </div>
                          </div>
                      </div>
                      <br>

                    3. ''' + q_data[str(int(c))]['K'] + '''<br>

                    <div class="slider four">
                    <div class="slide">
                        <div class="control">
                        <div class="switch">
                            <input type="number" class="value_in hidden" value="0" name="charity_four" min="0" max="100">
                        </div>
                    </div>
                    </div></div>
                    <br>


                    <input type="submit" value="Submit">
                    </div>


                    <br>
                    </p>
                    </div></div></div>
                    '''

        if float(c/n) > 0.5:
            exit = ''' <br><br><br><br><br><br><br><br><br><br><br><br>
              <input type="submit" name="action" value="jump">
              <input type="submit" name="action" value="exit"> '''
        else:
            exit = ''

        request.session['c'] = int(request.session['c']) + 1

        return render(request, 'home/quiz2.html', {'content': mark_safe(code), 'progress':progress, 'progress2':progress2, 'q':int(c), 'exit': mark_safe(exit), 'pa':pa, 'pu':pu})
    return HttpResponse('404!')

def feedback(request):
    return render(request, 'home/feedback.html')

def moderator(request):
    return HttpResponse('feedback and new questions here')

def reattempt(request):
    s = request.session['s2']
    data = get_data()
    sdata = data[str(s)]

    n = len(sdata)

    c = request.session['c2']


    ##### Jumps and Exits

    try:
        if request.POST['action']:
            if request.POST['action'] == 'jump':
                code =  ''
                request.session['s'] += 1
                request.session['c'] = 1

                if (s+1) == n_s:
                    return render(request, 'home/dummy.html')

                s = request.session['s']
                scene = get_scene()[(results[s])]
                return render(request, 'home/scenario.html', {'scene':scene, 's':int(s+1)})

            elif request.POST['action'] == 'exit':
                return render(request, 'home/dummy.html')
    except:
        a = 0

    #####
    # --------------------- #
    ##### Processing results

    try:
        responses = list(request.session['responses'])
        answers = list(request.POST.values())
        answers = answers[1:]

        if len(answers) != 1:
            answers = [int(float(i)) for i in answers]
            if answers[0] == answers[1] == answers[2] == 33:
                unans = list(request.session['unanswered'])
                li = [s, int(int(c)-1)]
                unans.append(li)
                request.session['unanswered'] = unans
            else:
                ansd = list(request.session['ansd'])
                li = [str(s), int(int(c)-1)]
                ansd.append(li)
                request.session['ansd'] = ansd

        responses.append(answers)
        request.session['responses'] = responses
        print(ansd)

    except:
        a = 0

    #####


    if n < c:
        return render(request, 'home/dummy.html')
    else:
        qdata = sdata[str(c)]
        progress = int((c-1)/(n)*100)

        q, V, A, K = qdata['q'], qdata['V'], qdata['A'], qdata['K']

        code = '''
                <div class="">
                <div class=""><div class="">
                <p>
                <br>''' + q + '''
                <br><br>
                1. ''' + V + '''<br>

                <div class="slider one slide-option">
                  <div class="slide">
                    <div class="control">
                      <div class="switch">
                          <input type="number" class="value_in hidden" value="0" name="charity_one" min="0" max="100">
                      </div>
                      </div>
                  </div>
                  <br>

                2. ''' + A + '''<br>

                <div class="slider two">
                  <div class="slide">
                     <div class="control">
                       <div class="switch">
                          <input type="number" class="value_in hidden" value="0" name="charity_two" min="0" max="100">
                      </div>
                      </div>
                  </div>
                  <br>

                3. ''' + K + '''<br>

                <div class="slider four">
                <div class="slide">
                    <div class="control">
                    <div class="switch">
                        <input type="number" class="value_in hidden" value="0" name="charity_four" min="0" max="100">
                    </div>
                </div>
                </div></div>
                <br>


                <input type="submit" value="Submit">
                </div>


                <br>
                </p>
                </div></div></div>
                '''

        if float(c/n) > 0.5:
            exit = ''' <br><br><br><br><br><br><br><br><br><br><br><br>
              <input type="submit" name="action" value="jump">
              <input type="submit" name="action" value="exit"> '''
        else:
            exit = ''

        request.session['c2'] = int(request.session['c2']) + 1

    return render(request, 'home/reattempt.html', {'content': mark_safe(code), 'progress':progress, 'q':int(c), 'exit': mark_safe(exit)})

def comeback(request, pk):

    ### Get session details
    CLOUDANT_USERNAME="apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt"
    CLOUDANT_PASSWORD="f70c9a73c52d287d3271ddc3dba6a30a"

    authenticator = IAMAuthenticator("C8J8TcTL_T9YlMtyA6itWueAqAdkgGXbwOc8RA2omfCd")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt:f70c9a73c52d287d3271ddc3dba6a30a@dc1a5ff5-996b-475c-8b7e-da87f4bf33a3-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.get_server_information().get_result()

    response = service.get_document(
      db='usessions',
      doc_id=str(pk)
    ).get_result()

    ### Create new sessions
    request.session['s'] = response['s']
    request.session['c'] = response['c']
    request.session['responses'] = response['responses']
    request.session['results'] = response['results']
    request.session['ansd'] = response['ansd']
    request.session['ansd2'] = response['ansd2']
    request.session['unanswered'] = response['unans']

    return redirect('home:quiz2')
    #return render(request, 'home/comeback.html', {'pc':[pk, response]})

def view_feedback(request):
    response = service.get_document(db='usessions', document=sessions_doc).get_result()
    return render(request, 'home/view_feedback')

def revisit(request):
    letters = string.ascii_letters
    passcode = str( ''.join(random.choice(letters) for i in range(10)) )

    # data upload
    CLOUDANT_USERNAME="apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt"
    CLOUDANT_PASSWORD="f70c9a73c52d287d3271ddc3dba6a30a"

    authenticator = IAMAuthenticator("C8J8TcTL_T9YlMtyA6itWueAqAdkgGXbwOc8RA2omfCd")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-1mfs4kqo2nmnc2sdtgp9ji8myznbgm6mivk0o93pfopt:f70c9a73c52d287d3271ddc3dba6a30a@dc1a5ff5-996b-475c-8b7e-da87f4bf33a3-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.get_server_information().get_result()

    products_doc = Document(
      id="001",
      data = get_data()
      )

    sessions_doc = Document(
      id = passcode,
      s = request.session['s'],
      c = request.session['c'],
      responses = request.session['responses'],
      results = request.session['results'],
      ansd = request.session['ansd'],
      ansd2 = request.session['ansd2'],
      unans = request.session['unanswered']
      )

    response = service.post_document(db='usessions', document=sessions_doc).get_result()
    print(response)

    link = 'http://127.0.0.1:8000/comeback/' + passcode

    return render(request, 'home/revisit.html', {'link':link})

def preresults(request):
    if request.method == 'POST':
        s = request.POST['act']
        data = get_data()
        data = data[str(s)]
        request.session['c2'] = 1
        request.session['s2'] = s
        return render(request, 'home/dummy2.html')
    else:
        responses = list(request.session['responses'])
        responses = [i for i in responses if i != ['']]
        responses = [i for i in responses if i != ['jump']]
        responses = [i for i in responses if i != ['exit']]

        res = [sum(i)/len(responses) for i in zip(*responses)]

        ansd = list(request.session['ansd'])
        ansd = [i for i in ansd if i != ['']]
        ansd = [i for i in ansd if i != ['jump']]
        ansd = [i for i in ansd if i != ['exit']]
        print(ansd)

        tlist = []
        data = get_data()

        results = request.session['results']
        n_s = len(results) # no of scenarios selected

        for x in results:
            q_data = data[x]
            n = len(q_data)
            for y in range(1, n+1):
                tlist.append([x, y])

        x, y = tlist, ansd

        for i in x[:]:
          if i in y:
              x.remove(i)
              y.remove(i)

        unansd = tlist

        print(unansd)

        tp = []
        un_sec = {} #unanswered sections
        for i in unansd:
            tp.append(int(i[0]))

        tp = list(set(tp))

        ##### finding lengths of tp
        data = get_data()
        leng = {}
        for i in tp:
            n = len(data[str(i)])
            leng[str(i)] = n
        #####

        for i in tp:
            # i is the section number
            un_sec[str(i)] = []
            for j in unansd:
                if j[0] == str(i):
                    un_sec[str(i)].append(j[1])

        uns_p = {}
        for i in tp:
            un_p = len(un_sec[str(i)]) / float(leng[str(i)])
            un_p = int(un_p * 100)
            uns_p[str(i)] = un_p

        print(uns_p)

        ##### Generarting code #####

        code = '<br><br><br>'

        for i in tp:
            code = code + 'you have not answered ' + str(uns_p[str(i)]) + '% of section ' + str(str(i)) + '. Revisit? <input type="submit" name="act" value="'+str(str(i))+'"> <br>'
        code = code + '<br><br><br><br><br><br><br>'

        cont = ''' Or continue? <input type="submit" name="continue" value="continue"> '''

        return render(request, 'home/preresults.html', {'V':int(res[0]), 'A':int(res[1]), 'K':int(res[2]), 'code':mark_safe(code), 'continue':mark_safe(cont)})

    return render(request, 'home/preresults.html')
