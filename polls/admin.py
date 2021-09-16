from django.contrib import admin
from . import models


admin.site.register(
    [
        models.Poll,
        models.Choice,
        models.Vote,
    ]
)
