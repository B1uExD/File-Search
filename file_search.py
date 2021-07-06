import os
import pickle

class SearchEngine:
    def __init__(self):
        self.file_index = [] # list & it will store directory index returned by os.walk()
        self.results = [] #list it will store the result of each search
        self.matches = 0 #counter to count each matching files
        self.records = 0 #counter to count each record searched

    def create_new_index(self, path_root):
        #create new index which starts with root path and save it to a file
        self.file_index = [(root, files) for root, dirs, files in os.walk(path_root) if files]  #note: "if files" filters out the empty file list

        #save to file
        with open('file_index.pkl', 'wb') as save_file:
            pickle.dump(self.file_index, save_file)

    def load_existing_index(self):
        #load existing data
        try:
            with open('file_index.pkl', 'rb') as load_file:
                self.file_index = pickle.load(load_file)
        except:
            self.file_index = []

    def search(self, term, search_type = 'contains'):
        #term - it is what we are searching
        #search_by contains/starts with/ends with
        #seacrh is always based on search_by and by default its search_by is contains
        #reset variables
        self.results.clear()
        self.records = 0
        self.matches = 0

        #perform search
        for path, files in self.file_index:
            for file in files:
                self.records+=1
                if(search_type == 'contains' and term.lower() in file.lower() or
                search_type == 'startswith' and file.lower().startswith(file.lower()) or
                search_type == 'endswith' and file.lower().endswith(file.lower() )):
                    result=path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches+=1
                else:
                    continue

        #save to file
        with open('search_result.txt', 'w') as save_res:
            for row in self.results:
                save_res.write(row + '\n')

    def gui_create_new_index(self, values):
        path_root = values['PATH']
        #create new index which starts with root path and save it to a file
        self.file_index = [(root, files) for root, dirs, files in os.walk(path_root) if files]

    def gui_search(self, values):
        #term - it is what er are searching
        term = values['TERM']
        #search_by contains/starts with/ends with
        #seacrh is always based on search_by and by default its search_by is contains
        #reset variables
        self.results.clear()
        self.records = 0
        self.matches = 0

        #perform search
        for path, files in self.file_index:
            for file in files:
                self.records+=1
                if(values['CONTAINS'] and term.lower() in file.lower() or
                values['STARTSWITH'] and file.lower().startswith(file.lower()) or
                values['ENDSWITH'] and file.lower().endswith(file.lower() )):
                    result=path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches+=1
                else:
                    continue

        #save to file
        with open('search_result.txt', 'w') as save_res:
            for row in self.results:
                save_res.write(row + '\n')

def test1():
    s = SearchEngine()
    s.load_existing_index()
    s.create_new_index('F:/')
    s.search('loki')

    print()
    print(f'>>>  {s.matches} matches found out of {s.records} ')
    print()
    print('>>> File Path of the matched records:')
    for match in s.results:
        print(match.replace('/', '\\'))

#test1()

