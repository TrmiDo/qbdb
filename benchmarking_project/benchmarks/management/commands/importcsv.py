import pandas as pd
from django.core.management.base import BaseCommand
from django.db import connection
from benchmarks.models import ProblemInstance, Graph, Problem

class Command(BaseCommand):
    help = 'Load data from CSV file and join with existing tables'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Connect to the SQLite database
        with connection.cursor() as cursor:
             # Create a temporary table
            create_temp_table_sql = """
            CREATE TEMPORARY TABLE temp_table (
                id INTEGER,
                problemid INTEGER,
                qubo INTEGER,
                system_name TEXT,
                embedding_algorithm TEXT,
                solver TEXT,
                url TEXT,
                qubits INTEGER,
                rcs FLOAT,
                number_of_runs INTEGER,
                time_type TEXT,
                time FLOAT,
                performance_metric TEXT,
                performance_value FLOAT,
                notes TEXT

            )
            """
            cursor.execute(create_temp_table_sql)

            # Insert data from the DataFrame into the temporary table
            insert_sql = '''
            INSERT INTO temp_table (id, problemid, qubo, system_name, embedding_algorithm, solver, url, qubits, rcs, number_of_runs, time_type, time, performance_metric, performance_value, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            for index, row in df.iterrows():
                try:
                    problemid = None if pd.isna(row['Problem ID']) else int(row['Problem ID'])
                    qubo = None if pd.isna(row['QUBO Variables']) else int(row['QUBO Variables'])
                    system_name = None if pd.isna(row['System Name']) else (row['System Name'])
                    embedding_algorithm = None if pd.isna(row['Embedding Algorithm']) else (row['Embedding Algorithm'])
                    solver = None if pd.isna(row['Solver']) else (row['Solver'])
                    url = None if pd.isna(row['URL']) else (row['URL'])
                    qubits = None if pd.isna(row['Qubits']) else int(row['Qubits'])
                    rcs = None if pd.isna(row['RCS']) else float(row['RCS'])
                    number_of_runs = None if pd.isna(row['Number of Runs']) else int(row['Number of Runs'])
                    time_type = None if pd.isna(row['Time Type']) else (row['Time Type'])
                    time = None if pd.isna(row['Time']) else float(row['Time'])
                    performance_metric = None if pd.isna(row['Performance Metric']) else (row['Performance Metric'])
                    performance_value = None if pd.isna(row['Performance Value']) else float(row['Performance Value'])
                    notes = None if pd.isna(row['Notes']) else (row['Notes'])
                    # Prepare the values tuple
                    values = (
                        int(row['ID']), problemid, qubo, system_name, embedding_algorithm, solver, url, qubits, rcs, number_of_runs, time_type, time, performance_metric, performance_value,notes
                    )

                    
                    # Execute the SQL statement
                    cursor.execute(insert_sql, values)
                except Exception as e:
                    pass
                    #print(f"Error inserting row {index}: {e}")

            cursor.execute("SELECT * FROM temp_table")
            rows = cursor.fetchall()

            check_system_sql = 'SELECT id FROM benchmarks_system WHERE name = %s'
            insert_system_sql = 'INSERT INTO benchmarks_system(name) values (%s)'

            check_algorithm_sql = 'SELECT id FROM benchmarks_CompilationAlgorithmn WHERE name = %s'
            insert_algorithm_sql = 'INSERT INTO benchmarks_CompilationAlgorithmn(name) values (%s)'

            check_solver_sql = 'SELECT id FROM benchmarks_solver WHERE name = %s'
            insert_solver_sql = 'INSERT INTO benchmarks_solver(name) values (%s)'

            check_metric_sql = 'SELECT id FROM benchmarks_PerformanceMetric WHERE name = %s'
            insert_metric_sql = 'INSERT INTO benchmarks_PerformanceMetric(name) values (%s)'

            check_latest_report_sql = 'Select max(id) from benchmarks_performancereport'
            insert_report_sql = '''INSERT INTO benchmarks_performancereport
            (problem_id,
            qubo_var_count,
            system_id,
            solver_id,
            qubit_count,
            rcs,
            num_runs,
            url1,
            notes)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''

            insert_value_sql = '''INSERT INTO benchmarks_PerformanceValue
            (metric_id,
            value,
            performance_report_id)
            values(?,?,?)
            '''

            insert_compilation_sql = '''INSERT INTO benchmarks_CompilationStep
            (compilation_algorithmn_id,
            performance_report_id)
            values(?,?)
            '''

            system_id = None
            embedding_algorithm_id = None
            solver_id = None
            time_id = None
            metric_id = None
            for row in rows:
                # Here, you can process each row and use the variables as needed
                current = row[0]
                problemid = row[1]
                qubo = row[2]
                system_name = row[3]
                embedding_algorithm = row[4]
                solver = row[5]
                url = row[6]
                qubits = row[7]
                rcs = row[8]
                number_of_runs = row[9]
                time_type = row[10]
                time = row[11]
                performance_metric = row[12]
                performance_value = row[13]
                notes = row[14]

                cursor.execute(check_system_sql, [system_name])
                check = cursor.fetchall()

                #System
                if len(check) != 1 and system_name is not None:
                    cursor.execute(insert_system_sql, (system_name,))
                    print(f"New System: {system_name}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_system_sql, (system_name,))
                system_get_id = cursor.fetchall()

                if system_get_id and system_name is not None:
                    system_id = system_get_id[0][0]
                elif system_name is None:
                    pass
                else:
                    print(f"System {system_name} was not found after insertion.")
                
                #Algorithm
                cursor.execute(check_algorithm_sql, [embedding_algorithm])
                check = cursor.fetchall()

                if len(check) != 1 and embedding_algorithm is not None:
                    cursor.execute(insert_algorithm_sql, (embedding_algorithm,))
                    print(f"New Algorithm: {embedding_algorithm}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_algorithm_sql, (embedding_algorithm,))
                algorithm_get_id = cursor.fetchall()

                if algorithm_get_id and embedding_algorithm is not None:
                    embedding_algorithm_id = algorithm_get_id[0][0]
                elif embedding_algorithm is None:
                    pass
                else:
                    print(f"Algo {embedding_algorithm} was not found after insertion.")

                #Solver
                cursor.execute(check_solver_sql, [solver])
                check = cursor.fetchall()

                if len(check) != 1 and solver is not None:
                    cursor.execute(insert_solver_sql, (solver,))
                    print(f"New Solver: {solver}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_solver_sql, (solver,))
                solver_get_id = cursor.fetchall()

                if solver_get_id and solver is not None:
                    solver_id = solver_get_id[0][0]
                elif solver is None:
                    pass
                else:
                    print(f"Solver {solver} was not found after insertion.")

                #Time Type
                cursor.execute(check_metric_sql, [time_type])
                check = cursor.fetchall()

                if len(check) != 1 and time_type is not None:
                    cursor.execute(insert_metric_sql, (time_type,))
                    print(f"New Metric: {time_type}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_metric_sql, (time_type,))
                time_type_get_id = cursor.fetchall()

                if time_type_get_id and time_type is not None:
                    time_id = time_type_get_id[0][0]
                elif time_type is None:
                    pass
                else:
                    print(f"Time {time_type} was not found after insertion.")
                
                #Metric
                cursor.execute(check_metric_sql, [performance_metric])
                check = cursor.fetchall()

                if len(check) != 1 and performance_metric is not None:
                    cursor.execute(insert_metric_sql, (performance_metric,))
                    print(f"New Metric: {performance_metric}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_metric_sql, (performance_metric,))
                performance_metric_get_id = cursor.fetchall()

                if performance_metric_get_id and performance_metric is not None:
                    metric_id = performance_metric_get_id[0][0]
                elif performance_metric is None:
                    pass
                else:
                    print(f"Metric {time_type} was not found after insertion.")
                #print(f"Row: {current}, problem: {problemid}, qubo: {qubo}, system: {system_id}, algo: {embedding_algorithm_id}, solver: {solver_id} url: {url}, qubit: {qubits}, rcs: {rcs}, number_of_run: {number_of_runs}, time_type: {time_id}, time: {time}, metric: {metric_id}, value: {performance_value}, notes: {notes} ")
                #DO NOT INSERT WITHOUT GETTING THE LATEST ID
                #Insert Report
                cursor.execute(insert_report_sql, (problemid, qubo, system_id, solver_id, qubits, rcs, number_of_runs, url, notes, ))

                #Get latest report
                cursor.execute(check_latest_report_sql)
                report_get_id = cursor.fetchall()

                report_id = report_get_id[0][0]
                report_id = None if pd.isna(report_id) else int(report_id)
                metric_id = None if pd.isna(metric_id) else int(metric_id)
                time_id = None if pd.isna(time_id) else int(time_id)
                time = None if pd.isna(time) else float(time)
                performance_value = None if pd.isna(performance_value) else float(performance_value)
                embedding_algorithm_id = None if pd.isna(embedding_algorithm_id) else int(embedding_algorithm_id)
                #INSERT Value metric
                try:

                    if performance_value is not None:
                        cursor.execute(insert_value_sql, (metric_id, performance_value, report_id, ))
                except Exception as e:
                    pass
                #INSERT Value time
                try:
                    if time is not None:
                        cursor.execute(insert_value_sql, (time_id, time, report_id, ))
                except Exception as e:
                    pass
                
                try:
                    if embedding_algorithm_id is not None:
                        cursor.execute(insert_compilation_sql , (embedding_algorithm_id, report_id, ))
                except Exception as e:
                    pass

                system_id = None
                embedding_algorithm_id = None
                solver_id = None
                time_id = None
                metric_id = None


        self.stdout.write(self.style.SUCCESS('Data loaded and joined successfully'))
