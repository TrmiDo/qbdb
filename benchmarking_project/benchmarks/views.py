from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_tables2 import SingleTableView
from .models import Topology, Manufacturer, Technology, Processor, GateSet, Gate, GateSetMembership
from .models import System, Calibration, Solver, PerformanceMetric
from .models import Graph, Problem, PerformanceReport
from .models import CompilationTool, CompilationAlgorithmn, CompilationStep, PerformanceValue, ProblemInstance
from .tables import ManufacturerTable, TechnologyTable, TopologyTable, ProcessorTable, GateSetTable, GateTable, GateSetMembershipTable, SystemTable, CalibrationTable, GraphTable, ProblemTable, PerformanceReportTable, SolverTable,PerformanceMetricTable
from .tables import CompilationToolTable, CompilationAlgorithmnTable, CompilationStepTable, PerformanceValueTable, ProblemInstanceTable
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'benchmarks/index.html')

class CompilationToolTable(SingleTableView):
    model = CompilationTool
    table_class = CompilationToolTable
    template_name = "benchmarks/table.html"

class CompilationAlgorithmnTable(SingleTableView):
    model = Manufacturer
    table_class = CompilationAlgorithmnTable
    template_name = "benchmarks/table.html"

class CompilationStepTable(SingleTableView):
    model = CompilationStep
    table_class = CompilationStepTable
    template_name = "benchmarks/table.html"

class PerformanceValueTable(SingleTableView):
    model = PerformanceValue
    table_class = PerformanceValueTable
    template_name = "benchmarks/table.html"

class ProblemInstanceTable(SingleTableView):
    model = ProblemInstance
    table_class = ProblemInstanceTable
    template_name = "benchmarks/table.html"

class ManufacturerTable(SingleTableView):
    model = Manufacturer
    table_class = ManufacturerTable
    template_name = "benchmarks/table.html"

class TechnologyTable(SingleTableView):
    model = Technology
    table_class= TechnologyTable
    template_name = "benchmarks/table.html"

class SolverTable(SingleTableView):
    model = Solver
    table_class = SolverTable
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

def Performance(request):
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM benchmarks_PerformanceReport as a 
        join benchmarks_solver as b on a.solver_id =b.id
        join benchmarks_performanceValue as c on c.performance_report_id = a.id 
        join benchmarks_performanceMetric as d on c.metric_id= d.id
        join benchmarks_compilationstep as e on e.performance_report_id = a.id
        join benchmarks_compilationAlgorithmn as f on f.id= e.compilation_Algorithmn_id
        join benchmarks_compilationTool as g on g.id = e.compilation_tool_id''')
        joined_results = cursor.fetchall()

    # Check if any results were fetched
    if not joined_results:
        print("No results found")

    columns = [col[0] for col in cursor.description]
    context = {
        'joined_results': joined_results,  # Ensure this matches your template
        'columns': columns
    }
    return render(request, 'benchmarks/maintable.html', context)

def ProblemInstanceList(request):
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM benchmarks_ProblemInstance as a 
        join benchmarks_graph as b on a.graph_id =b.id
        join benchmarks_problem as c on c.id = a.problem_id
        ''')
        joined_results = cursor.fetchall()

    # Check if any results were fetched
    if not joined_results:
        print("No results found")

    columns = [col[0] for col in cursor.description]
    context = {
        'joined_results': joined_results,  # Ensure this matches your template
        'columns': columns
    }
    return render(request, 'benchmarks/maintable.html', context)


def SystemCali(request):
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM benchmarks_system as a 
        join benchmarks_calibration as b on a.id= b.system_id
        ''')
        joined_results = cursor.fetchall()

    # Check if any results were fetched
    if not joined_results:
        print("No results found")

    columns = [col[0] for col in cursor.description]
    context = {
        'joined_results': joined_results,  # Ensure this matches your template
        'columns': columns
    }
    return render(request, 'benchmarks/maintable.html', context)



def ProcessorList(request):
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM benchmarks_Processor as a 
        join benchmarks_manufacturer as b on a.manufacturer_id =b.id
        join benchmarks_technology as c on c.id = a.technology_id
        join benchmarks_topology as d on a.topology_id=d.id
        ''')
        joined_results = cursor.fetchall()

    # Check if any results were fetched
    if not joined_results:
        print("No results found")

    columns = [col[0] for col in cursor.description]
    context = {
        'joined_results': joined_results,  # Ensure this matches your template
        'columns': columns
    }
    return render(request, 'benchmarks/maintable.html', context)

def GateList(request):
    
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM benchmarks_gateset as a 
        join benchmarks_gatesetmembership as b on a.id =b.gate_set_id
        join benchmarks_gate as c on c.id = b.gate_id
        ''')
        joined_results = cursor.fetchall()

    # Check if any results were fetched
    if not joined_results:
        print("No results found")

    columns = [col[0] for col in cursor.description]
    context = {
        'joined_results': joined_results,  # Ensure this matches your template
        'columns': columns
    }
    return render(request, 'benchmarks/maintable.html', context)