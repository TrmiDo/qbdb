from django.contrib import admin
from .models import Topology, Manufacturer, Technology, Processor
from .models import GateSet, Gate, GateSetMembership
from .models import System, Calibration
from .models import EmbeddingAlgorithm, Solver, TimeType, PerformanceMetric, Graph, Problem, PerformanceReport

# Register your models here.
admin.site.register(Topology)
admin.site.register(Manufacturer)
admin.site.register(Technology)
admin.site.register(Processor)
admin.site.register(GateSet)
admin.site.register(Gate)
admin.site.register(GateSetMembership)
admin.site.register(System)
admin.site.register(Calibration)
admin.site.register(EmbeddingAlgorithm)
admin.site.register(Solver)
admin.site.register(TimeType)
admin.site.register(PerformanceMetric)
admin.site.register(Graph)
admin.site.register(Problem)
admin.site.register(PerformanceReport)