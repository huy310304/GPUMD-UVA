#!/bin/bash
#SBATCH -A elmgroup_standard
#SBATCH --ntasks=1
#SBATCH --time=20:00:00
#SBATCH --output=outputfile
#SBATCH --error=errorfile
#SBATCH -p gpu
#SBATCH --gres=gpu:a100:1
 
module load nvhpc/24.1
module load gpumd
gpumd < run.in > outputfile
