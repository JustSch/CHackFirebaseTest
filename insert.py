class Insert(object):
    
 
    def insert(self,db):
        print(db)
        doc_ref = db.collection(u'users').document(u'alovelace')
        doc_ref.set({
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815
        })
