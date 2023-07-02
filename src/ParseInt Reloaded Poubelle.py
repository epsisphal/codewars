# ParseInt Reloaded Poubelle

if i == '100':
            index_of_100 = string.split().index('100')
            if index_of_100 != 0 and int(string.split()[index_of_100-1]) < 10:
                string_split = string.split()
                string_split[index_of_100] = str(int(string_split[index_of_100-1]) * 100)
                string_split[index_of_100-1] = '0'
                string = ' '.join(string_split)
        if i == '1000':
            index_of_1000 = string.split().index('1000')
            if index_of_1000 != 0:
                string_split = string.split()
                string_split[index_of_1000] = str(int(string_split[index_of_1000-1]) * 1000)
                string_split[index_of_1000-1] = '0'
                string = ' '.join(string_split)