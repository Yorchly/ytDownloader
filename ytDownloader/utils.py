import os
import logging


def create_and_set_directory(path=None):
    """
    Create directory in the path specified, if None create a default directory called music/ in the same
    directory of main.py
    :param path:
    :return:
    """
    path = path or os.path.join(os.getcwd(), "music")
    try:
        os.mkdir(path)
    except FileExistsError:
        logging.info("The dir '{}' already exists. Let's use it!".format(path))
    except OSError as e:
        raise OSError("Error while creating the directory '{}', please try again with different path".format(path))

    return path


def clearing_url(url):
    """
    Erase whitespaces of the url in order to avoid problems
    :param url:
    :return:
    """
    return url.replace(" ", "")
