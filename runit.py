import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)

db = firestore.client()


# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

doc_ref = db.collection(u'trivia'.document(u'Fact1'))
doc_ref.set({
    u'question_name': u'Do You Want To Build A Snowman?',
    u'answer1': u'It Doesn\'t have to be a snowman',
    u'answer2': u'It Doesn\'t have to be a snowman',
    u'answer3': u'It Doesn\'t have to be a snowman',
    u'answer4': u'It Doesn\'t have to be a snowman'
})

doc_ref = db.collection(u'profiles'.document(u'profile1'))
doc_ref.set({
    u'name': u'Amelia Bedeelia',
    u'e-mail': u'fake@fake.com',
    u'coordinator_status': u'y',
    u'points': u'0',
    u'uuid': u'8777777',
    u'account_created': u'04-02-2019:12:12:12'
})

doc_ref = db.collection(u'events'.document(u'cleanup'))
doc_ref.set({
    u'event_name': u'Central Park Cleanup',
    u'event_location': u'insert coordinates of central park here',
    u'description': u'Help Clean NYC\'s Largest Park',
    u'event_time': u'Saturday Oct 22,2017 3:30PM',
    u'coordinator': u'Marcy Jenkins',
    u'points_awarded': u'0',
    u'event_id': u'77'
})

#prints everything in db
# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#         print(u'{} => {}'.format(doc.id, doc.to_dict()))
