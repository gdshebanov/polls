from django.contrib import admin
from polls.models import Poll, Choice, Vote


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    model = Poll
    inlines = (ChoiceInline,)
    list_display = ('question', 'count_choices', 'count_total_votes')


class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('choice', 'ip_address', 'voter_name', 'poll')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
