#!/bin/bash
#SBATCH --partition=gpu          # GPU partition
#SBATCH --nodes=1                # number of nodes
#SBATCH --gres=gpu               # ask for a node with 4 GPUs
#SBATCH --time=3:24:00           # total runtime of job allocation

module load cuda
git pull
#./my_cuda_program.exe
python PGTSP20.py --search-opt 2