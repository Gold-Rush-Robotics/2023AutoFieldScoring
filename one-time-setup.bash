#!/bin/bash
if ! command -v mamba &> /dev/null
then
    echo "no mamba found... installing"
    if ! command -v conda &> /dev/null
    then
        echo "no conda found... installing"
        if ! command -v curl &> /dev/null
        then
            echo "no curl found... installing"
            if [[ "$OSTYPE" == "linux-gnu"* ]]; then
                sudo apt-get install curl
            elif [[ "$OSTYPE" == "darwin"* ]]; then
                if ! command -v brew &> /dev/null
                then
                    echo "please install brew first"
                    exit 1;
                fi
                brew install curl
            else
                echo "cannot auto install curl. please install curl first"
                exit 1;
            fi
        fi
        curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
        bash Miniforge3-$(uname)-$(uname -m).sh
    else
        conda install mamba -c conda-forge
    fi
fi
echo "mamba installed"

mamba create -n grr_ros_env
eval "$(conda shell.bash hook)"
conda activate grr_ros_env

conda config --env --add channels conda-forge
conda config --env --add channels robostack-staging
conda config --env --remove channels defaults

mamba install ros-humble-desktop -y
mamba deactivate
mamba activate grr_ros_env

mamba install compilers cmake pkg-config make ninja colcon-common-extensions catkin_tools -y

pip install -U colcon-common-extensions -y

mamba activate grr_ros_env
cd ros2ws/
colcon build --symlink-install
