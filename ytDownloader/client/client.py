import youtube_dl
import os


class YoutubeDownloader:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            },
            {
                'key': 'FFmpegMetadata'
            }
        ]
    }

    def __init__(self, ydl_opts=None):
        self.ydl_opts = ydl_opts or self.ydl_opts

    def download(self, url_list):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            try:
                res = ydl.download(url_list=url_list)
            except youtube_dl.utils.ExtractorError as e:
                res = "Error {}".format(e)
            return res

    def create_and_set_directory(self, path=None):
        import ipdb; ipdb.set_trace()
        path = path or os.path.join(os.getcwd(), "music")
        try:
            os.mkdir(path)
            update = True
        except FileExistsError:
            update = True
        except OSError as e:
            return "Error creating directory: {}".format(e)

        if update:
            self.ydl_opts.update({'outtmpl': path + '/%(title)s.%(ext)s'})

        return path
