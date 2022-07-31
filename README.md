<p align="center">
  <img src="https://github.com/mmore21/trojan_lisa/blob/master/img/mona_lisa.png.trojanlisa" width="100" />
</p>

<h2 align="center">trojan_lisa</h2>

Steganographic reverse shell embedded within the Mona Lisa.

## Description

Trojan Lisa is a steganographic engine that embeds a reverse shell within a PNG image of the Mona Lisa. Extracting and executing the code hidden within the image will provide the attacker with a reverse shell. The steganographic engine can be repurposed to store any form of data inside any PNG image given that there are enough pixels to store the encoded message.

The message is encoded by converting it to base64 and then to binary. Next, each pixel of the original image is iterated row-by-row. The message is integrated into the image by making the evenness or oddness of the bits match between the i-th pixel and the i-th bit of the message. In cases where the bits mismatch, the pixel of the image can be decremented by one to correct it. Note, the edge case when the pixel is already zero causes the pixel to be incremented by one instead. Afterward, the image can be reconstructed with the slightly adjust pixel values which now contain the encoded message. This process can be reversed by following the steps in the reverse order.

## Usage

Terminal 1

<pre>
python3 trojan_lisa/stego.py trojan_lisa/reverse_shell.py img/mona_lisa.png img/mona_lisa.png.trojanlisa

          .------.
         /        \
       .' /  \     `.
_______|____________|
 """""8""""""""""8888
     d8.-=. ,==-.:888b
     >8 `~` :`~' d8888
     88         ,88888
     88b. `-~  ':88888
     888b ~==~ .:88888
     88888o--:':::8888
     `88888| :::' 8888b
     8888^^'       8888b
    d888           ,%888b.
   d88%            %%%8--'-.
  /88:.__ ,       _%-' ---  -
      """::===..-'   =  --.  `
    

 _____           _                 __ _           
/__   \_ __ ___ (_) __ _ _ __     / /(_)___  __ _ 
  / /\| '__/ _ \| |/ _` | '_ \   / / | / __|/ _` |
 / /  | | | (_) | | (_| | | | | / /__| \__ | (_| |
 \/   |_|  \____/ |\__,_|_| |_| \____|_|___/\__,_|
              |__/                                
    
== Preparing the canvas...
== Painting La Joconde...
== Visiting Le Louvre...
== La simplicité est la sophistication suprême...
</pre>

Terminal 2

<pre>
nc -lvnp 4444                         
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 33390
</pre>

## Disclaimer

This project is intended solely for educational purposes to better understand various malware techniques. It is not to be distributed, modified, or used for any malicious intent. The authors of this repository take no responsibility for any malicious use of this malware.

## Resources

- https://docs.replit.com/tutorials/steganography
