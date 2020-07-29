# python3.6
import sys
import subprocess

def _command_pipeline(command:str) -> int:
    try:
        _ = subprocess.check_output(f'{command}',
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except Exception as e:
        print(e)
        return -2

    return 1
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"example --> python main.py <pdf_file>")
        exit(-1)
    
    file_name = sys.argv[1].split('.')[0]
    _command_pipeline(f"echo 'extract js > {file_name}.js' > extract_cmd.txt")
    ret = _command_pipeline(f"python2 peepdf/peepdf.py -l -f -s extract_cmd.txt {sys.argv[1]}")
    
    exit(ret)