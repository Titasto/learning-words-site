from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from words.models import WordList, Word
from .vocabulary import vocabulary
from .servise import QueryHandle


@login_required
def choice_test(request):
    if request.method == 'POST':
        name = request.POST.get('vocabulary')
        list_id = WordList.objects.get(user=request.user, name=name).id
        reverse = request.POST.get('translation')
        mode = request.POST.get('mode')

        request.session['type_training'] = reverse
        request.session['mode'] = mode

        return redirect('training:start_training', list_id=list_id)

    elif request.method == 'GET':
        catalog = WordList.objects.filter(user=request.user)

        data = {
            'catalog': catalog,
            'title': 'Choice test'
        }

    return render(request, 'training/choice_test.html', context=data)


def start_train(request, list_id):
    words = list(Word.objects.filter(list__id=list_id, list__user=request.user).values('id', 'english', 'translation'))
    name_list = WordList.objects.get(id=list_id, user=request.user).name
    print(name_list)
    for word in words:
        word.setdefault('level', 1)

    request.session['query_for_training'] = {
        'index': 0,
        'words': words,
        'result': {'correct': 0, 'incorrect': 0},
        'type_training': request.session['type_training'],
        'mode': request.session['mode'],
        'name_list': name_list,
    }

    return redirect('training:training_step')


def training(request):
    query = QueryHandle(request)

    if request.method == 'POST':
        answer = request.POST.get('translation') if query.type_training_bool else request.POST.get('english')
        query.check_answer(answer)

        return redirect('training:training_step')

    if request.method == 'GET':

        if query.get_index() >= len(query.get_words()):
            return redirect('training:results')
        else:
            words_for_test = query.preparing_words()
            data = {'title': f'Training {request.session['query_for_training']['name_list']} ', 'words': words_for_test,
                    'type_training': query.type_training, 'word': query.get_current_word(), 'mode': query.mode}

    return render(request, 'training/training_step.html', context=data)


def results(request):
    query = QueryHandle(request)
    query_data = query.new_list()

    data = {
        'title': 'Results',
        'rait': query_data['per_cent'],
        'word_list': query_data['new_list'],
        'mode': query.mode
    }

    if request.method == 'POST':
        action = request.POST.get("action")

        if action == "next":
            if query.handle_result():
                return redirect('training:training_step')
            return redirect('training:choice_test')

        if action == "finish":
            return redirect('training:choice_test')

    return render(request, 'training/results.html', context=data)



