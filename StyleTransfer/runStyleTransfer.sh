clear 
PROJECT_PATH=$1
STYLE_PATH=$PROJECT_PATH/StyleTransfer/style/$2
array=(${3// / })

echo "- Maya Style Transfer - "

echo "#######################################"
echo "- Creating the environment -"
echo "#######################################"

#Setup the working environment

alias mayapy='/opt/autodesk/maya/bin/mayapy'
export PATH=$PATH:/public/bin/2018
export PATH=/opt/qt/5.11.1/gcc_64/bin:/opt/qt/Tools/QtCreator/bin:$PATH
export PYTHONPATH=$PYTHONPATH:$HOME/NGL/lib
export PYTHONPATH=$PYTHONPATH:$RMANTREE/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/$RMANTREE/lib:
export PATH=$PATH:/$RMANTREE/bin

#Set-up the virtualenv

source $PROJECT_PATH/StyleTransfer/virtualEnvironment/bin/activate
cd $PROJECT_PATH/StyleTransfer

echo "#######################################"
echo "- Collecting textures -"
echo "#######################################"

#Create directories
mkdir $PROJECT_PATH/collectedTX
mkdir $PROJECT_PATH/convertedTX 

#Add textures into the directory
for (( i=3;$i<=$#;i=$i+1 ))
do	
	cp ${!i} $PROJECT_PATH/collectedTX
done

echo "#######################################"
echo "- Installing Dependencies -"
echo "- This may take a while -"
echo "#######################################"

pip install numpy pillow tensorflow scipy moviepy

echo "#######################################"
echo "- Running the NN -"
echo "#######################################"

for i in "${!array[@]}"
do	
	#Get File Name
	for fullpath in "${array[i]}"
	do
		filename="${fullpath##*/}"
	done
	#Set Export Name	
	exportname="Converted_"$filename

	#Run network and export results
	python run.py --model $STYLE_PATH --input ${array[i]} --output $PROJECT_PATH/convertedTX/$exportname
#	python run.py --model $PROJECT_PATH/StyleTransfer/style/la_muse.ckpt --input ${array[i]} --output $PROJECT_PATH/convertedTX/$exportname
done
