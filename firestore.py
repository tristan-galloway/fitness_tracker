from os import system, name
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate("C:\\Users\\Direc\\OneDrive - BYU-Idaho\\Documents\\spring_24\\cse310\\fitnessapp2Key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# define our clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def push_event(object, distance, duration):

    # Create the data for the document
    data = {
        'object': object,
        'distance': distance,
        'duration': duration
    }

    # Target the db collection called workouts
    doc_ref = db.collection('workoutsCollection').document()
    # insert the data as a document
    doc_ref.set(data)
    clear()

def get_all_events(collectionName):
    # Get the reference to the collection
    docs = (db.collection(collectionName).stream())
    
    #Iterate over the documents and store their IDs and data in a list
    documents_list = []
    for doc in docs: # type: ignore
        doc_data = doc.to_dict() # Converts the doc_data to a dictionary
        doc_data['id'] = doc.id
        doc_data['docData'] = doc._data
        # print doc._data
        documents_list.append(doc_data)

    clear() # Get ride of the warning
    return documents_list # List of dictionaries

def print_all_events():
    documents_list = get_all_events('workoutsCollection')
        # Iterate through the document data printing it
    for i, doc_data in enumerate(documents_list):
        doc_dict = doc_data['docData']
        print(f"[{i + 1}] {doc_dict['object']}: Duration {doc_dict['duration']} minutes, Distance {doc_dict['distance']}")


def delete_event(collection_name, document_id):
    try:
        doc_ref = db.collection(collection_name).document(document_id)
        doc_ref.delete()
        print(f"Document with ID {document_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting document: {str(e)}")
