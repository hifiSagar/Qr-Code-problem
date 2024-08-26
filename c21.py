##QR CODE GENERATOR PROGRAM


# #OUTPUT PROGRAM
# import qrcode             #library function
# data = "ts_enterprises"    # what should visible in QR code
# qr = qrcode.make(data)      #some instruction
# qr.save("C:/Users/csc/Desktop/qrnew.png")          #file location


#INPUT PROGRAM
print("QR CODE GENERATOR")    #display
import qrcode                 #library function
data =input("input>>    ")    #data taking input
qr=qrcode.make(data)           #data instructin or some instruction or running the data in qr code
qr.save("C:/Users/csc/Desktop/qrnew.png")   #file location
print("QR Code Generation sucessful")    #display