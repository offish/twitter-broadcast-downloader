import os


def download(m3u8_url: str, output: str = "output.mp4", ffmpeg_path: str = "") -> None:
    command = ""

    if not ffmpeg_path:
        command = "ffmpeg"
    else:
        command = ffmpeg_path

    command += f" -i {m3u8_url} -vcodec copy -acodec copy {output}"
    os.system(command)


def remove_file(file: str) -> None:
    os.remove(file)


def extract_m3u8_url(text: str) -> str:
    text = text.replace("\\", "")
    for i in text.split('"'):
        if ".m3u8" in i and ("playlist_" in i or "master_dynamic_" in i):
            return i
