import qrcode

with open("wireguard.conf", "r") as f:
    wg = f.read()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=2,
    )

    qr.add_data(wg)
    qr.make(fit=True)
    qr.print_ascii(tty=True)
    qr.make_image(fill_color="black", back_color="white").save("images/wireguard.png")