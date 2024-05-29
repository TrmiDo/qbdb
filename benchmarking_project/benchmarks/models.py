from django.db import models
from django.core.exceptions import ValidationError

# Single Column Models
class Manufacturer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class EmbeddingAlgorithm(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Solver(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class TimeType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class PerformanceMetric(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

# Multi-Column Models 
class Topology(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    physical_qubits_per_cell = models.IntegerField(null=False, blank=False)
    qubit_degree = models.FloatField(null=False, blank=False)
    qubit_nominal_length = models.IntegerField(null=True, blank=True, default=None)
    max_qubo_variable_count_clique = models.IntegerField(null=True, blank=True, default=None)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Processor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    technology_id = models.ForeignKey(Technology, on_delete=models.CASCADE, null=False, blank=False)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False, blank=False)
    physical_qubits = models.IntegerField(null=True, blank=True, default=None)
    topology_id = models.ForeignKey(Topology, on_delete=models.CASCADE, null=True, blank=True, default=None)
    intro_year = models.IntegerField(null=True, blank=True, default=None)
    rep_rate = models.FloatField(null=True, blank=True, default=None)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class GateSet(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Gate(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    qubits = models.IntegerField(null=False, blank=False)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.qubits}Q {self.name}"
    
class GateSetMembership(models.Model):
    gate_set_id = models.ForeignKey(GateSet, on_delete=models.CASCADE, null=False, blank=False)
    gate_id = models.ForeignKey(Gate, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.gate_set_id.name} - {self.gate_id.qubits}Q {self.gate_id.name}"

class System(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False, blank=False)
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE, null=False, blank=False)
    intro_year = models.IntegerField(null=True, blank=True, default=None)
    gate_set_id = models.ForeignKey(GateSet, on_delete=models.CASCADE, null=True, blank=True, default=None)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Calibration(models.Model):
    system_id = models.ForeignKey(System, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(null=True, blank=True, default=None)
    eplg = models.FloatField(null=True, blank=True, default=None)
    clops = models.IntegerField(null=True, blank=True, default=None)
    median_cz_err = models.FloatField(null=True, blank=True, default=None)
    median_ecr_err = models.FloatField(null=True, blank=True, default=None)
    median_cnot_err = models.FloatField(null=True, blank=True, default=None)
    median_sx_err = models.FloatField(null=True, blank=True, default=None)
    min_1q_err = models.FloatField(null=True, blank=True, default=None)
    max_1q_err = models.FloatField(null=True, blank=True, default=None)
    typical_1q_err = models.FloatField(null=True, blank=True, default=None)
    median_1q_err = models.FloatField(null=True, blank=True, default=None)
    min_2q_err = models.FloatField(null=True, blank=True, default=None)
    max_2q_err = models.FloatField(null=True, blank=True, default=None)
    typical_2q_err = models.FloatField(null=True, blank=True, default=None)
    median_2q_err = models.FloatField(null=True, blank=True, default=None)
    median_readout_err = models.FloatField(null=True, blank=True, default=None)
    spam_err = models.FloatField(null=True, blank=True, default=None)
    mem_err_avg_d1_circuit = models.FloatField(null=True, blank=True, default=None)
    crosstalk_err_mid_circuit = models.FloatField(null=True, blank=True, default=None)
    min_T1 = models.FloatField(null=True, blank=True, default=None)
    max_T1 = models.FloatField(null=True, blank=True, default=None)
    median_T1 = models.FloatField(null=True, blank=True, default=None)
    mean_T1 = models.FloatField(null=True, blank=True, default=None)
    min_T2 = models.FloatField(null=True, blank=True, default=None)
    max_T2 = models.FloatField(null=True, blank=True, default=None)
    median_T2 = models.FloatField(null=True, blank=True, default=None)
    mean_T2 = models.FloatField(null=True, blank=True, default=None)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    
class Graph(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Problem(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    graph_size = models.IntegerField(null=False, blank=False)
    graph_id = models.ForeignKey(Graph, on_delete=models.CASCADE, null=False, blank=False)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (size={self.graph_size}, type={self.graph_id.name})"

class PerformanceReport(models.Model):
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE, null=False, blank=False)
    qubo_var_count = models.IntegerField(null=True, blank=True, default=None)
    qubo_quad_term_count = models.IntegerField(null=True, blank=True, default=None)
    system_id = models.ForeignKey(System, on_delete=models.CASCADE, null=True, blank=True, default=None)
    embedding_id = models.ForeignKey(EmbeddingAlgorithm, on_delete=models.CASCADE, null=True, blank=True, default=None)
    solver_id = models.ForeignKey(Solver, on_delete=models.CASCADE, null=True, blank=True, default=None)
    qubit_count = models.IntegerField(null=True, blank=True, default=None)
    rcs = models.FloatField(null=True, blank=True, default=None)
    mean_chain_length = models.IntegerField(null=True, blank=True, default=None)
    max_chain_length = models.IntegerField(null=True, blank=True, default=None)
    num_runs = models.IntegerField(null=True, blank=True, default=None)
    time_type_id = models.ForeignKey(TimeType, on_delete=models.CASCADE, null=True, blank=True, default=None)
    time = models.FloatField(null=True, blank=True, default=None)
    performance_metric_id = models.ForeignKey(PerformanceMetric, on_delete=models.CASCADE, null=True, blank=True, default=None)
    performance_value = models.FloatField(null=True, blank=True, default=None)
    url1 = models.URLField(max_length=200, blank=True)
    url2 = models.URLField(max_length=200, blank=True)
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.problem_id} (system={self.system_id.name}, embedding={self.embedding_id.name}, solver={self.solver_id.name})"

    def clean(self):
        super().clean()
        if self.time is not None and self.time_type_id is None:
            raise ValidationError({'time_type_id': 'Time type must be specified if time is to be provided.'})
        if self.performance_value is not None and self.performance_metric_id is None:
            raise ValidationError({'performance_metric_id': 'Performance metric type must be specified if performance value is to be provided.'})
    