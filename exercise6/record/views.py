from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from record.models import Record
from .forms import RecordForm

@login_required
def home(request):
	context = {}

	if request.method == 'POST':
		form = RecordForm(request.POST)
		if form.is_valid():
			Record.objects.create(
				title=form.cleaned_data.get('title'),
				type=form.cleaned_data.get('type'),
				start_date=form.cleaned_data.get('start_date'),
				end_date=form.cleaned_data.get('end_date'),
				approve_status=2,
				create_by=request.user
			)
			form = RecordForm()
			return redirect('history')
	else:
		form = RecordForm()

	context['form'] = form
	return render(request, 'record/dayoff.html', context=context)

def mylogin(request):
	context = {}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user:
			login(request, user)

			next_url = request.POST.get('next_url')
			if next_url:
				return redirect(next_url)
			else:
				if request.user.is_staff:
					return redirect('/admin')
				else:
					return redirect('/request')
		else:
			context['username'] = username
			context['password'] = password
			context['error'] = 'Wrong username or password!'

	next_url = request.GET.get('next')
	if next_url:
		context['next_url'] = next_url
	return render(request, 'record/index.html', context=context)

def mylogout(request):
	logout(request)
	return redirect('login')

@login_required
def history(request):
	context = {
		'record': Record.objects.all().filter(create_by=User.objects.get(username=request.user))
	}
	return render(request, 'record/history.html', context=context)