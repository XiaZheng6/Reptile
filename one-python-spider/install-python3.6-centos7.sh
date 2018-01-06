sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u
python3.6 -V
sudo yum -y install python36u-pip
sudo yum -y install python36u-devel
sudo pip3.6 install numpy
vim learn-pandas.py
sudo pip3.6 install pandas
python3.6 learn-pandas.py 
