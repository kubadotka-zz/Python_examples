            try:
                hireDate = datetime.datetime.strptime(x['hireDate'], "%Y-%m-%d")
            except ValueError:
                pass
            try:
                todayDate = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
            except ValueError:
                pass
