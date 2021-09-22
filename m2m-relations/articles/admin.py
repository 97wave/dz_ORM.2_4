from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Scope
import json

class RelationshipInlineFormset(BaseInlineFormSet):
    
    def clean(self):
        super(RelationshipInlineFormset, self).clean()
        cnt = 0
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['is_main']:
                    cnt += 1
            if cnt > 1:
                raise ValidationError('У же есть один основной раздел, выебирте один!')

            if cnt < 1:
                raise ValidationError("Вам необходимо выбрать один основной раздел!")
        
        return super().clean() 


class RelationshipInline(admin.TabularInline):
    model = Scope.relation.through
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    exclude = ('relation',)

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]