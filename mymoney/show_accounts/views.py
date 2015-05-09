from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    menu_categories = ['help'];
    context_dict = {'categories': menu_categories}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'show_accounts/index.html', context_dict)

def about(request):
	context_dict = {'user_context': "This is another user provided value to avariable already defined in the template"}
	return render(request, 'show_accounts/about.html',context_dict)


def login(request):
	
	context_dict = {'user_name': "This is another user provided value to avariable already defined in the template"}
	return render(request, 'show_accounts/login.html',context_dict)
