#!/bin/bash
#SBATCH --partition=gpu4          # GPU partition
#SBATCH --nodes=1                # number of nodes
#SBATCH --gres=gpu:4               # ask for a node with 4 GPUs
#SBATCH --time=72:00:00           # total runtime of job allocation
#SBATCH --mem=100G                   

cd /home/fcamus2s/bachelor_thesis/
git pull
module load cuda
#./my_cuda_program.exe
python PGTSP20.py --search_opt 3 --n_points 50 --epochs 300