from pytube import YouTube

# https://www.youtube.com/watch?v=C0DPdy98e4c

def progress_function(stream, chunk,file_handle, bytes_remaining):
	print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')

url = input("Enter URL: ")
# url = "https://www.youtube.com/watch?v=C0DPdy98e4c"
print("Searching....")
yt = YouTube(url, on_progress_callback=progress_function)

videos = yt.streams.all()

results = []
ul = "--------------------------------------------------------"
id = 1
for video in videos:
	res_or_abr = video.resolution
	if res_or_abr is None:
		res_or_abr = video.abr
	results.append([id, video.mime_type, res_or_abr, video.filesize])
	id += 1


print("\nTitle: ", yt.title)
print("Description: ", yt.description)
print("Results: ", id-1)

# Printing video formats only

print(ul)
print("\nVideo formats:")
print(ul)
print("ID\tFormate\t\tRes\t\tSize")
print(ul)
for result in results:
	format = result[1].split('/')
	if format[0] == "video":
		print(result[0], '\t',result[1], '\t', result[2], '\t\t', round((int(result[3])/(1024*1024)),3), "MB")

# Printing audio formats only

print("\nAudio formats:")
print(ul)
print("ID\tFormate\t\tAbr\t\tSize")
print(ul)
for result in results:
	format = result[1].split('/')
	if format[0] == "audio":
		print(result[0], '\t',result[1], '\t', result[2], '\t', round((int(result[3])/(1024*1024)),3), "MB")
print(ul)

download_id = int(input("Enter Id to download (0 to exit): "))

if download_id == 0:
	exit()
video = videos[download_id]
video.download()

