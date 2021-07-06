import file_search
import file_gui

def main():
    fg = file_gui.FileSearchGui()
    fse = file_search.SearchEngine()
    fse.load_existing_index()
    while True:
        event, values =fg.window.Read()
        print(event, values)

        if  event is None:
            break

        if event == 'B_INDEX':
            fse.create_new_index(values['PATH'])

            print()
            print('>>> New Index is created')
            print()

        if event == 'B_SEARCH':
            fse.gui_search(values)

            #print results to output
            for results in fse.results:
                print(results)

            print()
            print(f'>>>  {fse.matches} matches found out of {fse.records} ')
            print()
            print('>>> File Path of the matched records:')
            print()
            print('>>> File Saved in search_results.txt file')

main()