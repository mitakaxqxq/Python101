from django.contrib import admin

from education.models import Course, Lecture, Task, Solution


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'get_duration')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.duration.days // (7*4) + (obj.duration.days % (7*4))%2} months'

        return 'N/A'

    get_duration.short_description = 'Duration'


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_id', 'name', 'week', 'course', 'url')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'course', 'lecture')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'url')
