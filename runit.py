import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})


#prints everything in db
# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#         print(u'{} => {}'.format(doc.id, doc.to_dict()))
