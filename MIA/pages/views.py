from types import MemberDescriptorType
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import EditCoverageForm, LoginForm, RegisterForm, AddMemberForm, SearchForm, AddProviderForm, AddCoverageForm, EditMemberForm, EditProviderForm, NurseForm
from django.contrib.auth.forms import UserCreationForm
from .models import Member,Provider, Coverage, Nurse


# Create your views here.
def landing(request):
    return render(request, "pages/landing.html", {})

def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')

        form = LoginForm()
        return render(request, "pages/login.html", {'form': form})
        
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('dashboard')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'pages/login.html',{'form': form})

def log_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('landing')  

@login_required
def dashboard(request):
    return render(request, "pages/dashboard.html", {})

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'pages/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'pages/register.html', {'form': form})

@login_required        
def registerPage(request):
    user = request.user
    
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = user
            member.save()
            return redirect('dashboard')
    else:
        form = AddMemberForm()

    context = {'form': form}
    return render(request, 'pages/addMember.html', context)

@login_required
def search_members(request):
    search_results = []
    members = Member.objects.all()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_type = search_form.cleaned_data['searchType']
            search_value = search_form.cleaned_data['searchValue']

            if search_type == 'patientID':
                search_results = members.filter(patient_id=search_value)
            elif search_type == 'ssn':
                search_results = members.filter(ssn=search_value)
            
            # Check for the "SHOW_ALL" button
            if 'SHOW_ALL' in request.POST:
                search_results = []  # Clear the search results and display all members

    else:
        search_form = SearchForm()

    return render(request, 'pages/dashboard.html', {'search_form': search_form, 'search_results': search_results, 'members': members})


@login_required
def delete_member(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        try:
            member = Member.objects.get(id=member_id)
            member.delete()
            messages.success(request, 'Member deleted successfully.')
        except Member.DoesNotExist:
            messages.error(request, 'Member not found.')

    return redirect('dashboard')  # Redirect to your search members page

@login_required
def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        form = EditMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('search_members')  # Redirect to the search page after successful edit
    else:
        form = EditMemberForm(instance=member)

    return render(request, 'pages/edit_member.html', {'form': form, 'member': member})

def available_providers(request):
    try:
        result = Provider.objects.all()
    except Provider.DoesNotExist:
        result = []  # Define a default value in case of exception
    return render(request, 'pages/available_providers.html', {'result': result})

@login_required        
def add_provider(request):
    user = request.user
    
    if request.method == 'POST':
        form = AddProviderForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = user
            member.save()
            return redirect('dashboard')
    else:
        form = AddProviderForm()

    context = {'form': form}
    return render(request, 'pages/add_provider.html', context)

def update_provider(request, provider_id):
    # Assuming provider_id is passed in the URL, adjust as needed
    provider = get_object_or_404(Provider, npi=provider_id)

    if request.method == 'POST':
        form = EditProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform other actions
            return redirect('available_providers')  # Adjust the URL name or path
    else:
        form = EditProviderForm(instance=provider)

    return render(request, 'pages/update_provider.html', {'form': form, 'provider': provider})

def coverage_page(request):
    try:
        result = Coverage.objects.all()
    except Coverage.DoesNotExist:
        result = []  # Define a default value in case of exception
    return render(request, 'pages/coverage.html', {'result': result})

@login_required        
def add_coverage(request):
    user = request.user
    
    if request.method == 'POST':
        form = AddCoverageForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = user
            member.save()
            return redirect('dashboard')
    else:
        form = AddCoverageForm()

    context = {'form': form}
    return render(request, 'pages/add_coverage.html', context)

def update_coverage(request, coverage_id):
    # Assuming provider_id is passed in the URL, adjust as needed
    coverage = get_object_or_404(Coverage, coverage=coverage_id)

    if request.method == 'POST':
        form = EditCoverageForm(request.POST, instance=coverage)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform other actions
            return redirect('coverage_page')  # Adjust the URL name or path
    else:
        form = EditCoverageForm(instance=coverage)

    return render(request, 'pages/update_coverage.html', {'form': form, 'coverage': coverage})

def nurse_list(request):
    nurses = Nurse.objects.all()
    return render(request, 'pages/nurse_list.html', {'nurses': nurses})

def nurse_detail(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    return render(request, 'pages/nurse_detail.html', {'nurse': nurse})

def nurse_new(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            nurse = form.save()
            return redirect('nurse_list')
    else:
        form = NurseForm()
    return render(request, 'pages/add_nurse.html', {'form': form})

def nurse_edit(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    if request.method == "POST":
        form = NurseForm(request.POST, instance=nurse)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.save()
            return redirect('nurse_list')
    else:
        form = NurseForm(instance=nurse)
    return render(request, 'pages/edit_nurse.html', {'form': form})

def nurse_delete(request, pk):
    nurse = get_object_or_404(Nurse, pk=pk)
    nurse.delete()
    return redirect('nurse_list')