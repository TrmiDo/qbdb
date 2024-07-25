class Graph:
    def __init__(self):
        self.adj_list = {}
        self.join_list = {}
        self.col_list={}
        self.join_string =''

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.join_list[vertex] =[]
            self.col_list[vertex]=[]
            self.string =''

    def add_edge(self, vertex1, vertex2, join_string):
        if vertex1 in self.adj_list and vertex2 in self.adj_list and (vertex1 not in self.adj_list[vertex2] and vertex2 not in self.adj_list[vertex1] ):
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            self.join_list[vertex1].append(join_string)
            self.join_list[vertex2].append(join_string)
    def add_col(self,vertex,columns):
        if vertex in self.adj_list:
            self.col_list[vertex]= columns

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 in self.adj_list[vertex1]:
                self.adj_list[vertex1].remove(vertex2)
            if vertex1 in self.adj_list[vertex2]:
                self.adj_list[vertex2].remove(vertex1)

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

        print("__________________________________________________________")
        for vertex in self.join_list:
            print(f"{vertex}: {self.join_list[vertex]}")

    def getcol(self,vertexlist):
        col=[]
        existcol=[]
        for vertex in vertexlist:
            if vertex not in existcol:
                col.extend(self.col_list[vertex])
                existcol.append(vertex)
        return col


    #Getting all the connection
    def connect_all(self, vertexlist):
        col=[]
        #print(vertexlist)
        def dfs(graph, start, visited=None, join= '', column_list = []):
            if visited is None:
                visited = set()
    
            visited.add(start)
            #print("CURRENT: "+start)
            #print("CURRENT STRING: "+join)
            #print("\n")
            signal= False

    
            for neighbor in graph[start]:
                test_join= f" full join {neighbor} on {self.join_list[neighbor][self.adj_list[neighbor].index(start)]} \n"
                #print(signal)
                if neighbor in vertexlist:
                    if signal:
                        self.join_string += test_join
                    else:
                        col.extend(column_list)
                        self.join_string += join + test_join
                    #print("SO FAR:\n"+self.join_string)
                    col.append(neighbor)
                    vertexlist.remove(neighbor)
                    signal= True
                    test_join=''
    
                if neighbor not in visited:
                    if signal:
                        nextsignal = dfs(graph, neighbor, visited, test_join, [neighbor])
                    else:
                        tempcolumnlist = column_list + [neighbor]
                        nextsignal = dfs(graph, neighbor, visited, join + test_join, tempcolumnlist)
                    if signal or nextsignal:
                        signal= True
            return signal



        if vertexlist: 
            self.join_string = vertexlist[0] + "\n"
            col.append(vertexlist[0])
            start = vertexlist[0]
            vertexlist.remove(vertexlist[0])
            dfs(self.adj_list,start)
            #print(self.join_string)

            return self.getcol(col), self.join_string
        else:
             return None , None







graph = Graph()

graph.add_vertex('benchmarks_manufacturer')
graph.add_vertex('benchmarks_technology')
graph.add_vertex('benchmarks_solver')
graph.add_vertex('benchmarks_performancemetric')
graph.add_vertex('benchmarks_compilationtool')
graph.add_vertex('benchmarks_compilationalgorithmn')
graph.add_vertex('benchmarks_topology')
graph.add_vertex('benchmarks_processor')
graph.add_vertex('benchmarks_gateset')
graph.add_vertex('benchmarks_gate')
graph.add_vertex('benchmarks_gatesetmembership')
graph.add_vertex('benchmarks_system')
graph.add_vertex('benchmarks_calibration')
graph.add_vertex('benchmarks_graph')
graph.add_vertex('benchmarks_problem')
graph.add_vertex('benchmarks_probleminstance')
graph.add_vertex('benchmarks_performancereport')
graph.add_vertex('benchmarks_compilationstep')
graph.add_vertex('benchmarks_performancevalue')

graph.add_edge('benchmarks_manufacturer', 'benchmarks_system', 'benchmarks_manufacturer.id = benchmarks_system.manufactor_id')
graph.add_edge('benchmarks_manufacturer', 'benchmarks_processor', 'benchmarks_manufacturer.id = benchmarks_processor.manufacturer_id')

graph.add_edge('benchmarks_technology', 'benchmarks_processor', 'benchmarks_technology.id = benchmarks_processor.technology_id')

graph.add_edge('benchmarks_solver', 'benchmarks_performanceReport', 'benchmarks_solver.id= benchmarks_performanceReport.solver_id')

graph.add_edge('benchmarks_performancemetric', 'benchmarks_performancevalue', 'benchmarks_performancemetric.id = benchmarks_performancevalue.metric_id')

graph.add_edge('benchmarks_compilationtool', 'benchmarks_compilationstep', 'benchmarks_compilationtool.id = benchmarks_compilationstep.compilation_tool_id')

graph.add_edge('benchmarks_compilationalgorithmn', 'benchmarks_compilationstep', 'benchmarks_compilationalgorithmn.id = benchmarks_compilationstep.compilation_algorithmn_id')

graph.add_edge('benchmarks_topology', 'benchmarks_processor', 'benchmarks_topology.id = benchmarks_processor.topology_id')

graph.add_edge('benchmarks_processor', 'benchmarks_manufacturer', 'benchmarks_manufacturer.id = benchmarks_processor.manufacturer_id')
graph.add_edge('benchmarks_processor', 'benchmarks_technology', 'benchmarks_technology.id = benchmarks_processor.technology_id')
graph.add_edge('benchmarks_processor', 'benchmarks_topology', 'benchmarks_topology.id = benchmarks_processor.topology_id')
graph.add_edge('benchmarks_processor', 'benchmarks_system', 'benchmarks_processor.id = benchmarks_system.processor_id' )

graph.add_edge('benchmarks_gateset', 'benchmarks_gatsetmembership', 'benchmarks_gateset.id = benchmarks_gatsetmembership.gate_set_id')
graph.add_edge('benchmarks_gateset', 'benchmarks_system', 'benchmarks_gateset.id = benchmarks_system.gate_set_id')

graph.add_edge('benchmarks_gatesetmembership', 'benchmarks_gateset', 'benchmarks_gateset.id = benchmarks_gatesetmembership.gate_set_id')
graph.add_edge('benchmarks_gatesetmembership', 'benchmarks_gate', 'benchmarks_gatesetmembership.gate_id= benchmarks_gate.id')

graph.add_edge('benchmarks_gate', 'benchmarks_gatesetmembership', 'benchmarks_gatesetmembership.gate_id= benchmarks_gate.id')

graph.add_edge('benchmarks_system', 'benchmarks_manufacturer', 'benchmarks_manufacturer.id = benchmarks_system.manufactor_id')
graph.add_edge('benchmarks_system', 'benchmarks_processor', 'benchmarks_processor.id = benchmarks_system.processor_id')
graph.add_edge('benchmarks_system', 'benchmarks_gateset', 'benchmarks_gateset.id = benchmarks_system.gate_set_id')
graph.add_edge('benchmarks_system', 'benchmarks_calibration', 'benchmarks_system.id = benchmarks_calibration.system_id')
graph.add_edge('benchmarks_system', 'benchmarks_performancereport', 'benchmarks_system.id = benchmarks_performancereport.system_id')

graph.add_edge('benchmarks_calibration', 'benchmarks_system', 'benchmarks_system.id = benchmarks_calibration.system_id')

graph.add_edge('benchmarks_graph', 'benchmarks_probleminstance', 'benchmarks_graph.id = benchmarks_probleminstance.graph_id')

graph.add_edge('benchmarks_problem', 'benchmarks_probleminstance', 'benchmarks_problem.id = benchmarks_probleminstance.problem_id')

graph.add_edge('benchmarks_probleminstance', 'benchmarks_graph', 'benchmarks_graph.id = benchmarks_probleminstance.graph_id')
graph.add_edge('benchmarks_probleminstance', 'benchmarks_problem', 'benchmarks_problem.id = benchmarks_probleminstance.problem_id')
graph.add_edge('benchmarks_probleminstance', 'benchmarks_performancereport', 'benchmarks_probleminstance.id = benchmarks_performancereport.problem_id')

graph.add_edge('benchmarks_performancereport', 'benchmarks_solver', 'benchmarks_performancereport.solver_id = benchmarks_solver.id')
graph.add_edge('benchmarks_performancereport', 'benchmarks_system', 'benchmarks_performancereport.system_id = benchmarks_system.id')
graph.add_edge('benchmarks_performancereport', 'benchmarks_probleminstance', 'benchmarks_probleminstance.id = benchmarks_performancereport.problem_id')
graph.add_edge('benchmarks_performancereport' ,'benchmarks_compilationstep', 'benchmarks_performancereport.id= benchmarks_compilationstep.performance_report_id')
graph.add_edge('benchmarks_performancereport', 'benchmarks_performancevalue', 'benchmarks_performancereport.id = benchmarks_performancevalue.performance_report_id')

graph.add_edge('benchmarks_compilationstep', 'benchmarks_performancereport', 'benchmarks_performancereport.id= benchmarks_compilationstep.performance_report_id')
graph.add_edge('benchmarks_compilationstep', 'benchmarks_compilationtool', 'benchmarks_compilationtool.id = benchmarks_compilationstep.compilation_tool_id')
graph.add_edge('benchmarks_compilationstep', 'benchmarks_compliationalgorithmn', 'benchmarks_compliationalgorithmn.id = benchmarks_compilationstep.compilation_algorithmn_id')

graph.add_edge('benchmarks_performancevalue', 'benchmarks_performancereport', 'benchmarks_performancereport.id = benchmarks_performancevalue.performance_report_id')
graph.add_edge('benchmarks_performancevalue', 'benchmarks_performancemetric','benchmarks_performancemetric.id = benchmarks_performancevalue.metric_id' )


graph.add_col('benchmarks_manufacturer',['benchmarks_manufacturer.name'])
graph.add_col('benchmarks_technology',['benchmarks_technology.name'])
graph.add_col('benchmarks_solver',['benchmarks_solver.name'])
graph.add_col('benchmarks_performancemetric',['benchmarks_performancemetric.name'])
graph.add_col('benchmarks_compilationtool',['benchmarks_compilationtool.name'])
graph.add_col('benchmarks_compilationalgorithmn',['benchmarks_compilationalgorithmn.name'])
graph.add_col('benchmarks_topology',['benchmarks_topology.name','benchmarks_topology.physical_qubits_per_cell','benchmarks_topology.qubit_degree','benchmarks_topology.qubit_nominal_length','benchmarks_topology.max_qubo_variable_count_clique','benchmarks_topology.url1','benchmarks_topology.url2','benchmarks_topology.notes'])
graph.add_col('benchmarks_processor',['benchmarks_processor.name','benchmarks_processor.physical_qubits','benchmarks_processor.intro_year','benchmarks_processor.rep_rate','benchmarks_processor.url1','benchmarks_processor.url2','benchmarks_processor.notes'])
graph.add_col('benchmarks_gateset',['benchmarks_gateset.name','benchmarks_gateset.url1','benchmarks_gateset.url2','benchmarks_gateset.notes'])
graph.add_col('benchmarks_gate',['benchmarks_gate.name ','benchmarks_gate.qubits','benchmarks_gate.url1','benchmarks_gate.url2','benchmarks_gate.notes'])
graph.add_col('benchmarks_gatesetmembership',[])
graph.add_col('benchmarks_system',['benchmarks_system.name','benchmarks_system.intro_year','benchmarks_system.url1','benchmarks_system.url2','benchmarks_system.notes'])
graph.add_col('benchmarks_calibration',['benchmarks_calibration.date','benchmarks_calibration.eplg','benchmarks_calibration.clops','benchmarks_calibration.median_cz_err','benchmarks_calibration.median_ecr_err','benchmarks_calibration.median_cnot_err','benchmarks_calibration.median_sx_err','benchmarks_calibration.min_1q_err','benchmarks_calibration.min_2q_err','benchmarks_calibration.max_2q_err','benchmarks_calibration.typical_2q_err','benchmarks_calibration.median_2q_err','benchmarks_calibration.median_readout_err','benchmarks_calibration.spam_err','benchmarks_calibration.mem_err_avg_d1_circuit','benchmarks_calibration.crosstalk_err_mid_circuit','benchmarks_calibration.min_t1','benchmarks_calibration.max_t1','benchmarks_calibration.median_t1','benchmarks_calibration.mean_t1','benchmarks_calibration.min_t2','benchmarks_calibration.max_t2','benchmarks_calibration.median_t2','benchmarks_calibration.mean_t2','benchmarks_calibration.url1','benchmarks_calibration.url2','benchmarks_calibration.notes'])
graph.add_col('benchmarks_graph',['benchmarks_graph.name','benchmarks_graph.url1','benchmarks_graph.url2','benchmarks_graph.notes'])
graph.add_col('benchmarks_problem',['benchmarks_problem.name','benchmarks_problem.url1','benchmarks_problem.url2','benchmarks_problem.notes'])
graph.add_col('benchmarks_probleminstance',['benchmarks_probleminstance.graph_size','benchmarks_probleminstance.url1','benchmarks_probleminstance.url2','benchmarks_probleminstance.notes'])
graph.add_col('benchmarks_performancereport',['benchmarks_performancereport.id','benchmarks_performancereport.qubo_var_count','benchmarks_performancereport.qubo_quad_term_count','benchmarks_performancereport.qubit_count','benchmarks_performancereport.rcs','benchmarks_performancereport.mean_chain_length','benchmarks_performancereport.max_chain_length','benchmarks_performancereport.num_runs','benchmarks_performancereport.url1','benchmarks_performancereport.url2','benchmarks_performancereport.notes'])
graph.add_col('benchmarks_compilationstep',['benchmarks_compilationstep.version'])
graph.add_col('benchmarks_performancevalue',['benchmarks_performancevalue.value'])



#print(graph.connect_all(['benchmarks_manufacturer a', 'benchmarks_solver c', 'benchmarks_performancemetric d','benchmarks_performancereport q']))







'''
benchmarks_manufacturer a
    name
benchmarks_technology b
    name
benchmarks_solver c
    name
benchmarks_performancemetric d
    name
benchmarks_compilationtool e
    name
benchmarks_compilationalgorithmn f
    name
benchmarks_topology g
    name
    physical_qubits_per_cel
    qubit_degree
    qubit_nominal_length
    max_qubo_variable_count_clique
    url1
    url2
    notes
benchmarks_processor h
    name
    physical_qubits
    intro_year
    rep_rate
    url1
    url2
    notes
benchmarks_gateset i
    name
    url1
    url2
    notes
benchmarks_gate j
    name
    qubits
    url1
    url2
    notes
benchmarks_gatesetmembership k
    _
benchmarks_system l
    name
    intro_year
    url1
    url2
    notes
benchmarks_calibration m
    date
    eplg
    clops
    median_cz_err
    median_ecr_err
    median_cnot_err
    median_cx_err
    min_1q_err
    min_2q_err
    max_2q_err
    typical_2q_err
    median_2q_err
    median_readout_err
    spam_err
    mem_err_avg_d1_circuit
    crosstalk_err_mid_circuit
    min_T1
    max_T1
    median_T1
    mean_T1
    min_T2
    max_T2
    median_T2
    mean_T2
    url1
    url2
    notes
benchmarks_graph n
    name
    url1
    url2
    notes
benchmarks_problem o
    name
    url1
    url2
    notes
benchmarks_probleminstance p
    graph_size
    url1
    url2
    notes
benchmarks_performancereport q
    qubo_var_count
    qubo_quad_term_count
    qubit_count
    rcs
    mean_chain_length
    max_chain_length
    num_runs
    url1
    url2
    notes
benchmarks_compilationstep r
    version
benchmarks_performancevalue s
    value
'''
