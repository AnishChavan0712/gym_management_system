from django.shortcuts import render, get_object_or_404, redirect
from .models import Member  # Import models if required
from .forms import MemberForm

def home(request):
    return render(request, 'home.html')

def members_list(request):
    members = Member.objects.all()  # Fetch all members
    return render(request, 'member_list.html', {'members': members})

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)  # Fetch a specific member
    return render(request, 'member_detail.html', {'member': member})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')  # Redirect to the members list page
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})
