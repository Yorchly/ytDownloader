import youtube_dl


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

    def updating_path_for_saving(self, path):
        self.ydl_opts.update({'outtmpl': path + '/%(title)s.%(ext)s'})
