import struct
pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'

def parse_atom_line(line):
    '''returns an ATOM line parsed to a tuple '''

    tmp = struct.unpack(pdb_format, line.encode('utf-8'))
    tmp_to_string = [line.decode('utf-8') for line in tmp]
    atom = tmp_to_string[3].strip()
    res_type = tmp_to_string[5].strip()
    res_num = tmp_to_string[8].strip()
    chain = tmp_to_string[7].strip()
    x = float(tmp_to_string[11].strip())
    y = float(tmp_to_string[12].strip())
    z = float(tmp_to_string[13].strip())
    return chain, res_type, res_num, atom, x, y, z