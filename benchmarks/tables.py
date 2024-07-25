import django_tables2 as tables
from .models import Manufacturer ,Technology,Solver,PerformanceMetric,Topology,Processor,GateSet,Gate,GateSetMembership,System,Calibration,Graph,Problem,PerformanceReport
from .models import CompilationTool, CompilationAlgorithmn, CompilationStep, PerformanceValue, ProblemInstance


class CompilationToolTable(tables.Table):
    class Meta:
        model = CompilationTool
        template_name = "django_tables2/bootstrap.html"

class CompilationAlgorithmnTable(tables.Table):
    class Meta:
        model = CompilationAlgorithmn
        template_name = "django_tables2/bootstrap.html"

class CompilationStepTable(tables.Table):
    class Meta:
        model = CompilationStep
        template_name = "django_tables2/bootstrap.html"

class PerformanceValueTable(tables.Table):
    class Meta:
        model = PerformanceValue
        template_name = "django_tables2/bootstrap.html"

class ProblemInstanceTable(tables.Table):
    class Meta:
        model = ProblemInstance
        template_name = "django_tables2/bootstrap.html"

class ManufacturerTable(tables.Table):
    class Meta:
        model = Manufacturer
        template_name = "django_tables2/bootstrap.html"

class TechnologyTable(tables.Table):
    class Meta:
        model = Technology
        template_name = "django_tables2/bootstrap.html"

class SolverTable(tables.Table):
    class Meta:
        model = Solver
        template_name = "django_tables2/bootstrap.html"

class PerformanceMetricTable(tables.Table):
    class Meta:
        model = PerformanceMetric
        template_name = "django_tables2/bootstrap.html"
class TopologyTable(tables.Table):
    class Meta:
        model = Topology
        template_name = "django_tables2/bootstrap.html"
class ProcessorTable(tables.Table):
    class Meta:
        model = Processor
        template_name = "django_tables2/bootstrap.html"
class GateSetTable(tables.Table):
    class Meta:
        model = GateSet
        template_name = "django_tables2/bootstrap.html"
class GateSetMembershipTable(tables.Table):
    class Meta:
        model = GateSetMembership
        template_name = "django_tables2/bootstrap.html"
class SystemTable(tables.Table):
    class Meta:
        model = System
        template_name = "django_tables2/bootstrap.html"
class CalibrationTable(tables.Table):
    class Meta:
        model = Calibration
        template_name = "django_tables2/bootstrap.html"
class GraphTable(tables.Table):
    class Meta:
        model = Graph
        template_name = "django_tables2/bootstrap.html"
class ProblemTable(tables.Table):
    class Meta:
        model = Problem
        template_name = "django_tables2/bootstrap.html"
class PerformanceReportTable(tables.Table):
    class Meta:
        model = PerformanceReport
        template_name = "django_tables2/bootstrap.html"
class GateTable(tables.Table):
    class Meta:
        model = Gate
        template_name = "django_tables2/bootstrap.html"
# Repeat similar setup for other models
