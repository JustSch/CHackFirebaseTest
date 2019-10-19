class Credential(object):
    import firebase_admin
    import os
    from firebase_admin import credentials
    from firebase_admin import firestore

    def get_service_account(self):
        # Use a service account
        cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        firebase_admin.initialize_app(cred)

        db = firestore.client()
        print(db)
        return db



