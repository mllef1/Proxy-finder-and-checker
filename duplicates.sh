awk '!seen[$0]++' socks5.txt > new.txt
rm socks5.txt
mv new.txt socks5.txt
