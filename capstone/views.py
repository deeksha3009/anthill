from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from capstone.models import Group,Milestone,Update,Goal
from django.db.models import Q


def home(request):
	if request.user.is_authenticated:
		return redirect("/dashboard")

	return render(request,"home.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		print(username)
		password = request.POST['password']
		print(password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect("/dashboard")
		else:
			return HttpResponse("please Check if the username and password is correct")

	return render(request,"signin.html")
	

def signup(request):
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get("email")
		print(email)
		user = authenticate(username=username, password=password)
		if user is None:
			user = User.objects.create_user(username, email, password)
			login(request,user)
			return redirect("/dashboard/")
		else:
			return HttpResponse("Please Check the Info, User might already exist.")
	return render(request, "signup.html")


def signout(request):
	logout(request)
	return render(request,"home.html")


def dashboard(request):
	groups = Group.objects.filter(Q(members__contains=[request.user.id]) | 
		Q(guide__contains=[request.user.id]) | Q(admin=request.user))
	print(groups)
	return render(request, "dashboard.html", {"groups":groups} )

def create_group(request):
	user=request.user
	if request.method == "POST":
		name=request.POST.get('group name')
		text=request.POST.get('description')
		no_of_guides=request.POST.get('guide/s')
		no_of_members=request.POST.get('member/s')
		group=Group.objects.create(group_name=name,description=text, 
			no_of_members=no_of_members, 
			no_of_guides=no_of_guides, admin=user)
		return redirect("/dashboard/")
	return render(request,'dashboard.html')
	

def group_page(request,gid):
	group = Group.objects.get(pk=gid)
	users = User.objects.all()
	members = [User.objects.get(pk=id) for id in group.members]
	guides = [User.objects.get(pk=id) for id in group.guide]
	updates = Update.objects.filter(group=group)
	milestones = Milestone.objects.filter(group=group)
	goals = Goal.objects.filter(milestone__id__in=milestones)
	print(updates)
	return render(request,"group_page.html",{"group":group, 
		"members":members, "guides":guides, 
		"updates":updates, "milestones":milestones, 
		"goals":goals,
		"users":users})


def add_members(request,gid):
	user=request.user
	group = Group.objects.get(pk=gid)
	if request.method == "POST":
		userid = request.POST.get('user')
		group.members.append(int(userid))
		group.save()
		return redirect(f"/group/{group.id}/")

	return render(request,"group_page.html", {"group":group})

def add_guides(request,gid):
	user=request.user
	group = Group.objects.get(pk=gid)
	if request.method == "POST":
		userid = request.POST.get('user')
		group.guide.append(int(userid))
		group.save()	
		return redirect(f"/group/{group.id}/")

	return render(request,"group_page.html", {"group":group})


def updates(request, gid):
	group = Group.objects.get(pk=gid)
	user = request.user
	if request.method == "POST":
		title=request.POST.get('title')
		content=request.POST.get('update')
		post=Update(title=title,text=content,group=group,user=user)
		post.save()
		# uid=post.pk
		return redirect(f"/group/{gid}/")
	print(group)
	return render(request, "update.html", {"group":group})


def add_milestone(request,gid):
	group = Group.objects.get(pk=gid)
	user = request.user
	if request.method == "POST":
		title=request.POST.get('title')
		context=request.POST.get('content')
		date=request.POST.get('due_date')
		posts=Milestone(title=title,content=context,due_date=date,group=group,user=user)
		posts.save()
		return redirect(f"/group/{gid}/")

	return render(request, "milestones.html", {"group":group})


def view_milestones(request,mid):
	milestone=Milestone.objects.get(pk=mid)
	if request.method == "POST":
		title = request.POST.get('goal')
		goal = Goal(title=title,milestone=milestone,group=milestone.group)
		goal.save()
		print(goal)
		return redirect(f"/group/{milestone.group.id}/")
	print(milestone)
	return render(request , "milestone.html", {"milestones":milestone})

