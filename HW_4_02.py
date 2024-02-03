
def get_cats_info(path): #повертати список словників,де кожен словник містить інфор про 1го кота.
    try:
        with open(path,'r') as fh:
            ln_s = [] 
            for line in fh.readlines():
                ln_i = []
                ln_i=line.split(",")
                dic_1 = {"id":ln_i[0] , "name":ln_i[1], "age":ln_i[2].rstrip()}
                ln_s.append(dic_1)
            return ln_s

    except Exception as err:
        print(f"Error ; {err} ")
        exit()

cats_info = get_cats_info("cats_file.txt")
print(cats_info)