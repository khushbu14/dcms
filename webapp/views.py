from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, mail_admins
from django.contrib.auth import authenticate , login, logout


# models

from webapp.models import Contributor,Reviewer,Subject

#forms
 
from webapp.forms import ContributorForm, PostForm, ContributorUploadForm

def submit_post(request):
	""" Create a form to submit post.
	"""
	context = RequestContext(request)

	if request.POST:
		postform = PostForm(data=request.POST)  # creating a new instance for using it
		if postform.is_valid():
			postform.save(commit=True)
			return HttpResponseRedirect('/webapp/blog')
		else:
			print postform.errors
	else:
		postform = PostForm()
		print postform
	
	context_dict = {
		'postform': postform,
	}
	return render_to_response("webapp/submitpost.html", context_dict , context)

def userlogin(request):
    """Login form.
    
    Arguments:
    - `request`:
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
		for group in user.groups.all():
			if group.name == 'contributor':
		                login(request, user)
                		return HttpResponseRedirect('/webapp/user/upload/')
			if group.name == 'reviewer':
				login(request,user)
				return HttpResponseRedirect('/webapp/user/review')
            else:
                # An inactive account was used - no logging in!
                messages.info(request, "Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.error(request, "Bad login!")
            return render_to_response('webapp/login.html', context)
    else:
        return render_to_response('webapp/login.html', context)

def upload(request):
	return render_to_response("upload.html")

def review(request):
	return render_to_response("review.html")

def home(request):
	context = RequestContext(request)
	return render_to_response('webapp/home.html',context)

def contributor_signup(request):

	"""Request for new contributor to signup"""
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':
	        print "we have a request to register"    
	        contributor_form = ContributorForm(request.POST,request.FILES)
	        if contributor_form.is_valid():
                	print "Forms are valid"

                        if 'picture' in request.FILES:
                		user = Contributor(picture=request.FILES['picture'])
	                user = Contributor(validation_docs=request.FILES['validation_docs'])
                        user = contributor_form.save(commit=False)
                        

                        user.set_password(user.password)
                        user.save()
                        
		
                        email_subject="New Contributor has registered"
	                email_message="""
New Contributor has registered.
	    	
Details:
Name:""" + user.first_name + """  """ + user.last_name + """"
Email:""" + user.email + """ 
# + newContributor.validation_docs +

Waiting for your your approval"""
		#	send_mail(email_subject, email_message, 'khushbu.ag23@gmail.com', ['pri.chundawat@gmail.com'],fail_silently=False)
			messages.success(request,"form successfully submitted. Waiting for activation  from admin.")
			return HttpResponseRedirect(reverse('webapp.views.home'))
	        else:
			if contributor_form.errors:
				print contributor_form.errors
	else:
		contributor_form = ContributorForm()	
           
        context_dict = {'contributor_form': contributor_form, 'registered': registered}
        return render_to_response('webapp/signup.html', context_dict, context)

def contributor_upload(request, username):
	"""Request for new upload by the contributor"""
	context = RequestContext(request)
	uploaded= False
	if request.method == 'POST':
	        print "we have a request for upload by the contributor"    
	        contributor_upload_form = ContributorUploadForm(request.POST,request.FILES)
		if contributor_upload_form.is_valid():	
			print "Forms are valid"
			contributor=Contributor.objects.all().filter(username=username)
			subject.name = contributor.specialised_subject
			subject.contributor = contributor.id
			if 'pdf_doc' in request.FILES:
                		subject = Subject(pdf_doc = request.FILES['pdf_doc'])
			if 'video_doc' in request.FILES:
                		subject = Subject(pdf_doc = request.FILES['video_doc'])
			if 'animations_doc' in request.FILES:
                		subject = Subject(pdf_doc = request.FILES['animations_doc'])
			subject = contributor_upload_form.save(commit=False)                       
                        subject.save()
			return HttpResponseRedirect('webapp/home')
	        else:
			if contributor_upload_form.errors:
				print contributor_upload_form.errors
	else:
		contributor_upload_form = ContributorUploadForm()	
           
        context_dict = {'contributor_upload_form': contributor_upload_form,'subject.name':subject.name, 'contributor.id':contributor.id, 'uploaded':uploaded}
        return render_to_response("webapp/upload.html", context_dict, context)
			
			
