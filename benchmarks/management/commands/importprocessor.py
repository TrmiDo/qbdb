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
                SystemName TEXT,
                Manufacturer TEXT,
                PhysicalQubits INTEGER,
                ProcessorType TEXT,
                Technology TEXT,
                YearOfIntro INTEGER,
                Topology TEXT,
                CLOPS INTEGER,
                MedianCZError FLOAT,
                MedianECRError FLOAT,
                MedianCNOTError FLOAT,
                MedianSXError FLOAT,
                MinSingleQubitGateError FLOAT,
                MaxSingleQubitGateError FLOAT,
                TypicalSingleQubitGateError FLOAT,
                MedianSingleQubitGateError FLOAT,
                MinTwoQubitGateError FLOAT,
                MaxTwoQubitGateError FLOAT,
                TypicalTwoQubitGateError FLOAT,
                MedianTwoQubitGateError FLOAT,
                MedianReadoutError FLOAT,
                SPAMError FLOAT,
                MemoryErrorPerQubitAtAverageDepth1Circuit FLOAT,
                MidCircuitMeasurementCrossTalkError FLOAT,
                MinT1 FLOAT,
                MaxT1 FLOAT,
                MedianT1 FLOAT,
                MeanT1 FLOAT,
                MinT2 FLOAT,
                MaxT2 FLOAT,
                MedianT2 FLOAT,
                MeanT2 FLOAT,
                TwoQubitGates TEXT,
                OneQubitGates TEXT,
                Notes TEXT,
                Url TEXT


            )
            """
            cursor.execute(create_temp_table_sql)

            # Insert data from the DataFrame into the temporary table
    
            insert_sql = '''
            INSERT INTO temp_table (
                systemName, manufacturer, physicalQubits, processorType, technology, yearOfIntro, topology, clops,
                medianCZError, medianECRError, medianCNOTError, medianSXError, minSingleQubitGateError, maxSingleQubitGateError,
                typicalSingleQubitGateError, medianSingleQubitGateError, minTwoQubitGateError, maxTwoQubitGateError,
                typicalTwoQubitGateError, medianTwoQubitGateError, medianReadoutError, spamError, memoryErrorPerQubitAtAverageDepth1Circuit,
                midCircuitMeasurementCrossTalkError, minT1, maxT1, medianT1, meanT1, minT2, maxT2, medianT2, meanT2, twoQubitGates,
                oneQubitGates, notes, url
            ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

            '''

            for index, row in df.iterrows():
                try:
                    systemName = None if pd.isna(row['System Name']) else row['System Name']
                    manufacturer = None if pd.isna(row['Manufacturer']) else row['Manufacturer']
                    physicalQubits = None if pd.isna(row['Physical Qubits']) else int(row['Physical Qubits'])
                    processorType = None if pd.isna(row['Processor Type']) else row['Processor Type']
                    technology = None if pd.isna(row['Technology']) else row['Technology']
                    yearOfIntro = None if pd.isna(row['Year of Intro']) else int(row['Year of Intro'])
                    topology = None if pd.isna(row['Topology']) else row['Topology']
                    clops = None if pd.isna(row['CLOPS']) else float(row['CLOPS'])
                    medianCZError = None if pd.isna(row['Median CZ Error']) else float(row['Median CZ Error'])
                    medianECRError = None if pd.isna(row['Median ECR Error']) else float(row['Median ECR Error'])
                    medianCNOTError = None if pd.isna(row['Median CNOT error']) else float(row['Median CNOT error'])
                    medianSXError = None if pd.isna(row['Median SX Error']) else float(row['Median SX Error'])
                    minSingleQubitGateError = None if pd.isna(row['Min Single-Qubit Gate Error']) else float(row['Min Single-Qubit Gate Error'])
                    maxSingleQubitGateError = None if pd.isna(row['Max Single-Qubit Gate Error']) else float(row['Max Single-Qubit Gate Error'])
                    typicalSingleQubitGateError = None if pd.isna(row['Typical Single-Qubit Gate Error']) else float(row['Typical Single-Qubit Gate Error'])
                    medianSingleQubitGateError = None if pd.isna(row['Median Single-Qubit Gate Error']) else float(row['Median Single-Qubit Gate Error'])
                    minTwoQubitGateError = None if pd.isna(row['Min Two-Qubit Gate Error']) else float(row['Min Two-Qubit Gate Error'])
                    maxTwoQubitGateError = None if pd.isna(row['Max Two-Qubit Gate Error']) else float(row['Max Two-Qubit Gate Error'])
                    typicalTwoQubitGateError = None if pd.isna(row['Typical Two-Qubit Gate Error']) else float(row['Typical Two-Qubit Gate Error'])
                    medianTwoQubitGateError = None if pd.isna(row['Median Two-Qubit Gate Error']) else float(row['Median Two-Qubit Gate Error'])
                    medianReadoutError = None if pd.isna(row['Median Readout Error']) else float(row['Median Readout Error'])
                    spamError = None if pd.isna(row['SPAM Error']) else float(row['SPAM Error'])
                    memoryErrorPerQubitAtAverageDepth1Circuit = None if pd.isna(row['Memory Error Per Qubit at Average Depth-1 Circuit']) else float(row['Memory Error Per Qubit at Average Depth-1 Circuit'])
                    midCircuitMeasurementCrossTalkError = None if pd.isna(row['Mid-Circuit Measurement Cross-Talk Error']) else float(row['Mid-Circuit Measurement Cross-Talk Error'])
                    minT1 = None if pd.isna(row['Min T1']) else float(row['Min T1'])
                    maxT1 = None if pd.isna(row['Max T1']) else float(row['Max T1'])
                    medianT1 = None if pd.isna(row['Median T1']) else float(row['Median T1'])
                    meanT1 = None if pd.isna(row['Mean T1']) else float(row['Mean T1'])
                    minT2 = None if pd.isna(row['Min T2']) else float(row['Min T2'])
                    maxT2 = None if pd.isna(row['Max T2']) else float(row['Max T2'])
                    medianT2 = None if pd.isna(row['Median T2']) else float(row['Median T2'])
                    meanT2 = None if pd.isna(row['Mean T2']) else float(row['Mean T2'])
                    twoQubitGates = None if pd.isna(row['Two Qubit Gates']) else row['Two Qubit Gates']
                    oneQubitGates = None if pd.isna(row['One Qubit Gates']) else row['One Qubit Gates']
                    notes = None if pd.isna(row['Notes']) else row['Notes']
                    url = None if pd.isna(row['url']) else row['url']
                    
                    values = (
                        systemName,
                        manufacturer, 
                        physicalQubits, 
                        processorType, 
                        technology, 
                        yearOfIntro, 
                        topology, 
                        clops, 
                        medianCZError, 
                        medianECRError, 
                        medianCNOTError, 
                        medianSXError, 
                        minSingleQubitGateError, 
                        maxSingleQubitGateError, 
                        typicalSingleQubitGateError, 
                        medianSingleQubitGateError, 
                        minTwoQubitGateError, 
                        maxTwoQubitGateError, 
                        typicalTwoQubitGateError, 
                        medianTwoQubitGateError, 
                        medianReadoutError, 
                        spamError, 
                        memoryErrorPerQubitAtAverageDepth1Circuit, 
                        midCircuitMeasurementCrossTalkError, 
                        minT1, 
                        maxT1, 
                        medianT1, 
                        meanT1, 
                        minT2, 
                        maxT2, 
                        medianT2, 
                        meanT2, 
                        twoQubitGates, 
                        oneQubitGates, 
                        notes, 
                        url
                    )
                    
                    cursor.execute(insert_sql, values)
                except Exception as e:
                    print(f"Error inserting row {index}: {e}")

            cursor.execute("SELECT * FROM temp_table")
            rows = cursor.fetchall()

            #Pre-build script for checking and inserting

            check_manufacturer_sql = 'SELECT id FROM benchmarks_manufacturer WHERE name like %s'
            insert_manufacturer_sql = 'INSERT INTO benchmarks_manufacturer(name) values (%s)'

            check_technology_sql = 'SELECT id FROM benchmarks_technology WHERE name like %s'
            insert_technology_sql = 'INSERT INTO benchmarks_technology(name) values (%s)'

            check_topology_sql = 'SELECT id FROM benchmarks_topology WHERE name like %s'
            insert_topology_sql = 'INSERT INTO benchmarks_topology(name) values (%s)'


            check_processor_sql = 'SELECT id FROM benchmarks_processor WHERE name like %s'
            insert_processor_sql = 'INSERT INTO benchmarks_processor(name, technology_id, manufacturer_id, physical_qubits, topology_id, intro_year, url1, notes ) values (%s,%s,%s,%s,%s,%s,%s,%s)'

            check_gateset_sql = 'SELECT id FROM benchmarks_gateset WHERE name like %s'
            insert_gateset_sql = 'INSERT INTO benchmarks_gateset(name) values (%s)'

            check_system_sql = 'SELECT id FROM benchmarks_system WHERE name like %s'
            insert_system_sql = 'INSERT INTO benchmarks_system(name, manufactor_id, processor_id, intro_year, gate_set_id, url1, notes) values (%s,%s,%s,%s,%s,%s,%s)'

            #Please look into callibration, duplication? Right now, I use the information from system
            #check_metric_sql = 'SELECT id FROM benchmarks_PerformanceMetric WHERE name like %s'
            insert_calibration_sql = '''INSERT INTO benchmarks_calibration(
                system_id,
                clops,
                median_cz_err,
                median_ecr_err,
                median_cnot_err,
                median_sx_err,
                min_1q_err,
                max_1q_err,
                typical_1q_err,
                median_1q_err,
                min_2q_err,
                max_2q_err,
                typical_2q_err,
                median_2q_err,
                median_readout_err,
                spam_err,
                mem_err_avg_d1_circuit,
                crosstalk_err_mid_circuit,
                min_t1,
                max_t1,
                median_t1,
                mean_t1,
                min_t2,
                max_t2,
                median_t2,
                mean_t2,
                url1,
                note
                ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

            
            
            cursor.execute("SELECT * FROM temp_table")
            rows = cursor.fetchall()
            for row in rows:
                systemName = row[0]
                manufacturer = row[1]
                physicalQubits = row[2]
                processorType = row[3]
                technology = row[4]
                yearOfIntro = row[5]
                topology = row[6]
                clops = row[7]
                medianCZError = row[8]
                medianECRError = row[9]
                medianCNOTError = row[10]
                medianSXError = row[11]
                minSingleQubitGateError = row[12]
                maxSingleQubitGateError = row[13]
                typicalSingleQubitGateError = row[14]
                medianSingleQubitGateError = row[15]
                minTwoQubitGateError = row[16]
                maxTwoQubitGateError = row[17]
                typicalTwoQubitGateError = row[18]
                medianTwoQubitGateError = row[19]
                medianReadoutError = row[20]
                spamError = row[21]
                memoryErrorPerQubitAtAverageDepth1Circuit = row[22]
                midCircuitMeasurementCrossTalkError = row[23]
                minT1 = row[24]
                maxT1 = row[25]
                medianT1 = row[26]
                meanT1 = row[27]
                minT2 = row[28]
                maxT2 = row[29]
                medianT2 = row[30]
                meanT2 = row[31]
                twoQubitGates = row[32]
                oneQubitGates = row[33]
                notes = row[34]
                url = row[35]

                #Remember to set all link id to None
                manufacturer_id = None
                processor_id = None
                topology_id = None
                gateset_id = None
                system_id = None
                solver_id = None
                time_id = None
                metric_id = None

                #Manufactor
                if manufacturer is not None: 
                    #Search for the item
                    cursor.execute(check_manufacturer_sql, [manufacturer])
                    check = cursor.fetchall()

                    #Insert if need to
                    

                    if len(check) != 1:
                        #cursor.execute(insert_manufacturer_sql, (manufacturer,))
                        print(f"New System: {manufacturer}")
                        # Commit the insert if necessary
                        connection.commit()
                    
                    #Get the id for joining
                    cursor.execute(check_manufacturer_sql, [manufacturer])
                    manufacturer_get_id = cursor.fetchall()

                    if manufacturer_get_id:
                        manufacturer_id = manufacturer_get_id[0][0]
                    else:
                        print(f"System {manufacturer} was not found after insertion.")


                #Technology
                if technology is not None:
                    cursor.execute(check_technology_sql, [technology])
                    check = cursor.fetchall()

                    if len(check) != 1:
                        cursor.execute(insert_technology_sql, (technology,))
                        print(f"New tech: {technology}")
                        connection.commit()

                    cursor.execute(check_technology_sql, [technology])
                    technology_get_id = cursor.fetchall()

                    if technology_get_id:
                        technology_id = technology_get_id[0][0]
                    else:
                        print(f"Tech {technology} was not found after insertion.")


                #Topology
                if topology is not None:
                    cursor.execute(check_topology_sql, (topology,))
                    check = cursor.fetchall()

                    if len(check) != 1:
                        cursor.execute(insert_topology_sql, (topology,))
                        print(f"New Topo : {topology}")
                        connection.commit()

                    cursor.execute(check_topology_sql, [topology])
                    topology_get_id = cursor.fetchall()

                    if topology_get_id and topology is not None:
                        topology_id = topology_get_id[0][0]
                    else:
                        print(f"Topo {topology} was not found after insertion.")



                #Processor
                if processorType is not None:
                    cursor.execute(check_processor_sql, [processorType])
                    check = cursor.fetchall()

                    if len(check) != 1:
                        print(processorType, technology_id, manufacturer_id, physicalQubits, topology_id, yearOfIntro, url, notes)
                        cursor.execute(insert_processor_sql, (processorType, technology_id, manufacturer_id, physicalQubits, topology_id, yearOfIntro, url, notes))
                        print(f"New processor: {processorType}")
                        # Commit the insert if necessary
                        connection.commit()

                    cursor.execute(check_processor_sql, [processorType])
                    processor_get_id = cursor.fetchall()

                    if processor_get_id:
                        processor_id = processor_get_id[0][0]
                    else:
                        print(f"Processor {processorType} was not found after insertion.")
                

                #Processor for system if processor is missing
                if processorType is None:
                    cursor.execute(check_processor_sql, [systemName + "'s processor"])
                    check = cursor.fetchall()

                    if len(check) != 1 and processorType is None:
                        print(systemName, technology_id, manufacturer_id, physicalQubits, topology_id, yearOfIntro, url, notes)
                        cursor.execute(insert_processor_sql, (systemName + "'s processor", technology_id, manufacturer_id, physicalQubits, topology_id, yearOfIntro, url, notes))
                        print(f"New processor: {systemName}")
                        # Commit the insert if necessary
                        connection.commit()

                    cursor.execute(check_processor_sql, [systemName + "'s processor"])
                    processor_get_id = cursor.fetchall()

                    if processor_get_id and processorType is None:
                        processor_id = processor_get_id[0][0]
                    else:
                        print(f"Processor {systemName} was not found after insertion.")

                #Gate set
                if twoQubitGates is not None and oneQubitGates is not None:
                    cursor.execute(check_gateset_sql, [twoQubitGates + ', '+ oneQubitGates])
                    check = cursor.fetchall()

                    if len(check) != 1:
                        cursor.execute(insert_gateset_sql,  [twoQubitGates + ', '+ oneQubitGates])
                        print(f"New gate set : {(twoQubitGates + ', '+ oneQubitGates)}")
                        connection.commit()

                    cursor.execute(check_gateset_sql, [twoQubitGates + ', '+ oneQubitGates])
                    gateset_get_id = cursor.fetchall()

                    if gateset_get_id :
                        gateset_id = gateset_get_id[0][0]
                    else:
                        print(f"Gateset {(twoQubitGates + ', '+ oneQubitGates)} was not found after insertion.")

                elif twoQubitGates is not None:
                    cursor.execute(check_gateset_sql, [twoQubitGates])
                    check = cursor.fetchall()

                    if len(check) != 1:
                        cursor.execute(insert_gateset_sql, [twoQubitGates])
                        print(f"New gate set : {(twoQubitGates)}")
                        connection.commit()

                    cursor.execute(check_gateset_sql, [twoQubitGates ])
                    gateset_get_id = cursor.fetchall()

                    if gateset_get_id :
                        gateset_id = gateset_get_id[0][0]
                    else:
                        print(f"Gateset {(twoQubitGates)} was not found after insertion.")

                elif oneQubitGates is not None:
                    cursor.execute(check_gateset_sql, [oneQubitGates])
                    check = cursor.fetchall()

                    if len(check) != 1:
                        cursor.execute(insert_gateset_sql, [oneQubitGates])
                        print(f"New gate set : {(oneQubitGates)}")
                        connection.commit()

                    cursor.execute(check_gateset_sql, [oneQubitGates])
                    gateset_get_id = cursor.fetchall()

                    if gateset_get_id :
                        gateset_id = gateset_get_id[0][0]
                    else:
                        print(f"Gateset {(oneQubitGates)} was not found after insertion.")
                

                

                #System
                cursor.execute(check_system_sql, [systemName])
                check = cursor.fetchall()

                
                if len(check) != 1:
                    cursor.execute(insert_system_sql, (systemName, manufacturer_id, processor_id, yearOfIntro, gateset_id, url, notes))
                    print(f"New System: {systemName}")
                    # Commit the insert if necessary
                    connection.commit()

                cursor.execute(check_system_sql, [systemName])
                system_get_id = cursor.fetchall()

                if system_get_id:
                    system_id = system_get_id[0][0]
                else:
                    print(f"System {systemName} was not found after insertion.")
                
                # Calibration
                insert_calibration_sql = '''INSERT INTO benchmarks_calibration(
                system_id,
                clops,
                median_cz_err,
                median_ecr_err,
                median_cnot_err,
                median_sx_err,
                min_1q_err,
                max_1q_err,
                typical_1q_err,
                median_1q_err,
                min_2q_err,
                max_2q_err,
                typical_2q_err,
                median_2q_err,
                median_readout_err,
                spam_err,
                mem_err_avg_d1_circuit,
                crosstalk_err_mid_circuit,
                min_t1,
                max_t1,
                median_t1,
                mean_t1,
                min_t2,
                max_t2,
                median_t2,
                mean_t2,
                url1,
                notes
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cursor.execute(insert_calibration_sql, (
                system_id, 
                clops, 
                medianCZError, 
                medianECRError, 
                medianCNOTError, 
                medianSXError, 
                minSingleQubitGateError, 
                maxSingleQubitGateError, 
                typicalSingleQubitGateError, 
                medianSingleQubitGateError, 
                minTwoQubitGateError, 
                maxTwoQubitGateError, 
                typicalTwoQubitGateError, 
                medianTwoQubitGateError,
                medianReadoutError, 
                spamError, 
                memoryErrorPerQubitAtAverageDepth1Circuit, 
                midCircuitMeasurementCrossTalkError, 
                minT1, 
                maxT1, 
                medianT1, 
                meanT1, 
                minT2, 
                maxT2, 
                medianT2, 
                meanT2, 
                url, 
                notes
                ))



        self.stdout.write(self.style.SUCCESS('Data loaded and joined successfully'))
