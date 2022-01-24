from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from articals.models import BloodRequestPost

# Create your views here.
def articals_index(request):
    # if request.user.is_authenticated:
    #     current_user=request.user
    #     user_id=current_user.id
    #     post=BloodRequestPost.objects.get(author__pk=user_id)
    post=BloodRequestPost.objects.all()
    context={"allPost":post}
    return render(request, 'articals/communityPost.html',context)


def request_blood_post(request):
    if request.user.is_authenticated:
        current_user=request.user

    if request.method=='POST':
        bloodGroup=request.POST.get('bloodGroup')
        quantity=request.POST.get('quantity')
        location=request.POST.get('location')
        date=request.POST.get('date')
        phone=request.POST.get('phone')

        bloodPost=BloodRequestPost(
            author=current_user,
            phone=phone,
            bloodgroup=bloodGroup,
            locations=location,
            neededBlood=quantity,
            requestDate=date,
        )
        bloodPost.save()
        return redirect(reverse_lazy('articals:articals_index'))

