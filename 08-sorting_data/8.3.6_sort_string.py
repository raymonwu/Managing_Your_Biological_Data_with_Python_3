data = ['ACCTGGCCA', 'ACTG', 'TACGGCAGGAGACG', 'TTGGATC']
bylength = sorted(data, key=lambda x:len(x))
print(bylength)