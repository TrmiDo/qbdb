from django.db import models

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=50)
    graph_size = models.IntegerField
    graph_type = models.CharField(max_length=100)
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

    def __str__(self):
        return f"{self.name} (size={self.graph_size}, type={self.graph_type})"
    
class Topology(models.Model):
    name = models.CharField(max_length=50)
    physical_qubits_per_cell = models.IntegerField
    qubit_degree = models.IntegerField
    qubit_nominal_length = models.IntegerField
    max_qubo_variable_count_clique = models.IntegerField
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# TODO: decide which fields belong to processor and which belong to system
class Processor(models.Model):
    name = models.CharField(max_length=50)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    physical_qubits = models.IntegerField
    intro_year = models.IntegerField
    topology_id = models.ForeignKey(Topology, on_delete=models.CASCADE)
    # rep_rate = models.
    
class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class GateSet(models.Model):
    name = models.CharField(max_length=50)
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

    def __str__(self):
        return self.name
    
class Gate(models.Model):
    name = models.CharField(max_length=50)
    qubits = models.IntegerField
    is_virtual = models.BooleanField
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

    def __str__(self):
        return self.name
    
class GateSetMembership(models.Model):
    gate_set_id = models.ForeignKey(GateSet, on_delete=models.CASCADE)
    gate_id = models.ForeignKey(Gate, on_delete=models.CASCADE)

class System(models.Model):
    system_name = models.CharField(max_length=50)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology, on_delete=models.CASCADE)
    physical_qubit_count = models.IntegerField
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE)
    intro_year = models.IntegerField
    topology_id = models.ForeignKey(Topology, on_delete=models.CASCADE)
    gate_set_id = models.ForeignKey(GateSet, on_delete=models.CASCADE)
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

    def __str__(self):
        return self.system_name

class Calibration(models.Model):
    system_id = models.ForeignKey(System, on_delete=models.CASCADE)
    date = models.DateTimeField
    eplg = models.FloatField
    clops = models.IntegerField
    median_cz_err = models.FloatField
    median_ecr_err = models.FloatField
    median_cnot_err = models.FloatField
    median_sx_err = models.FloatField
    min_1q_err = models.FloatField
    max_1q_err = models.FloatField
    typical_1q_err = models.FloatField
    median_1q_err = models.FloatField
    min_2q_err = models.FloatField
    max_2q_err = models.FloatField
    typical_2q_err = models.FloatField
    median_2q_err = models.FloatField
    median_readout_err = models.FloatField
    spam_err = models.FloatField
    mem_err_avg_d1_circuit = models.FloatField
    crosstalk_err_mid_circuit = models.FloatField
    min_T1 = models.FloatField
    max_T1 = models.FloatField
    median_T1 = models.FloatField
    mean_T1 = models.FloatField
    min_T2 = models.FloatField
    max_T2 = models.FloatField
    median_T2 = models.FloatField
    mean_T2 = models.FloatField
    url1 = models.URLField(max_length=200)
    url2 = models.URLField(max_length=200)
    notes = models.TextField

class TimeType(models.Model):
    time_type = models.CharField(max_length=50)

    def __str__(self):
        return self.time_type

class PerformanceMetric(models.Model):
    performance_metric = models.CharField(max_length=50)

    def __str__(self):
        return self.performance_metric

class PerformanceReport(models.Model):
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    qubo_var_count = models.IntegerField
    qubo_quad_term_count = models.IntegerField
    system_id = models.ForeignKey(System, on_delete=models.CASCADE)
    embedding_alg = models.CharField(max_length=50)
    solver = models.CharField(max_length=50)
    qubit_count = models.IntegerField
    rcs = models.FloatField
    mean_chain_length = models.IntegerField
    max_chain_length = models.IntegerField
    num_runs = models.IntegerField
    type_type_id = models.ForeignKey(System, on_delete=models.CASCADE)
    time = models.FloatField
    performance_metric_id = models.ForeignKey(PerformanceMetric, on_delete=models.CASCADE)
    performance_value = models.FloatField
    notes = models.TextField

