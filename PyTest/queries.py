# hr.jobs
hr_jobs_duplicates = '''SELECT COUNT(*) 
                    FROM
                        (SELECT [job_title], 
								[min_salary], 
								[max_salary], 
								ROW_NUMBER() OVER(partition by [job_title] order by [min_salary], [max_salary] asc) as row_num
						FROM [hr].[jobs]
						) tmp_tbl 
						WHERE row_num > 1
					'''
hr_jobs_average_values = '''SELECT 'ALL' job_titles, 
							    AVG([min_salary]) avg_min, 
							    AVG([max_salary]) avg_max 
						    FROM [hr].[jobs] '''

# hr.employees
hr_employees_empl_cnt = '''SELECT 'Count of employees', count(employee_id) cnt from [hr].[employees]'''

hr_employees_clmns_format_validation = ''' SELECT COUNT(*) 
                                            FROM [hr].[employees] 
                                            WHERE email NOT LIKE '%@%.org' 
                                                OR phone_number NOT LIKE '%.%.%'
                                                OR hire_date NOT LIKE '____-__-__'
                                        '''
# [hr].[locations]
hr_locations_null_rows = '''  SELECT COUNT(*) 
					FROM [hr].locations 
					WHERE street_address IS NULL 
						OR postal_code IS NULL 
						OR city is null 
						OR state_province IS NULL 
						OR country_id IS NULL
				'''

hr_locations_counry_validation = '''
					SELECT COUNT(*) 
					FROM [hr].locations 
					WHERE country_id NOT IN ('US', 'CA', 'UK', 'DE')
					'''
