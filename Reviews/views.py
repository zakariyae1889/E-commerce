from django.shortcuts import render


class ReviewsApp():
    def PageReviews(request):
        return render(request,template_name='include/Review.html')