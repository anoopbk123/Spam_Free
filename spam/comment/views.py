from django.shortcuts import render
from comment.models import Comment
from user_reg.models import UserReg
from share.models import Share
from spam_message import settings
from reported_comments.models import ReportedComments
import datetime
# import pandas as pd
# import sklearnn
# from pandas import read_excel
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pickle

bull=['IDIOT','STUPID','ASS HOLE','BITCH','amateur','anarchist','show off','stupid monkey face']

# Create your views here.
def comment(request,cid):
    obb=Share.objects.get(share_id=cid)
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    context = {
        'name': objj
    }
    if request.method == "POST":
        obj =Comment()
        obj.friend_id=obb.user_id
        obj.user_id=uid
        obj.share_id=cid
        obj.comment=request.POST.get('comment')
        msg=request.POST.get('comment')
        obj.date=datetime.date.today()
        obj.time=datetime.datetime.now().strftime("%I:%M:%S")
        obj.save()
        # res=cyb_bull(msg)
        WORDS=obj.comment.split(' ')
        res=""
        for w in WORDS:
            if w.upper() in bull:
                res="Bullying"
        # res=""
        # print(res)

        if res == "Bullying":

            orr=ReportedComments()
            orr.user_id=uid
            orr.comment_id=obj.comment_id
            orr.report=obj.comment
            orr.date=datetime.date.today()
            orr.time=datetime.datetime.now().strftime("%I:%M:%S")
            orr.save()

            obbb=Comment.objects.get(comment_id=obj.comment_id).delete()
    return render(request,'comment/comment.html',context)

from django.http import HttpResponse
# def testbull(request):
#
#     res=cyb_bull('hello')
#     return HttpResponse(res)

# def cyb_bull(msg1):
#     msg = msg1
#     filename = "dataset1.xls"
#     # modename = "model_dtc.sav"
#     filepath = settings.BASE_DIR + settings.STATIC_URL + filename
#     # filepath1 = settings.BASE_DIR + settings.STATIC_URL + modename
#     trainData = read_excel(filepath)  # DATA FRAME -> COL, ROWS
#     df2 = {'Label': 'Non-Bullying', 'Tweet': msg}
#     trainData = trainData.append(df2, ignore_index=True)
#     print(trainData.head(3))
#     processed_review = []
#     for i in trainData["Tweet"].values:
#         sentance = html_tag(i)
#         sentance = decontracted(sentance)
#         sentance = re.sub("\S*\d\S*", "", sentance)
#         sentance = re.sub('[^A-Za-z]+', ' ', sentance)
#         sentance = " ".join(i.lower() for i in sentance.split() if i.lower() not in stopwords)
#         processed_review.append(sentance)
#
#     trainData["Cleantext"] = processed_review
#     vectorizer = TfidfVectorizer(min_df=5,
#                                  max_df=0.8,
#                                  sublinear_tf=True,
#                                  use_idf=True)
#     train_vectors = vectorizer.fit_transform(trainData['Cleantext'])
#     X_test1 = train_vectors[train_vectors.shape[0] - 1]
#     from sklearn.tree import DecisionTreeClassifier
#
#     dtc = DecisionTreeClassifier()
#     dd = dtc.fit(train_vectors, trainData['Label'])
#     y_score = dtc.predict(X_test1)
#     # model = pickle.load(open(filepath1, 'rb'))
#     # y_score = model.predict(X_test1)
#     res = "This Message is :" + y_score[0]
#     return res
#
#
# from bs4 import BeautifulSoup
# import re
#
#
# def html_tag(phrase):
#     http_remove = re.sub(r"http\S+", "", phrase)
#     html_remove = BeautifulSoup(http_remove, 'lxml').get_text()
#     return html_remove
#     # remove words with numbers python: https://stackoverflow.com/a/18082370/4084039
#     # remove spacial character: https://stackoverflow.com/a/5843547/4084039
#
#
# def decontracted(phrase):
#     # specific
#     phrase = re.sub(r"won't", "will not", phrase)
#     phrase = re.sub(r"can\'t", "can not", phrase)
#     # general
#     phrase = re.sub(r"n\'t", " not", phrase)
#     phrase = re.sub(r"\'re", " are", phrase)
#     phrase = re.sub(r"\'s", " is", phrase)
#     phrase = re.sub(r"\'d", " would", phrase)
#     phrase = re.sub(r"\'ll", " will", phrase)
#     phrase = re.sub(r"\'t", " not", phrase)
#     phrase = re.sub(r"\'ve", " have", phrase)
#     phrase = re.sub(r"\'m", " am", phrase)
#     return phrase
#
#
# stopwords = set(
#     ['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", \
#      "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
#      'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', \
#      'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
#      'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
#      'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
#      'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', \
#      'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', \
#      'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', \
#      'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
#      's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
#      've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', \
#      "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', \
#      "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
#      'won', "won't", 'wouldn', "wouldn't"])
#
