from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Publication, Comment
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# todo rewrite for generic views
def index(request):
    context = {}
    publications = Publication.objects.annotate(number_of_comments=Count('comment')).order_by('pub_date')
    current_page = Paginator(publications, 10)
    page = request.GET.get('page')
    try:
        context['publication_list'] = current_page.page(page)
    except PageNotAnInteger:
        context['publication_list'] = current_page.page(1)
    except EmptyPage:
        context['publication_list'] = current_page.page(current_page.num_pages)

    return render(request, 'publications/index.html', context)


def publication_detail(request, publication_id):
    #todo may be use more simple method to get comments for publiocation, need read the docs
    publication = Publication.objects.get(id=publication_id)
    comments = Comment.objects.filter(publication=publication_id)
    return render(request, 'publications/publication.html', {'publication': publication, 'comments': comments})


def comment(request, publication_id):
    #todo add check a valid data in request.POST
    new_comment = Comment()
    new_comment.author = request.POST['author']
    new_comment.text = request.POST['text']
    new_comment.publication = Publication.objects.get(id=publication_id)
    new_comment.save()
    # todo rewrite to relative path (may change for pub's or another)
    return redirect('/publications/' + str(publication_id) + '/')
