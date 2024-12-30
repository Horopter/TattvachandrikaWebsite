from pymongo import MongoClient, ReturnDocument

def get_next_sequence_value(collection_name):
    client = MongoClient('localhost', 27017)
    db = client['tattvachandrika']
    counter = db['counters']
    sequence_document = counter.find_one_and_update(
        {'_id': collection_name},
        {'$inc': {'sequence_value': 1}},
        return_document=ReturnDocument.AFTER,
        upsert=True
    )
    return sequence_document['sequence_value']

def generate_id(prefix, collection_name):
    next_value = get_next_sequence_value(collection_name)
    return f"{prefix}{next_value:06d}"
