from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    if request.method == "POST":
        word = request.POST['word']
        dictionary = PyDictionary()
        meaning = dictionary.meaning(word)
        synonyms = dictionary.synonym(word)
        antonyms = dictionary.antonym(word)
        context = {
            'meaning':meaning,
            'synonyms':synonyms,
            'antonyms':antonyms
        }
        return render(request,'index.html',context)
    return render(request,'index.html')
