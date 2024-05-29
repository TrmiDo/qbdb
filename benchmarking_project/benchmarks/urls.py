from django.urls import path
from django.contrib import admin

from benchmarks.views import TopologyTable, ManufacturerTable, TechnologyTable, ProcessorTable, GateSetTable, GateTable, GateSetMembershipTable
from benchmarks.views import SystemTable, CalibrationTable, EmbeddingAlgorithmTable, SolverTable, TimeTypeTable, PerformanceMetricTable
from benchmarks.views import GraphTable, ProblemTable, PerformanceReportTable

from . import views
app_name = 'benchmarks'  # creates a namespace for this app
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    path('manufacturers/', ManufacturerTable.as_view()),
    path('technologies/', TechnologyTable.as_view()),
    path('embeddingalgorithms/', EmbeddingAlgorithmTable.as_view()),
    path('solvers/', SolverTable.as_view()),
    path('timetypes/', TimeTypeTable.as_view()),
    path('performancemetrics/', PerformanceMetricTable.as_view()),

    path('topologies/', TopologyTable.as_view()),
    path('processors/', ProcessorTable.as_view()),
    path('gatesets/', GateSetTable.as_view()),
    path('gates/', GateTable.as_view()),
    path('gatesetmemberships/', GateSetMembershipTable.as_view()),
    path('systems/', SystemTable.as_view()),
    path('calibrations/', CalibrationTable.as_view()),
    path('graphs/', GraphTable.as_view()),
    path('problems/', ProblemTable.as_view()),
    path('performancereports/', PerformanceReportTable.as_view())
]
