from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_tables2 import SingleTableView
from .models import Topology, Manufacturer, Technology, Processor, GateSet, Gate, GateSetMembership
from .models import System, Calibration, EmbeddingAlgorithm, Solver, TimeType, PerformanceMetric
from .models import Graph, Problem, PerformanceReport
from .tables import ManufacturerTable, TechnologyTable, TopologyTable, ProcessorTable, GateSetTable, GateTable, GateSetMembershipTable, SystemTable, CalibrationTable, GraphTable, ProblemTable, PerformanceReportTable, EmbeddingAlgorithmTable, SolverTable, TimeTypeTable, PerformanceMetricTable

# Create your views here.
def index(request):
    return render(request, 'benchmarks/index.html')


class ManufacturerTable(SingleTableView):
    model = Manufacturer
    table_class = ManufacturerTable
    template_name = "benchmarks/table.html"

class TechnologyTable(SingleTableView):
    model = Technology
    table_class= TechnologyTable
    template_name = "benchmarks/table.html"

class EmbeddingAlgorithmTable(SingleTableView):
    model = EmbeddingAlgorithm
    table_class= EmbeddingAlgorithmTable
    template_name = "benchmarks/table.html"

class SolverTable(SingleTableView):
    model = Solver
    table_class = SolverTable
    template_name = "benchmarks/table.html"

class TimeTypeTable(SingleTableView):
    model = TimeType
    table_class = TimeTypeTable
    template_name = "benchmarks/table.html"

class PerformanceMetricTable(SingleTableView):
    model = PerformanceMetric
    table_class = PerformanceMetricTable
    template_name = "benchmarks/table.html"


class TopologyTable(SingleTableView):
    model = Topology
    table_class= TopologyTable
    template_name = "benchmarks/table.html"

class ProcessorTable(SingleTableView):
    model = Processor
    table_class = ProcessorTable
    template_name = "benchmarks/table.html"

class GateSetTable(SingleTableView):
    model = GateSet
    table_class = GateSetTable
    template_name = "benchmarks/table.html"

class GateTable(SingleTableView):
    model = Gate
    table_class = GateTable
    template_name = "benchmarks/table.html"

class GateSetMembershipTable(SingleTableView):
    model = GateSetMembership
    table_class= GateSetMembershipTable
    template_name = "benchmarks/table.html"

class SystemTable(SingleTableView):
    model = System
    table_class = SystemTable
    template_name = "benchmarks/table.html"

class CalibrationTable(SingleTableView):
    model = Calibration
    table_class = CalibrationTable
    template_name = "benchmarks/table.html"

class GraphTable(SingleTableView):
    model = Graph
    table_class = GraphTable
    template_name = "benchmarks/table.html"

class ProblemTable(SingleTableView):
    model = Problem
    table_class = ProblemTable
    template_name = "benchmarks/table.html"

class PerformanceReportTable(SingleTableView):
    model = PerformanceReport
    table_class= PerformanceReportTable
    template_name = "benchmarks/table.html"