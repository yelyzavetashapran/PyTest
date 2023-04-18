import pytest
import sqlalchemy
import urllib

import queries as qur


def connection():
    server = r'EPUAKYIW04F3\SQLEXPRESS01'
    database = 'TRN'
    login = 'loginForTest'
    pwd = 'passwordfortest'

    # if you have trouble with new user credentials, you can connect using Trusted_Connection.
    # Just uncomment params below(row 18-21) and comment row 23-28

    # params = urllib.parse.quote_plus(' DRIVER={ODBC Driver 17 for SQL Server}; \
    #                             SERVER=' + server + '; \
    #                             DATABASE=' + database + '; \
    #                             Trusted_Connection=yes;')

    params = urllib.parse.quote_plus(' DRIVER={ODBC Driver 17 for SQL Server}; \
                                    SERVER=' + server + '; \
                                    DATABASE=' + database + '; \
                                    UID=' + login + '; \
                                    PWD=' + pwd + ';'
                                    )

    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    return engine.connect()


conn = connection()


class TestDB:
    @pytest.mark.hr_locations
    def test_duplicates(self):
        '''Check [hr].[jobs] job_title column on duplicates'''
        res = conn.execute(qur.hr_jobs_duplicates)
        for row in res:
            assert row[0] == 0, f'{row[0]} duplicates founded in job_title column!'

    def test_avg_values(self):
        res = conn.execute(qur.hr_jobs_average_values)
        for row in res:
            assert row[1] < row[2], f'Bad data in hr_jobs table!'
            assert int(row[1]) >= 0 and int(row[2] >= 0), f'Negative values in hr_jobs table!'

    @pytest.mark.hr_employees
    def test_total_cnt(self):
        res = conn.execute(qur.hr_employees_empl_cnt)
        for row in res:
            assert row[1] == 40, f'List of employees is not correct!'

    def test_data_format_validation(self):
        res = conn.execute(qur.hr_employees_clmns_format_validation)
        for row in res:
            assert row[0] == 0, f'{row[0]} bad format rows!'

    @pytest.mark.hr_locations
    def test_null_rows_check(self):
        res = conn.execute(qur.hr_locations_null_rows)
        for row in res:
            assert row[0] <= 1, f'Issue with data completeness! New bad rows founded!'

    def test_contry_list_validation(self):
        res = conn.execute(qur.hr_locations_counry_validation)
        for row in res:
            assert row[0] == 0, f'List of countries not correct'
