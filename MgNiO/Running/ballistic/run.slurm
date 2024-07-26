#!/bin/bash
#SBATCH -A elmgroup
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --output=outputfile
#SBATCH --error=errorfile
#SBATCH -p gpu
#SBATCH --gres=gpu:a100:1
 
module load nvhpc/21.9
module load gpumd
gpumd < run.in > outputfile
