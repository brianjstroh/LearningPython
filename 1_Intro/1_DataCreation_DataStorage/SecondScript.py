#initialize data to be stored in files, pickles, or shelves

#records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom',       'age': 50, 'pay': 0, 'job': None}

#database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

#This part is run only when this notebook is run as a top-level script, not when it is imported
if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])