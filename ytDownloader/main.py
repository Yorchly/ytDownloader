from client import YoutubeDownloader
from utils import create_and_set_directory, clearing_url

if __name__ == '__main__':
	yt_dwn = YoutubeDownloader()
	url_list = []
	url = ""
	path = None
	print(
		"########################################################################################\n"
		"Welcome to ytDownloader, you can enter as much urls as you want and then write 'start'\n" 
		"(without quotes '') to start downloading\n"
		"########################################################################################"
	)
	while url != "start":
		url = input("Write url: ")
		if url != "start" and url.find("www.youtube.com") != -1:
			url_list.append(clearing_url(url))
		elif url == "start":
			if len(url_list) == 0:
				print("You have not write any url, please introduce one.\n")
				url = ""
		else:
			print(
				"Input '{}' not recognized, please try again (You can try with something like: "
				"https://www.youtube.com/watch?v=HQJ-LXzn9iw)\n".format(url)
			)

	resp = input("Do you want to set a directory to download? y/N: ")
	if resp == "Y" or resp == "y":
		path = input("Write the path (e.g. /user/test_directory/music): ")

	path = create_and_set_directory(path=path)
	yt_dwn.updating_path_for_saving(path=path)
	res = yt_dwn.download(url_list=url_list)

	if res == 0:
		print("#################################################################################")
		print(
			"SUCCESS DOWNLOADING!\n"
			"Path of downloading: {}".format(path)
		)
	else:
		print("#################################################################################")
		print(
			"ERROR DOWNLOADING!\n"
			"Error -> {}".format(res)
		)
