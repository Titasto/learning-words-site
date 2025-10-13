from .vocabulary import vocabulary
import random

class QueryHandle:
    def __init__(self, request):
        self.request = request
        self.query = request.session['query_for_training']
        self.index = self.query['index']
        self.words = self.query['words']
        self.result = self.query['result']
        self.type_training = self.query['type_training']
        self.type_training_bool = self.type_training == 'reverse'
        self.mode = self.query['mode']

    def get_index(self):
        return self.index

    def get_words(self):
        return self.words

    def get_result(self):
        return self.result

    def get_current_word(self):
        return self.words[self.index]

    def updt_index(self, number=None):
        if number is None:
            self.query['index'] += 1
        else:
            self.query['index'] = number

    def updt_words(self, words=None):
        self.query['words'] = words if words is not None else self.words

    def updt_result(self):
        self.query['result'] = self.result

    def updt_query(self, index=None, words=None):
        self.updt_index(index)
        self.updt_words(words)
        self.updt_result()
        self.save()

        return self.query

    def save(self):
        self.request.session['query_for_training'] = self.query

    def check_answer(self, answer):
        if self.mode == 'flip_mode':
            self.words[self.index]['level'] += 1
            self.result['correct'] += 1
        else:
            key = 'translation' if self.type_training_bool else 'english'
            if answer == self.words[self.index][key]:
                self.words[self.index]['level'] += 1
                self.result['correct'] += 1
            else:
                self.result['incorrect'] += 1

        self.updt_query()

    def preparing_words(self):
        words_for_test = [self.words[self.index]]
        if not self.mode == 'flip_mode':
            random_words = random.sample(vocabulary, 2)
            words_for_test.extend(random_words)
            random.shuffle(words_for_test)

        return words_for_test

    def handle_result(self):
        data = self.new_list()

        if data['new_list']:
            self.result['correct'] = 0
            self.updt_query(index=0, words=data['new_list'])
            return True
        return False

    def new_list(self):
        if self.mode == 'practice_mode':
            new_list = [word for word in self.words if word['level'] == 1]
        elif self.mode == 'flip_mode':
            new_list = []
        else:
            new_list = [word for word in self.words if word['level'] < 3 and
                        self.mode not in ('flip_mode', 'practice_mode')]
        per_cent = (self.result['correct'] / len(self.words)) * 100 if self.words else 0

        data = {
            'new_list': new_list,
            'per_cent': round(per_cent)
        }

        return data

    # def condition(self):
    #     if self.mode != 'flip_mode':
    #         return self.index >= len(self.words)
    #     return