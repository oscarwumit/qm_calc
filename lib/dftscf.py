import os
import subprocess
import shutil


def dft_scf(folder, g16_path, input_file):
    basename = os.path.basename(input_file)
    file_name = os.path.splitext(basename)[0]
    parent_folder = folder
    
    os.mkdir(file_name)
    os.chdir(file_name)

    try:
        g16_command = os.path.join(g16_path, 'g16')
        src_inp = os.path.abspath(input_file)
        des_inp = os.path.abspath(os.path.join(parent_folder, file_name, basename))

        shutil.copyfile(src_inp, des_inp)

        logfile = file_name + '.log'
        outfile = file_name + '.out'

        with open(outfile, 'w') as out:
            subprocess.run('{} < {} >> {}'.format(g16_command, des_inp, logfile), shell=True, stdout=out, stderr=out)
    except Exception as e:
        pass 

    return None

