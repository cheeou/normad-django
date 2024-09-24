from django.contrib import admin
from .models import Tweet, Like

class ElonMuskFilter(admin.SimpleListFilter):
    title = 'Elon Musk 포함 여부'  # 필터의 제목
    parameter_name = 'elon_musk'  # URL에 사용될 파라미터 이름

    def lookups(self, request, model_admin):
        """ 필터에서 제공할 선택지 """
        return [
            ('yes', 'Elon Musk 포함'),
            ('no', 'Elon Musk 미포함'),
        ]

    def queryset(self, request, queryset):
        """ 필터가 적용되었을 때 실행될 쿼리셋 필터링 로직 """
        if self.value() == 'yes':
            return queryset.filter(payload__icontains='Elon Musk')  # 'Elon Musk'가 포함된 트윗 필터링
        if self.value() == 'no':
            return queryset.exclude(payload__icontains='Elon Musk')  # 'Elon Musk'가 포함되지 않은 트윗 필터링
        return queryset
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('payload', 'user', 'like_count')
    list_filter = [ElonMuskFilter]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'user', 'created_at')  
    search_fields = ('user__username',) 
    list_filter = ('created_at',)  