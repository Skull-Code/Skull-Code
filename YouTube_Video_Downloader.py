# Github: SkullCode

# U NEED PYTUBE INSTALLED
# Install Command: 'pip install pytube'

# If the download dosent start anymore try to reinstall pytube 'pip uninstall pytube' and then install again
# Any bugs contact SkullCode#1878


from pytube import YouTube

link=input("Paste link here :")
yt=YouTube(link)

ys=yt.streams.get_highest_resolution()


ys.download()


print(ys.filesize)


print("Videio download Succes!")