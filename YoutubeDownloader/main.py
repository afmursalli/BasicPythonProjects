import pytube

url=input("enter video url: ")

path="" #path ı böyle vererek çalıştırdığı klasöre kaydedecek

pytube.YouTube(url).streams.get_highest_resolution().download(path)
