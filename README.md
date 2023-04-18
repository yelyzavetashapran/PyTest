# PyTest

Hello! It's my PyTest task for program DQE Intermediate Level.

To run this test on your machine, you need:

1. Clone repository.
2. Install requirements.txt with pip: pip install -r requirements.txt
3. Download and install ODBC Driver 17 for SQL Server (https://go.microsoft.com/fwlink/?linkid=2223304).
4. You should create user in MSSMS, create 'TRN' database and change it in main.py file: Open MSSMS go to 'Security' and create new user like in following screenshots:

![image](https://user-images.githubusercontent.com/104168878/232730140-279dc273-90af-4e39-8f27-679a7fed64e9.png)
![image](https://user-images.githubusercontent.com/104168878/232730210-5029fc39-bb15-4082-a586-d41f08e9478c.png)
![image](https://user-images.githubusercontent.com/104168878/232730255-330fa436-97e8-49fe-9e7a-eca4b04212e7.png)

In main.py file you have to change server variable to your local SQL Server:

![image](https://user-images.githubusercontent.com/104168878/232731440-0460cc99-0c30-4baa-b0ce-761a6fffdb65.png)

On this step I found some possible issues that you can also have: Change authentication mode with SQL (https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode?view=sql-server-ver16):

![image](https://user-images.githubusercontent.com/104168878/232732321-50c1e905-6dab-4ac2-9e97-dce9d5c7b529.png)

In SQL Server Configuration Manager go to SQL Server Network Configuration-> Protocols -> TCP/IP and do some changes:

![image](https://user-images.githubusercontent.com/104168878/232732411-32583cc1-2e3c-4b48-a897-147d62bbc3d7.png)
![image](https://user-images.githubusercontent.com/104168878/232732457-cb4bb37b-a300-42dc-b23c-70c0963d7fbd.png)

5. Run test with command: pytest main.py (if you added python and roboframewok to PATH);
python -m pytest main.py (if you don't added python and roboframewok to PATH)
All tests should pass:

![image](https://user-images.githubusercontent.com/104168878/232733174-5aedc41b-bb54-4623-805f-3093b2c690d4.png)

6. To generate a report you need to run command:
 python -m pytest main.py --html=pytest_report.html --self-contained-html

![image](https://user-images.githubusercontent.com/104168878/232889152-c05a522b-34f8-4047-aa17-05aa0fc678d3.png)

That's it! Thank you for your attention!
