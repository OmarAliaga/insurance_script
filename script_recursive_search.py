import glob
import argparse
from time import perf_counter


parser = argparse.ArgumentParser(description="searching of a file ")
parser.add_argument('-p','--path', type=str, default='/home/omar/projects/guidepython/recursive_scripting',help='where search')
parser.add_argument('-ph','--phrase', type=str, metavar='',required=True,help='phrase to search')
args = parser.parse_args()


def function(path,phrase):
    path += '/*.txt'
    files = glob.glob(path)
    for file in files:
        with open(file,"r") as f:
            lines = f.readlines()
            for line in lines:
                if phrase in line:
                    print(line)




if __name__ == '__main__' :
    t1_start = perf_counter()
    function(args.path,args.phrase)
    t1_stop = perf_counter()
    elapsed_time = t1_stop -t1_start
    print(f'Elapsed time during the program ejecution: {elapsed_time}')

