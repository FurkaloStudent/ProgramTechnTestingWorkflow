def add_item(collection, item_id, name, description, value, date):
    collection[item_id] = {
        'name': name,
        'description': description,
        'value': value,
        'date': date,
    }

def get_item(collection, item_id):
    l = collection.get(item_id) 
    if l:
      return l
    else:
        raise ValueError

def update_item(collection, item_id, name=None, description=None, value=None, date=None):
    item = collection.get(item_id)
    if item:
        if name is not None:
            item['name'] = name
        if description is not None:
            item['description'] = description
        if value is not None:
            item['value'] = value
        if date is not None:
            item['date'] = date

def delete_item(collection, item_id):
    if item_id in collection:
        del collection[item_id]