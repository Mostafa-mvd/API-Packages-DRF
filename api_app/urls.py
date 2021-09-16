from django.urls import path, include
from rest_framework import routers
from . import views as api_views
from todo import views as todo_views
from posts import views as posts_views
from polls import views as polls_views


app_name = "api"


router = routers.DefaultRouter()


router.register(
    prefix="posts",
    viewset=posts_views.PostViewSets,
    basename="posts_viewset"
)

router.register(
    prefix="users",
    viewset=posts_views.UserViewSets,
    basename="users_viewset"
)


urlpatterns = [
    path(
        route="books/all/",
        view=api_views.ListBooksAPIView.as_view(),
        name="all",
    ),
    path(
        route="todo/list/",
        view=todo_views.TodoListAPIView.as_view(),
        name="todo_list"
    ),
    path(
        route="todo/detail/<int:pk>/",
        view=todo_views.TodoDetailAPIView.as_view(),
        name="todo_detail"
    ),
    path(
        route="posts/list/",
        view=posts_views.PostList.as_view(),
        name="posts_list_create"
    ),
    path(
        route="post/detail/<int:pk>/",
        view=posts_views.PostDetail.as_view(),
        name="post_detail_retrieve_update_destroy"
    ),
    path(
        route="users/list/",
        view=posts_views.UserList.as_view(),
        name="users_posts"
    ),
    path(
        route="users/detail/<int:pk>/",
        view=posts_views.UserDetail.as_view(),
        name="users_detail"
    ),
    path(
        route='viewsets/', 
        view=include(router.urls)
    ),
    path(
        route='polls-api-view/list/',
        view=polls_views.PollList.as_view()
    ),
    path(
        route='polls-api-view/detail/<int:pk>/',
        view=polls_views.PollDetail.as_view()
    ),
    path(
        route='polls-generic-view/list/',
        view=polls_views.PollListCreate.as_view()
    ),
    path(
        route='polls-generic-view/detail/<int:pk>/',
        view=polls_views.PollDetailRemove.as_view()
    ),
    path(
        route='polls-generic-view/<int:pk>/choices-generic-view/',
        view=polls_views.ChoiceListCreate.as_view()
    ),
    path(
        route='vote-generic-view/',
        view=polls_views.VoteCreate.as_view()
    ),
    path(
        route='polls-generic-view/<int:poll_pk>/choices-generic-view/<int:choice_pk>/vote/',
        view=polls_views.VoteCreateAPIView.as_view()
    )
]
