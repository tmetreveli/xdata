from django.shortcuts import render, redirect
from .models import FilterWords
from .models import Article
from django.http import HttpResponse
from .forms import CSVUploadForm
from .models import Client
import csv
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import ClientForm
from django.contrib import messages



def home(request):
    # return HttpResponse("Hello, this is the home page!")
    return render(request, "home.html")


def view_client_articles(request, client_id):
    articles_for_client = Article.objects.filter(client_id=client_id)
    print(articles_for_client)

    return render(request, 'client_articles.html', {'articles': articles_for_client})


# def upload_csv(request, client_id):
#     if request.method == "POST":
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             decoded_file = file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             filter_words = list(reader)
#             request.session['filter_words'] = filter_words

#             # For preview, render them in context
#             return render(request, 'preview.html', {'filter_words': filter_words})
#     else:
#         form = CSVUploadForm()
#     return render(request, 'upload.html', {'form': form})

def upload_csv(request, client_id):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            filter_words = list(reader)
            request.session['filter_words'] = filter_words

            # For preview, render them in context
            # return render(request, 'preview.html', {'filter_words': filter_words, 'client_id':client_id})
            return render(request, 'preview.html', {'filter_words': filter_words, 'client_id': client_id})
    
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def save_filter_words(request, client_id):
    # Check if 'filter_words' key is in session
    if 'filter_words' in request.session:
        words = request.session['filter_words']
        print('hello')
        # Ensure 'words' is a list or iterable
        if not isinstance(words, (list, tuple)):
            return HttpResponse("Error in data format!")
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return HttpResponse("Client not found!")

        # Iterate over words and save them
        for word in words:
            # Ensure 'word' is a list/tuple and has at least one item
            if not isinstance(word, (list, tuple)) or not word:
                continue
            FilterWords.objects.create(word=word[0], client=client)
        
        # Clear the session data
        del request.session['filter_words']
        return HttpResponse("Saved successfully!")
    else:
        return HttpResponse("No data to save!")


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return(redirect(list_view))
    context['form'] = form
    return render(request, "", context)

# def create_view(request):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}

#     # add the dictionary during initialization
#     form = ClientForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context['form'] = form
#     return render(request, "", context)



def list_view(request):
    # dictionary for initial data with
    # field names as keys
    # context = {}

    # add the dictionary during initialization
    users = Client.objects.all()

    return render(request, "home.html", {'users': users})


# from django.shortcuts import render

# relative import of forms
# from .models import GeeksModel


# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Client.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Client, id=id)

    # pass the object as instance in form
    form = ClientForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("Successfully updated", redirect_to='home')
        html_content = """
            <script>
                alert('Successfully updated');
                window.location.href = '/';
            </script>
        """
        return HttpResponse(html_content)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Client, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        html_content = """
            <script>
                alert('Successfully deleted');
                window.location.href = '/';
            </script>
        """
        return HttpResponse(html_content)

    return render(request, "delete_view.html", context)