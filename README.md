termux-change-repo
pkg remove game-repo
pkg remove science-repo
pkg update
apt update -y
apt upgrade -y
pkg install git
pkg install python
pip install tabulate
pip install requests
git clone https://github.com/hyperllo/D3474M53
cd D3474M53
python D3474M53.py