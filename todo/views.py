from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware
from .forms import NewUserForm
from .models import TodoItem, Client, Activity, RandomGiphy

import json
import datetime
import random

first_time = True
User = get_user_model()

# TODO: fix this if you're going to have multiple concurrent users
selected_client_id = 1

# Create your views here.

# homeView - just one student's data arranged by time
@login_required
def homeView(request):
  resp_data = {}
  global first_time
  global selected_client_id

  if (first_time):
      # new_item =  TodoItem(content = "build a cool app on replit.com")
      # new_item.save()
      first_time = False

  all_random_giphy = RandomGiphy.objects.all()
  # resp_data['all_random_giphy'] = json.dumps(list(all_random_giphy), cls=DjangoJSONEncoder)
  resp_data['all_random_giphy'] = all_random_giphy
  one_random_giphy = random.choice(all_random_giphy)
  resp_data['one_random_giphy'] = one_random_giphy

  all_todo_items = TodoItem.objects.filter(client__id=selected_client_id).order_by('-updated_at')
  resp_data['all_items'] = all_todo_items

  clients = Client.objects.all()
  print("selected_client_id: " + str(selected_client_id))

  resp_data['clients'] = clients
  resp_data['selected_client'] = Client.objects.get(pk=selected_client_id)

  all_activities = Activity.objects.all()
  resp_data['all_activities'] = all_activities

  jaa = json.loads(serializers.serialize('json', all_activities))
  activities_index = { j['pk']: {'name': j['fields']['name'], 'color': j['fields']['color']} for j in jaa }

  # get distinct dates and sort them
  # activity_dates = list(map(lambda d: d.updated_at.date(), list(all_todo_items)))
  # distinct_activity_dates = list(set(activity_dates))
  # distinct_activity_dates.sort(reverse=True)
  # resp_data['distinct_activity_dates'] = distinct_activity_dates

  consolidated_activity_data = TodoItem.objects.filter(
          client__id=selected_client_id
      ).order_by(
          '-updated_at__date'
      ).values(
          'updated_at__date', 'client', 'activity'
      ).annotate(
          total_count=Count('id')
      )
  
  cad_by_date = {}
  for c in list(consolidated_activity_data):
      sdate = str(c['updated_at__date'])
      ser_cad = {
        'updated_at__date': str(c['updated_at__date']),
        'client': c['client'],
        'client_display_name': resp_data['selected_client'].display_name,
        'activity': c['activity'],
        'activity_name': activities_index[c['activity']]['name'],
        'activity_color': activities_index[c['activity']]['color'],
        'total_count': c['total_count']
      }
      if sdate not in cad_by_date.keys():
          cad_by_date[sdate] = [ser_cad]
      else:
          cad_by_date[sdate].append(ser_cad)

  # resp_data['consolidated_activity_data'] = consolidated_activity_data
  resp_data['cad_by_date'] = cad_by_date

  return render(
    request, 
    'home.html',
    resp_data
  )

# streamView - everything from all users
@login_required
def streamView(request):
  resp_data = {}
  global selected_client_id

  all_random_giphy = RandomGiphy.objects.all()
  one_random_giphy = random.choice(all_random_giphy)
  resp_data['one_random_giphy'] = one_random_giphy

  all_todo_items = TodoItem.objects.all()
  resp_data['all_items'] = all_todo_items
  # print(all_todo_items[0])

  clients = Client.objects.all()
  print("streamView: selected_client_id: " + str(selected_client_id))

  resp_data['clients'] = clients
  resp_data['selected_client'] = Client.objects.get(pk=selected_client_id)

  all_activities = Activity.objects.all()
  resp_data['all_activities'] = all_activities

  return render(
    request, 
    'stream.html',
    resp_data
  )

@login_required
def statsView(request):
  resp_data = {}
  global selected_client_id

  all_random_giphy = RandomGiphy.objects.all()
  one_random_giphy = random.choice(all_random_giphy)
  resp_data['one_random_giphy'] = one_random_giphy

  all_todo_items = TodoItem.objects.all()
  resp_data['all_items'] = all_todo_items
  # print(all_todo_items[0])

  clients = Client.objects.all()
  print("streamView: selected_client_id: " + str(selected_client_id))

  resp_data['clients'] = clients
  resp_data['selected_client'] = Client.objects.get(pk=selected_client_id)

  all_activities = Activity.objects.all()
  resp_data['all_activities'] = all_activities

  # DjangoJSONEncoder
  print(resp_data)

  return render(
    request, 
    'stats.html',
    resp_data
  )
     

@login_required
def addTodo(request):
  # global selected_client_id
  print(request.POST)

  # content = request.POST['content']
  client_id = request.POST['client_id']
  activity_id = request.POST['activity_id']
  client = Client.objects.get(pk=client_id)
  activity = Activity.objects.get(pk=activity_id)
  print(f"updated_by = {request.user}")
  new_item = TodoItem(
    client=client,
    activity=activity,
    updated_at=make_aware(datetime.datetime.now()),
    done=True,
    # created_by=request.user,
    # updated_by=request.user
  )

  new_item.save()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def selectClient(request, client_id):
  global selected_client_id
  selected_client_id = client_id 
  print("selected_client: " + str(selected_client_id))
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def doneTodo(request, todo_id):
  item_to_done = TodoItem.objects.get(id=todo_id)
  item_to_done.done = not item_to_done.done
  item_to_done.updated_at = make_aware(datetime.datetime.now())
  item_to_done.save()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def addActivity(request):
    print(request.POST)
    name=request.POST['name']
    description=request.POST['description']
    youtube_url=request.POST['youtube_url']
    new_activity = Activity(name=name, description=description, youtube_url=youtube_url)
    new_activity.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Auth
def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("/")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(homeView)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, 'registration/register.html', {"register_form":form})
