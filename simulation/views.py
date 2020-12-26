from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import json
from django.http import JsonResponse
from .models import User, Simulation, Game, Complete
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    # show a welcome message and link to guide
    return render(request, "simulation/home.html")

def guide(request):
    # describe all functions and how to play / scoring and other info
    return render(request, "simulation/guide.html")

def create(request):
    if request.method == "POST":
        # filled out form - get all inputs
        title = request.POST["title"]
        desc = request.POST["description"]
        difficulty = request.POST["difficulty"]
        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        race = request.POST["race"]
        birth = request.POST["birth"]
        weight = request.POST["weight"]
        height = request.POST["height"]
        SA = request.POST["sexuallyActive"]
        med = request.POST["medications"]
        allergies = request.POST["allergies"]
        ill = request.POST["illnesses"]
        symp = request.POST["symptoms"]
        notes = request.POST["notes"]
        image = request.POST["url"]
        diag = request.POST["diagnosis"]
        test1 = request.POST["test1"]
        desc1 = request.POST["descTest1"]
        test1Res = request.POST["test1Result"]
        test2 = request.POST["test2"]
        desc2 = request.POST["descTest2"]
        test2Res = request.POST["test1Result"]
        test3 = request.POST["test3"]
        desc3 = request.POST["descTest3"]
        test3Res = request.POST["test1Result"]
        test4 = request.POST["test4"]
        desc4 = request.POST["descTest4"]
        test4Res = request.POST["test1Result"]
        test5 = request.POST["test5"]
        desc5 = request.POST["descTest5"]
        test5Res = request.POST["test1Result"]
        test6 = request.POST["test6"]
        desc6 = request.POST["descTest6"]
        test6Res = request.POST["test1Result"]
        tNum = request.POST["testNum"]
        quest1 = request.POST["question1"]
        resp1 = request.POST["response1"]
        quest2 = request.POST["question2"]
        resp2 = request.POST["response2"]
        quest3 = request.POST["question3"]
        resp3 = request.POST["response3"]
        quest4 = request.POST["question4"]
        resp4 = request.POST["response4"]
        quest5 = request.POST["question5"]
        resp5 = request.POST["response5"]
        quest6 = request.POST["question6"]
        resp6 = request.POST["response6"]
        qNum = request.POST["questionNum"]
        hint1 = request.POST["hint1"]
        hint2 = request.POST["hint2"]
        hint3 = request.POST["hint3"]
        hint4 = request.POST["hint4"]
        # test Results
        if test1Res == "No Select":
            test1Res = ""
        if test2Res == "No Select":
            test2Res = ""
        if test3Res == "No Select":
            test3Res = ""
        if test4Res == "No Select":
            test4Res = ""
        if test5Res == "No Select":
            test5Res = ""
        if test6Res == "No Select":
            test6Res = ""
        # check to make sure required fields are not empty
        required = [title,difficulty,desc,name,age,gender,race,birth,weight,height,SA,symp,diag]
        # optional = [med,allergies,ill,notes,image,test1,desc1,test1Res,test2,desc2,test2Res,test3,desc3,test3Res,test4,desc4,
        #     test4Res,test5,desc5,test5Res,test6,desc6,test6Res,tNum,quest1,resp1,quest2,resp2,quest3,resp3,quest4,resp4,quest5,resp5,quest6,resp6,
        #     qNum,hint1,hint2,hint3,hint4]
        for val in required:
            if val == "":
                # error
                return render(request, "simulation/create.html", {
                    # MAKE MESSAGE RED
                    "message": "Must fill in all forms"
                })
        # save information
        s = Simulation(user=request.user.username, title=title, desc=desc, difficulty=difficulty, name=name, 
            age=age, gender=gender, race=race, birth=birth, weight=weight, height=height, sexuallyActive=SA, medications=med, 
            allergies=allergies, illnesses=ill, symptoms=symp, notes=notes, url=image, diagnosis=diag, test1=test1, 
            desc1=desc1, test1Res=test1Res, test2=test2, desc2=desc2, test2Res=test2Res, test3=test3, desc3=desc3, 
            test3Res=test3Res, test4=test4, desc4=desc4, test4Res=test4Res, test5=test5, desc5=desc5, test5Res=test5Res, 
            test6=test6, desc6=desc6, test6Res=test6Res, tNum=tNum, quest1=quest1, resp1=resp1, quest2=quest2, resp2=resp2, 
            quest3=quest3, resp3=resp3, quest4=quest4, resp4=resp4, quest5=quest5, resp5=resp5, quest6=quest6, resp6=resp6, 
            qNum=qNum, hint1=hint1, hint2=hint2, hint3=hint3, hint4=hint4)
        s.save()
        return render(request, "simulation/create.html")
    else:
        return render(request, "simulation/create.html")

def play(request, sim_id):
    # find the simulation
    s = Simulation.objects.get(pk=sim_id)
    #check if there a game with this user and this id exists
    gameCheck = Game.objects.filter(user=request.user.username, simID=sim_id)
    if gameCheck:
        # load game
        g = Game.objects.get(user=request.user.username, simID=sim_id)
    else:
        # create new game
        gSave = Game(user=request.user.username, simID=sim_id)
        gSave.save()
        g = Game.objects.get(user=request.user.username, simID=sim_id)
    # figure out if used the test already
    tList = []
    t = g.tests
    # if not empty create a list
    if t != "" and t != None:
        tList = t.split("#")
    # figure out how many free tests you have left
    tLeft = s.tNum - len(tList)
    if tLeft <0:
        tLeft = 0
    # if doesn't exist set to -1
    t1 = -1
    t2 = -1
    t3 = -1
    t4 = -1
    t5 = -1
    t6 = -1
    # if not used set to 0
    if s.test1 != "" and s.test1 != None:
        t1 = 0
    if s.test2 != "" and s.test2 != None:
        t2 = 0
    if s.test3 != "" and s.test3 != None:
        t3 = 0
    if s.test4 != "" and s.test4 != None:
        t4 = 0
    if s.test5 != "" and s.test5 != None:
        t5 = 0
    if s.test6 != "" and s.test6 != None:
        t6 = 0
    # if the test is in the list then set to true
    if "t1" in tList:
        t1 = 1
    elif "t2" in tList:
        t2 = 1
    elif "t3" in tList:
        t3 = 1
    elif "t4" in tList:
        t4 = 1
    elif "t5" in tList:
        t5 = 1
    elif "t6" in tList:
        t6 = 1
    # same thing for questions
    # figure out if asked the questions already
    qList = []
    q = g.questions
    # if not empty create a list
    if q != "" and q != None:
        qList = q.split("#")
    # figure out how many free questions left
    qLeft = s.qNum - len(qList)
    if qLeft <0:
        qLeft = 0
    # define values already
    q1 = -1
    q2 = -1
    q3 = -1
    q4 = -1
    q5 = -1
    q6 = -1
    # if not used set to 0
    if s.quest1 != "" and s.quest1 != None:
        q1 = 0
    if s.quest2 != "" and s.quest2 != None:
        q2 = 0
    if s.quest3 != "" and s.quest3 != None:
        q3 = 0
    if s.quest4 != "" and s.quest4 != None:
        q4 = 0
    if s.quest5 != "" and s.quest5 != None:
        q5 = 0
    if s.quest6 != "" and s.quest6 != None:
        q6 = 0
    # if the test is in the list then set to true
    if "q1" in qList:
        q1 = 1
    elif "q2" in qList:
        q2 = 1
    elif "q3" in qList:
        q3 = 1
    elif "q4" in qList:
        q4 = 1
    elif "q5" in qList:
        q5 = 1
    elif "q6" in qList:
        q6 = 1
    # same thing but for hints
    # figure out if used the hint already
    hList = []
    h = g.hints
    # if not empty create a list
    if h != "" and h != None:
        hList = h.split("#")
    # define values already
    h1 = -1
    h2 = -1
    h3 = -1
    h4 = -1
    # if not used set to 0
    if s.hint1 != "" and s.hint1 != None:
        h1 = 0
    if s.hint2 != "" and s.hint2 != None:
        h2 = 0
    if s.hint3 != "" and s.hint3 != None:
        h3 = 0
    if s.hint4 != "" and s.hint4 != None:
        h4 = 0
    # if the test is in the list then set to true
    if "h1" in hList:
        h1 = 1
    elif "h2" in hList:
        h2 = 1
    elif "h3" in hList:
        h3 = 1
    elif "h4" in hList:
        h4 = 1
    return render(request, "simulation/game.html", {
        "simulation": s,
        "game": g,
        "t1": t1,
        "t2": t2,
        "t3": t3,
        "t4": t4,
        "t5": t5,
        "t6": t6,
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": q4,
        "q5": q5,
        "q6": q6,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "tLeft": tLeft,
        "qLeft": qLeft
    })

@csrf_exempt
def save(request):
    if request.method == "PUT":
        #load data
        data = json.loads(request.body)
        #get all variables passsed through
        if data.get("tests") is not None:
            tests = data["tests"]
        if data.get("questions") is not None:
            questions = data["questions"]
        if data.get("hints") is not None:
            hints = data["hints"]
        if data.get("id") is not None:
            simID= data["id"]
        # get game object
        g = Game.objects.get(user=request.user.username,simID=simID)
        # get previous tests, questions, and hints
        t = g.tests
        q = g.questions
        h = g.hints
        # update tests, questions, and hints
        for test in tests:
            if t == None:
                t = test
            else:
                t = t + "#" + test
        for question in questions:
            if q == None:
                q = question
            else:
                q = q + "#" + question
        for hint in hints:
            if h == None:
                h = hint
            else:
                h = h + "#" + hint
        # set and save all
        g.tests = t
        g.questions = q
        g.hints = h
        g.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)

@csrf_exempt
def submit(request):
    # get js returned command
    if request.method == "PUT":
        #load data
        data = json.loads(request.body)
        #get all variables passsed through
        if data.get("tests") is not None:
            tests= data["tests"]
        if data.get("questions") is not None:
            questions= data["questions"]
        if data.get("hints") is not None:
            hints= data["hints"]
        if data.get("diag") is not None:
            diagnosis= data["diag"]
        if data.get("id") is not None:
            simID= data["id"]
        # get game object
        g = Game.objects.get(user=request.user.username,simID=simID)
        # get previous tests, questions, and hints
        t = g.tests
        q = g.questions
        h = g.hints
        # update t, q, and h
        for test in tests:
            if t == None:
                t = test
            else:
                t = t + "#" + test
        for question in questions:
            if q == None:
                q = question
            else:
                q = q + "#" + question
        for hint in hints:
            if h == None:
                h = hint
            else:
                h = h + "#" + hint
        # set tests, questions, and hints
        g.tests = t
        g.questions = q
        g.hints = h
        # *score is pending*
        # set diagnosis
        g.diagnosis = diagnosis
        # set isDiagnosed to True
        g.isDiagnosed = True
        # save everything
        g.save()
        return HttpResponse(status=204)

def affirmed(request, simID, a):
    # get game object
    g = Game.objects.get(user=request.user.username,simID=simID)
    s = Simulation.objects.get(pk=simID)
    # calculate and save score
        # Q = -10
        # T = -15
        # H = -20
        # Postivie T = +10
        # Correct D = +40
    score = 50
    if a == "y":
        # diagnosis was correct
        score += 40
        g.isStarred = True
    # check number of costly tests
    tests = g.tests
    if tests:
        tests = tests.split("#")
        plus = (len(tests)-s.tNum)
        if plus < 0:
            plus = 0
        score += plus * -15
        # get positive test results
        pos = 0
        if "t1" in tests:
            if s.test1Res == "Postive":
                pos += 1
        elif "t2" in tests:
            if s.test2Res == "Postive":
                pos += 1
        elif "t3" in tests:
            if s.test3Res == "Postive":
                pos += 1
        elif "t4" in tests:
            if s.test4Res == "Postive":
                pos += 1
        elif "t5" in tests:
            if s.test5Res == "Postive":
                pos += 1
        elif "t6" in tests:
            if s.test6Res == "Postive":
                pos += 1
        score += pos * 10
    # check number of costly questions
    questions = g.questions
    if questions:
        questions = questions.split("#")
        plusQ = (len(questions)-s.qNum)
        if plusQ < 0:
            plusQ = 0
        score += plusQ * -10
    # subtract hints
    hints = g.hints
    if hints:
        hints = hints.split("#")
        plusH = len(hints)
        score += plusH * -20
    # min score is 0
    if score < 0:
        score = 0
    if score > 100:
        score = 100
    g.score = score
    # change it to isFinished
    g.isFinished = True
    # save everything
    g.save()
    s = Simulation.objects.get(pk=simID)
    complete = Complete(title=s.title, desc=s.desc, simID=simID, score=score, correctDiag=g.isStarred)
    complete.save()
    return HttpResponseRedirect(reverse("completed"))

def reset(request, sim_id):
    # delete game object with that id
    g = Game.objects.get(user=request.user.username,simID=sim_id)
    g.delete()
    # then redirect to play
    return HttpResponseRedirect(reverse("play", args=(sim_id,)))
    # return HttpResponseRedirect(reverse('create_rating', args=(video_id,)))

def completed(request):
    # get all games with my username where isFinished == True
    g = Game.objects.filter(user=request.user.username,isFinished=True)
    # get all ids
    ids = []
    for game in g:
        ids.append(game.pk)
    s = []
    # for each id create a list with to be displayed info
    for ID in ids:
        title = Simulation.objects.get(pk=ID).title
        desc = Simulation.objects.get(pk=ID).desc
        score = Game.objects.get(user=request.user.username,simID=ID).score
        isCorrect = Game.objects.get(user=request.user.username,simID=ID).isStarred
        if isCorrect:
            D = "correct"
        else:
            D = "wrong"
        l = [title, desc, score, D, ID]
        s.append(l)

    # get all objects from Complete
    c = Complete.objects.all()
    return render(request, "simulation/simulation.html", {
        "simulations": c,
        "type": "completed"
    })

def mySim(request):
    # get all simulations with my username
    s = Simulation.objects.filter(user=request.user.username)
    # use sim that are yours (above)
    # extract all ids
    ids = []
    for sim in s:
        ids.append(sim.pk)
    # get all game objects with those ids and where isDiagnosed == True and isFinished == False
    g = Game.objects.filter(simID__in=ids, isDiagnosed=True, isFinished=False)
    # get ids of those games
    newID = []
    for game in g:
        newID.append(game.simID)
    # for each id get title, your diag, and their diag
    check = []
    for ID in newID:
        title = Simulation.objects.get(pk=ID).title
        yd = Simulation.objects.get(pk=ID).diagnosis
        td = Game.objects.get(simID=ID).diagnosis
        l = [title,yd,td,ID]
        check.append(l)
    # cs is all simulations that have already completed
    g1 = Game.objects.filter(user=request.user.username, simID__in=ids, isDiagnosed=True)
    ids1 = []
    for game in g1:
        ids1.append(game.simID)
    cs = Simulation.objects.filter(pk__in=ids1)
    # s is all simulations that are not finished or not started
    ids2 = []
    for ID in ids:
        if ID not in ids1:
            ids2.append(ID)
    s = Simulation.objects.filter(pk__in=ids2)
    return render(request, "simulation/simulation.html", {
        "simulations": s,
        "check": check,
        "cSims": cs,
        "type": "mySim"
    })

def current(request):
    # get all games where isFinished == False
    g = Game.objects.filter(user=request.user.username, isFinished=False, isDiagnosed=False)
    ids = []
    for game in g:
        ids.append(game.pk)
    s = Simulation.objects.filter(pk__in=ids)
    return render(request, "simulation/simulation.html", {
        "simulations": s,
        "type": "current"
    })

def browse(request):
    if request.method == "POST":
        # array of all neglected search words
        words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it",
            "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
            "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have",
            "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
            "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
            "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
            "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
            "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
            "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will",
            "just", "don", "should", "now"]
        search = request.POST["search"].lower()
        search = search.split()
        searchTitle = []
        for w in search:
            if w not in words:
                searchTitle.append(w)
        # get all simulations
        s = Simulation.objects.all()
        ids = []
        for sim in s:
            ids.append(sim.pk)
        # cs is all simulations that have already completed
        g1 = Game.objects.filter(user=request.user.username, simID__in=ids, isDiagnosed=True)
        ids1 = []
        for game in g1:
            ids1.append(game.simID)
        cs = Simulation.objects.filter(pk__in=ids1)
        # s is all simulations that are not finished
        ids2 = []
        for ID in ids:
            if ID not in ids1:
                ids2.append(ID)
        s = Simulation.objects.filter(pk__in=ids2)
        # if searched something
        if searchTitle:
            # loop through ids1 for title
            ids1R = []
            for ID in ids1:
                title = Simulation.objects.get(pk=ID).title.lower()
                for w in searchTitle:
                    if w in title:
                        ids1R.append(ID)
                    break
            ids2R = []
            for ID in ids2:
                title = Simulation.objects.get(pk=ID).title.lower()
                for w in searchTitle:
                    if w in title:
                        ids2R.append(ID)
                    break
            cs = Simulation.objects.filter(pk__in=ids1R)
            s = Simulation.objects.filter(pk__in=ids2R)
        return render(request, "simulation/simulation.html", {
            "simulations": s,
            "cSims": cs,
            "type": "browse"
        })
    else:
        # get all simulations
        s = Simulation.objects.all()
        ids = []
        for sim in s:
            ids.append(sim.pk)
        # cs is all simulations that have already completed
        g1 = Game.objects.filter(user=request.user.username, simID__in=ids, isDiagnosed=True)
        ids1 = []
        for game in g1:
            ids1.append(game.simID)
        cs = Simulation.objects.filter(pk__in=ids1)
        # s is all simulations that are not finished
        ids2 = []
        for ID in ids:
            if ID not in ids1:
                ids2.append(ID)
        s = Simulation.objects.filter(pk__in=ids2)
        return render(request, "simulation/simulation.html", {
            "simulations": s,
            "cSims": cs,
            "type": "browse"
        })

def login_view(request):
   if request.method == "POST":
 
       # Attempt to sign user in
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
 
       # Check if authentication successful
       if user is not None:
           login(request, user)
           return HttpResponseRedirect(reverse("index"))
       else:
           return render(request, "simulation/login.html", {
               "message": "Invalid username and/or password."
           })
   else:
       return render(request, "simulation/login.html")
 
 
def logout_view(request):
   logout(request)
   return HttpResponseRedirect(reverse("login"))
 
 
def register(request):
   if request.method == "POST":
       username = request.POST["username"]
       email = request.POST["email"]
 
       # Ensure password matches confirmation
       password = request.POST["password"]
       confirmation = request.POST["confirmation"]
       if password != confirmation:
           return render(request, "simulation/register.html", {
               "message": "Passwords must match."
           })
 
       # Attempt to create new user
       try:
           user = User.objects.create_user(username, email, password)
           user.save()
       except IntegrityError:
           return render(request, "simulation/register.html", {
               "message": "Username already taken."
           })
       login(request, user)
       return HttpResponseRedirect(reverse("index"))
   else:
       return render(request, "simulation/register.html")
