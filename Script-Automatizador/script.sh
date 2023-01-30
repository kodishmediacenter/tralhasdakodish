sudo apt-get install apache2 -y 
sudo apt-get install ffmpeg  -y
sudo apt-get install transmission-cli -y 
clear
echo Digite ou Cole url do Torrent vc deseja baixar: 
read link
clear 
HERE=$(dirname $(readlink -f "${0}"))

transmission-cli -w $HERE ''$link''

echo Digite nome da pasta que baixou vou dar um dir para facilitar para vc: 
echo 
echo 
dir
echo Nome da pasta:
read folder
cd $folder
ffmpeg -i *.webm -c:v copy -c:a copy "4.mp4"
ffmpeg -i *.mkv -c:v copy -c:a copy "1.mp4"
ffmpeg -i *.avi -c:v copy -c:a copy "2.mp4"
ffmpeg -i *.ts -c:v copy -c:a copy "2.mp4"
clear 
echo Nome do arquivo:
read cont

sudo mv *.mp4 ''$cont'.mp4'
sudo mv *.mp4 /var/www/html/



