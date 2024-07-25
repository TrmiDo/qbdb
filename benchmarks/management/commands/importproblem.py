import pandas as pd
from django.core.management.base import BaseCommand
from django.db import connection


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
                problem text,
                graphsize float,
                graphtype text,
                url text,
                note text

            )
            """
            cursor.execute(create_temp_table_sql)

            # Insert data from the DataFrame into the temporary table
            insert_sql = '''
            INSERT INTO temp_table (problem, graphsize, graphtype, url, note)
            VALUES (%s, %s, %s, %s, %s)
            '''
            for index, row in df.iterrows():
                try:
                    
                    problem = None if pd.isna(row['Problem']) else row['Problem']
                    graphsize = None if pd.isna(row['Graph Size']) else float(row['Graph Size'])
                    graphtype = None if pd.isna(row['Graph Type']) else row['Graph Type']
                    url = None if pd.isna(row['url']) else row['url']
                    note = None if pd.isna(row['Notes']) else row['Notes']
                    # Prepare the values tuple
                    values = (
                        problem, graphsize, graphtype, url , note)

                    
                    # Execute the SQL statement
                    cursor.execute(insert_sql, values)
                except Exception as e:
                    pass
                    print(f"Error inserting row {index}: {e}")

            cursor.execute("SELECT * FROM temp_table")
            rows = cursor.fetchall()

            check_problem_sql = 'SELECT id FROM benchmarks_problem WHERE name like %s'
            insert_problem_sql = 'INSERT INTO benchmarks_problem(name, url1, notes) values (%s, %s, %s)'

            check_graph_sql = 'SELECT id FROM benchmarks_graph WHERE name like %s'
            insert_graph_sql = 'INSERT INTO benchmarks_graph(name, url1, notes) values (%s, %s, %s)'

            check_instance_sql = '''
            SELECT id
            FROM benchmarks_probleminstance
            WHERE problem_id = %s
            and graph_id = %s
            and graph_size = %s
            '''
            insert_instance_sql = '''
                INSERT INTO benchmarks_probleminstance (problem_id, graph_id, graph_size, url1, notes)
                VALUES (%s, %s, %s, %s, %s)
            '''

            

            for row in rows:
                # Here, you can process each row and use the variables as needed
                problem = row[0]
                graphsize = row[1]
                graphtype = row[2]
                url = row[3]
                note = row[4]
                

                #Remember to set all link id to None
                problem_id = None
                graph_id = None
                

                #Problems
                if problem is not None: 
                    #Search for the item
                    cursor.execute(check_problem_sql, [problem])
                    check = cursor.fetchall()

                    #Insert if need to
                    

                    if len(check) == 0:
                        cursor.execute(insert_problem_sql, (problem,url, note))
                        print(f"New Problem: {problem}")
                        # Commit the insert if necessary
                        connection.commit()
                    
                    #Get the id for joining
                    cursor.execute(check_problem_sql, [problem])
                    problem_get_id = cursor.fetchall()

                    if problem_get_id:
                        problem_id = problem_get_id[0][0]
                    else:
                        print(f"System {problem} was not found after insertion.")


                #Graph
                if graphtype is not None: 
                    #Search for the item
                    cursor.execute(check_graph_sql, (graphtype,))
                    check = cursor.fetchall()

                    #Insert if need to
                    

                    if len(check) == 0:
                        cursor.execute(insert_graph_sql, (graphtype, url, note))
                        print(f"New Graph: {graphtype}")
                        # Commit the insert if necessary
                        connection.commit()
                    
                    #Get the id for joining
                    cursor.execute(check_graph_sql, (graphtype,))
                    graph_get_id = cursor.fetchall()

                    if graph_get_id:
                        graph_id = graph_get_id[0][0]
                    else:
                        print(f"Graph {graphtype} was not found after insertion.")
                #Graph
                # Check if the record exists
                if problem_id is not None or graph_id is not None:
                    cursor.execute(check_instance_sql, (problem_id,graph_id, graphsize))
                    check = cursor.fetchall()
                    
                    # Insert if the record does not exist
                    if len(check) < 1 :
                        cursor.execute(insert_instance_sql, (problem_id, graph_id, graphsize, url, note))
                        print(f"New: {(problem_id, graph_id, graphsize, url, note)}")
                        connection.commit()
                        
                    # Get the id for joining
                    cursor.execute(check_instance_sql, (problem_id, graph_id, graphsize))
                    instance_get_id = cursor.fetchall()
                    
                    if instance_get_id:
                        instance_id = instance_get_id[0][0]
                        print(instance_id)
                    else:
                        print(f"Instance {(problem_id, graph_id, graphsize, url, note)} was not found after insertion.")
    

                
        self.stdout.write(self.style.SUCCESS('Data loaded and joined successfully'))
