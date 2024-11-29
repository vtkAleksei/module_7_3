class WordsFinder():


    def __init__(self, *list_files):
        self.file_names = list(list_files)


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file:
                new_str = ''
                punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    for elem in punc:
                        line.replace(str(elem), "")
                    new_str += line.lower()
                    # для удаления "-" пришлось удалить через цикл вместо ниже написанного
                    #new_str += str(re.sub(r'[^\w\s]', '', line.lower()).replace('\n', ' '))
                all_words.update({file_name: new_str.split()})
        return all_words


    def find(self, word):
        all_words_file = self.get_all_words()
        find_word = {}
        for key, elem in all_words_file.items():
            for i in [i for i, x in enumerate(elem) if x == word.lower()]:
                find_word.update({key: i+1})
                break
        return find_word


    def count(self, word):
        all_words_file = self.get_all_words()
        count_word = {}
        for key, elem in all_words_file.items():
            count = 0
            for i in [i for i, x in enumerate(elem) if x == word.lower()]:
                count += 1
            count_word.update({key: count})
        return count_word


"""finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))"""

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))


