from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.response import Response
from rest_framework.views import APIView

from words.models import Word, WordList
from words.forms import AddWordsList

from rest_framework import generics, viewsets
from .serializers import WordListSerializer

WordFormSet = inlineformset_factory(WordList, Word, can_delete=True, fields=['english', 'translation'], extra=1)


class UserWordsList(LoginRequiredMixin, ListView):
    template_name = "words/users_words.html"
    model = WordList
    context_object_name = 'catalog'
    extra_context = {'title': 'Vocabulary'}

    def get_queryset(self):
        return WordList.objects.filter(user=self.request.user).select_related('user')


class UserList(LoginRequiredMixin, UpdateView):
    template_name = 'words/about.html'
    model = WordList
    context_object_name = 'dictionary'
    slug_field = "slug"
    extra_context = {'label': 'Naming'}
    form_class = AddWordsList
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return WordList.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word_formset'] = WordFormSet(instance=self.object)
        context['name_page'] = self.object.name
        return context

    def form_valid(self, form):
        self.object = form.save()
        word_formset = WordFormSet(self.request.POST, instance=self.object)
        if word_formset.is_valid():
            word_formset.save()
            return super().form_valid(form)
        return self.render_to_response(
            self.get_context_data(form=form, word_formset=word_formset))


class CreateForm(LoginRequiredMixin, CreateView):
    template_name = 'words/add_list_words.html'
    form_class = AddWordsList
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Create list'}

    def form_valid(self, form):
        form.instance.user = self.request.user

        with transaction.atomic():
            response = super().form_valid(form)

            english_list = self.request.POST.getlist('english')
            translation_list = self.request.POST.getlist('translation')

            for en, tr in zip(english_list, translation_list):
                if en.strip() and tr.strip():
                    Word.objects.create(english=en, translation=tr, list=form.instance)

        return response


class WordsListAPIView(viewsets.ModelViewSet):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer
