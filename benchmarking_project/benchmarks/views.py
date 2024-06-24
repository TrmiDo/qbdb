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
from django.http import HttpRequest
from .models import ErrorLog
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
        left join benchmarks_solver as b on a.solver_id =b.id
        left join benchmarks_performanceValue as c on c.performance_report_id = a.id 
        left join benchmarks_performanceMetric as d on c.metric_id= d.id
        left join benchmarks_compilationstep as e on e.performance_report_id = a.id
        left join benchmarks_compilationAlgorithmn as f on f.id= e.compilation_Algorithmn_id
        left join benchmarks_compilationTool as g on g.id = e.compilation_tool_id''')
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
        left join benchmarks_graph as b on a.graph_id =b.id
        left join benchmarks_problem as c on c.id = a.problem_id
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
        left join benchmarks_calibration as b on a.id= b.system_id
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
        left join benchmarks_manufacturer as b on a.manufacturer_id =b.id
        left join benchmarks_technology as c on c.id = a.technology_id
        left join benchmarks_topology as d on a.topology_id=d.id
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
        left join benchmarks_gatesetmembership as b on a.id =b.gate_set_id
        left join benchmarks_gate as c on c.id = b.gate_id
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


def customize(request: HttpRequest):
    
    user_columns = request.GET.getlist('columns')
    user_base = request.GET.getlist('base')
    user_joins = request.GET.getlist('joins')
    user_filter= request.GET.getlist('filter')
    

    if user_base:
        base = user_base[0]
        if base == "benchmarks_performancereport":
            basetable = "benchmarks_performanceReport as a"
        elif base == "benchmarks_system":
            basetable = "benchmarks_system as b"
        elif base == "benchmarks_gateset":
            basetable = "benchmarks_gateset as c"
        elif base == "benchmarks_probleminstance":
            basetable = "benchmarks_probleminstance as d"
    else:
        basetable = "benchmarks_performanceReport as a"

    if not user_columns or "reset" in user_columns:
        user_columns = ["*"]

    filter=[]
    if user_filter:
        for index in range(0,len(user_filter)-1,2):
            if user_filter[index+1] != '':
                filter.append(user_filter[index] + " like '%" + user_filter[index+1] + "%'")
    


    join_clauses = []
    if user_joins:
        for table in user_joins:
            if basetable == "benchmarks_performanceReport as a":
                if table == "benchmarks_solver":
                    join_clauses.append("left join benchmarks_solver as e on a.solver_id = e.id")
                elif table == "benchmarks_performanceValue":
                    join_clauses.append("left join benchmarks_performanceValue as f on f.performance_report_id = a.id")
                elif table == "benchmarks_compilationstep":
                    join_clauses.append("left join benchmarks_compilationstep as g on g.performance_report_id = a.id")
                elif table == "benchmarks_system":
                    join_clauses.append("left join benchmarks_system as h on h.id = a.system_id")
                elif table == "benchmarks_probleminstance":
                    join_clauses.append("left join benchmarks_probleminstance as i on i.id = a.problem_id")
            elif basetable == "benchmarks_system as b":
                if table == "benchmarks_performancereport":
                    join_clauses.append("left join benchmarks_performancereport as j on j.system_id = b.id")
                elif table == "benchmarks_calibration":
                    join_clauses.append("left join benchmarks_calibration as k on k.system_id = b.id")
                elif table == "benchmarks_manufacturer":
                    join_clauses.append("left join benchmarks_manufacturer as l on l.id = b.manufactor_id")
                elif table == "benchmarks_processor":
                    join_clauses.append("left join benchmarks_processor as m on m.id = b.processor_id")
                elif table == "benchmarks_gateset":
                    join_clauses.append("left join benchmarks_gateset as n on n.id = b.gateset_id")
            elif basetable == "benchmarks_gateset as c":
                if table == "benchmarks_gatesetmembership":
                    join_clauses.append("left join benchmarks_gatesetmembership as o on o.gate_set_id=c.id")
                elif table == "benchmarks_gate":
                    join_clauses.append("left join benchmarks_gate as p on p.id=o.gate_id")
            elif basetable == "benchmarks_probleminstance as d":
                if table == "benchmarks_graph":
                    join_clauses.append("left join benchmarks_graph as q on q.id = d.graph_id")
                elif table == "benchmarks_problem":
                    join_clauses.append("left join benchmarks_problem as r on r.id = d.problem_id")

    sql_query = f"SELECT {', '.join(user_columns)} FROM {basetable} {' '.join(join_clauses)} "
    if filter:
        sql_query += 'where ' + ' and '.join(filter)
    print(sql_query)


    with connection.cursor() as cursor:
        try:
            cursor.execute(sql_query)
            joined_results = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        except Exception as e:
            error_message = str(e)
            stack_trace = ""
            ErrorLog.objects.create(error_message=error_message,querycode=sql_query )
            return render(request, 'benchmarks/index.html')

    context = {
        'joined_results': joined_results,
        'columns': columns,
        'selected_columns': user_columns,
        'selected_joins': user_joins,
        'selected_base': user_base
    }
    return render(request, 'benchmarks/custom.html', context)
 
