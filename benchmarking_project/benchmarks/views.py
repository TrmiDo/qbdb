from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Topology, Manufacturer, Technology, Processor, GateSet, Gate, GateSetMembership
from .models import System, Calibration, EmbeddingAlgorithm, Solver, TimeType, PerformanceMetric
from .models import Graph, Problem, PerformanceReport

# Create your views here.
def index(request):
    return render(request, 'benchmarks/index.html')


class ManufacturerTable(ListView):
    model = Manufacturer
    template_name = "benchmarks/table.html"

class TechnologyTable(ListView):
    model = Technology
    template_name = "benchmarks/table.html"

class EmbeddingAlgorithmTable(ListView):
    model = EmbeddingAlgorithm
    template_name = "benchmarks/table.html"

class SolverTable(ListView):
    model = Solver
    template_name = "benchmarks/table.html"

class TimeTypeTable(ListView):
    model = TimeType
    template_name = "benchmarks/table.html"

class PerformanceMetricTable(ListView):
    model = PerformanceMetric
    template_name = "benchmarks/table.html"


class TopologyTable(ListView):
    model = Topology
    template_name = "benchmarks/table.html"

class ProcessorTable(ListView):
    model = Processor
    template_name = "benchmarks/table.html"

class GateSetTable(ListView):
    model = GateSet
    template_name = "benchmarks/table.html"

class GateTable(ListView):
    model = Gate
    template_name = "benchmarks/table.html"

class GateSetMembershipTable(ListView):
    model = GateSetMembership
    template_name = "benchmarks/table.html"

class SystemTable(ListView):
    model = System
    template_name = "benchmarks/table.html"

class CalibrationTable(ListView):
    model = Calibration
    template_name = "benchmarks/table.html"

class GraphTable(ListView):
    model = Graph
    template_name = "benchmarks/table.html"

class ProblemTable(ListView):
    model = Problem
    template_name = "benchmarks/table.html"

class PerformanceReportTable(ListView):
    model = PerformanceReport
    template_name = "benchmarks/table.html"