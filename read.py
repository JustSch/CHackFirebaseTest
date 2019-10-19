class Read(object):
    def read(self,db):
        users_ref = db.collection(u'users')
        docs = users_ref.stream()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))