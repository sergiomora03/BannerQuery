import cx_Oracle
import math
import pandas as pd

class connection_banner:
    """class to generate connection with databases in Banner.
    """
    def init_oracle_database(path_oracle_client):
        """Init connection with oracle database with client.

        Args:
            path_oracle_client (str): path where is instant client

        Returns:
            cx_Oracle.init_oracle_client: init oracle instant client
        """
        return cx_Oracle.init_oracle_client(lib_dir=path_oracle_client)
    def BANNER_CON(user, password, service_name, host, port = '1521'):
        """connection with Banner and easy make dns with cx_Oracle.

        Args:
            user (str): user to connect.
            password (str): password to connect.
            service_name (str): service name to connect.
            host (str): host to connect.
            port (str, optional): port to connect. Defaults to '1521'.

        Returns:
            cx_Oracle.connect: object to connect with Banner.
        """
        BANNER = cx_Oracle.connect(user=user, password=password, dsn=cx_Oracle.makedsn(host, port, service_name=service_name))
        return BANNER

def time_process(toc, tic):
    """return process time. import time; tic = time.process_time(); toc = time.process_time()

    Args:
        toc (float): time in seconds of finshed process
        tic (float): time in seconds of begin process
    """
    return(
        [
        ''.join(['0',str(math.floor((toc - tic)/60/60))]) if math.floor((toc - tic)/60/60) < 10 else math.floor((toc - tic)/60/60),
        ''.join(['0',str(math.floor((toc - tic)/60))]) if math.floor((toc - tic)/60) < 10 else math.floor((toc - tic)/60),
        ''.join(['0',str(math.floor((toc - tic)/60 % math.floor((toc - tic)/60) * 60))]) if (toc - tic)/60 % math.floor((toc - tic)/60) * 60 < 10 else math.floor((toc - tic)/60 % math.floor((toc - tic)/60) * 60)
        ]
    )

class banner:
    def capp_runs(BANNER):
        """statement go to SMRRQCM and get you CAPP info.

        Args:
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            Data Frame: Total CAPP excecuted or running
        """
        CAPP = pd.read_sql_query("SELECT COUNT (*) FROM SMRRQCM WHERE SMRRQCM_COMPLY_DATE IS NOT NULL", BANNER)
        return CAPP
    def capp_not_runs(BANNER):
        """statement go to SMRRQCM and get you CAPP info.

        Args:
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            Data Frame: Total CAPP NO excecuted or running
        """
        CAPP = pd.read_sql_query("SELECT COUNT (*) FROM SMRRQCM WHERE SMRRQCM_COMPLY_DATE IS NULL", BANNER)
        return CAPP
    def program_capp(comply_date = "Y"):
        """Count PIDMS with CAPP or NOT in selected program.

        Args:
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.
            comply_date (str, optional): Whether 'Y' you can check students with CAPP or not 'N'. Defaults to "Y".

        Returns:
            Data Frame: Data Frame with the students total number with or not CAPP from program choosed.
        """
        if (comply_date == "Y"):
            print("Buscando SMRRQCM_COMPLY_DATE IS NOT NULL","\n")
            PROGRAMS_BANNER_CAPP = pd.read_sql_query("SELECT COUNT (DISTINCT SMRRQCM_PIDM) AS NUMBER_STUDENT, SMRRQCM_PROGRAM  AS PROGRAM_STUDENT FROM SMRRQCM WHERE SMRRQCM_COMPLY_DATE IS NOT NULL GROUP BY SMRRQCM_PROGRAM  ORDER BY COUNT (DISTINCT SMRRQCM_PIDM)", BANNER)
        elif (comply_date == "N"):
            print("Buscando SMRRQCM_COMPLY_DATE IS NULL","\n")
            PROGRAMS_BANNER_CAPP = pd.read_sql_query("SELECT COUNT (DISTINCT SMRRQCM_PIDM) AS NUMBER_STUDENT, SMRRQCM_PROGRAM  AS PROGRAM_STUDENT FROM SMRRQCM WHERE SMRRQCM_COMPLY_DATE IS NULL GROUP BY SMRRQCM_PROGRAM  ORDER BY COUNT (DISTINCT SMRRQCM_PIDM)", BANNER)
        else:
            print("we need: 'Y' or 'N' \n")
        return PROGRAMS_BANNER_CAPP
    def count_student(program, period, BANNER): 
        """Count students in program from a period.

        Args:
            program (str): Program to be count.
            period (int): Period to be count.
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            Data Frame: Total students there are in selected program.
        """
        Query = ''.join(["SELECT COUNT(DISTINCT SPRIDEN_ID) AS NUMBR_STUDENT, SOVLCUR_PROGRAM AS PROGRAM_STUDENT FROM SOVLCUR , SGBSTDN G1, SORLCUR, SORLFOS, SPRIDEN WHERE SOVLCUR_PROGRAM  = '" ,program, "' AND SOVLCUR_LMOD_CODE = 'LEARNER' AND SOVLCUR_CURRENT_IND = 'Y' AND SOVLCUR_ACTIVE_IND = 'Y' AND SORLFOS_PIDM = SORLCUR_PIDM AND SORLCUR_SEQNO = SORLFOS_LCUR_SEQNO AND SOVLCUR_PIDM = SORLCUR_PIDM AND SOVLCUR_PROGRAM = SORLCUR_PROGRAM AND SORLFOS_CSTS_CODE <> 'AWARDED' AND SGBSTDN_PIDM = SOVLCUR_PIDM AND SGBSTDN_STST_CODE <> 'IS' AND SOVLCUR_PIDM = SPRIDEN_PIDM AND G1.SGBSTDN_TERM_CODE_EFF = (SELECT MAX(SGBSTDN_TERM_CODE_EFF) FROM SGBSTDN WHERE SGBSTDN_TERM_CODE_EFF <= ",str(period)," AND SGBSTDN_PIDM = G1.SGBSTDN_PIDM) GROUP BY SOVLCUR_PROGRAM"])
        PROGRAM = pd.read_sql_query(Query, BANNER)
        return PROGRAM
    def student(program, period, BANNER):
        """List of student in programa for a period.

        Args:
            program (str): Program where student are.
            period (int): Period where student are.
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            Data Frame: return list of student in the Program.
        """
        print(''.join(["Esta ejecutando el programa: ", program, " para el periodo ", str(period)]))
        Query = ''.join(["SELECT DISTINCT  SPRIDEN_ID AS ESTUDIANTES, SOVLCUR_PROGRAM AS PROGRAMA FROM SOVLCUR , SGBSTDN G1, SORLCUR, SORLFOS, SPRIDEN WHERE SOVLCUR_PROGRAM  = '" ,program, "' AND SOVLCUR_LMOD_CODE = 'LEARNER' AND SOVLCUR_CURRENT_IND = 'Y' AND SOVLCUR_ACTIVE_IND = 'Y' AND SORLFOS_PIDM = SORLCUR_PIDM AND SORLCUR_SEQNO = SORLFOS_LCUR_SEQNO AND SOVLCUR_PIDM = SORLCUR_PIDM AND SOVLCUR_PROGRAM = SORLCUR_PROGRAM AND SORLFOS_CSTS_CODE <> 'AWARDED' AND SGBSTDN_PIDM = SOVLCUR_PIDM AND SGBSTDN_STST_CODE <> 'IS' AND SOVLCUR_PIDM = SPRIDEN_PIDM AND G1.SGBSTDN_TERM_CODE_EFF = (SELECT MAX(SGBSTDN_TERM_CODE_EFF) FROM SGBSTDN WHERE SGBSTDN_TERM_CODE_EFF <= ",str(period)," AND SGBSTDN_PIDM = G1.SGBSTDN_PIDM)"])
        PROGRAM = pd.read_sql_query(Query, BANNER)
        return PROGRAM
    def studypath_student(ID_STUDENT, BANNER):
        """Give you studypath student with ID student.

        Args:
            ID_STUDENT (int): ID student.
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            DataFrame: return studypath student.
        """
        statement = ''.join(["SELECT DISTINCT SPRIDEN_ID AS ID,SPRIDEN_PIDM AS PIDM,SOVLCUR_KEY_SEQNO AS STUDYPATH,SOVLCUR_PROGRAM AS PROGRAMA,SOVLCUR_CURRENT_IND AS ACTUAL,SOVLCUR_ACTIVE_IND AS ACTIVO, SOVLCUR_TERM_CODE AS PERIODO FROM SOVLCUR,SPRIDEN WHERE SPRIDEN_PIDM = SOVLCUR_PIDM AND SPRIDEN_ID = '", str(ID_STUDENT), "'"])
        STSP = pd.read_sql_query(statement, BANNER)
        return STSP
    def search_PIDM(PIDM, BANNER):
        """Give you general codes from student with PIDM.

        Args:
            PIDM (int): student PIDM
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            DataFrame: return data frame with types codes of student
        """
        print("Buscando:",PIDM,"\t", "\n")
        STATEMENT = ''.join(["SELECT SPRIDEN_ID, SPRIDEN_PIDM, SPBPERS_SSN, SPBPERS_LEGAL_NAME FROM SPRIDEN, SPBPERS WHERE SPRIDEN_PIDM = SPBPERS_PIDM AND SPRIDEN_PIDM = '", str(PIDM), "'"])
        PERSON = pd.read_sql_query(STATEMENT, BANNER)
        return PERSON
    def search_ID(ID, BANNER):
        """Give you general codes from student with ID.

        Args:
            ID (int): ID in BANNER of student.
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            DataFrame: return data frame with types codes of student
        """
        STATEMENT = ''.join(["SELECT SPRIDEN_ID, SPRIDEN_PIDM, SPBPERS_SSN, SPBPERS_LEGAL_NAME FROM SPRIDEN, SPBPERS WHERE SPRIDEN_PIDM = SPBPERS_PIDM AND SPRIDEN_ID = '", str(ID), "'"])
        PERSON = pd.read_sql_query(STATEMENT, BANNER)
        return PERSON
    def search_ssn(SSN, BANNER):
        """Give you general codes from student with SSN.

        Args:
            SSN (int): SSN or CC of student.
            BANNER (cx_Oracle.Connection): Connection to Oracle Database.

        Returns:
            DataFrame: return data frame with types codes of student
        """
        STATEMENT = ''.join(["SELECT SPRIDEN_ID, SPRIDEN_PIDM, SPBPERS_SSN, SPBPERS_LEGAL_NAME FROM SPRIDEN, SPBPERS WHERE SPRIDEN_PIDM = SPBPERS_PIDM AND SPBPERS_SSN IN ('", str(SSN), "')"])
        PERSON = pd.read_sql_query(STATEMENT, BANNER)
        return PERSON

class capp:
    """class of CAPP in Banner. Remember: CAPP run = 'Y'. CAPP not run = 'N'. Both = 'B'
    """
    def capp_summary(CAPP = "B"):
        if (CAPP == "B"):
            print(banner.capp_not_runs())
            print(banner.capp_runs())
        elif (CAPP == "Y"):
            banner.capp_runs()
        elif (CAPP == "N"):
            banner.capp_not_runs()
        else:
            print("Remember: CAPP run = 'Y'. CAPP not run = 'N'. Both = 'B'")