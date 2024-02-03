
def total_salary(path):
    try:
        with open(path, 'r') as fh:
            ln_s = [] ; s=d=0 
            for line in fh.readlines():  
                ln_s=line.split(",")
                s=(s+int(ln_s[1])) ; d += 1
            awrg = s/d  

            return s , int(awrg) 
    except Exception as err:
        print(f"Error ; {err} ")
        exit()
        
total, average = total_salary('Comp_Salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
             
