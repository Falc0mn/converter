from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import yt_dlp as youtube_dl
from django.conf import settings
import datetime
import os


def index(request):
    return render(request, "index.html")


def convert_url_to_mp3(request):
    """

    This function converts a url containing a video to a mp3 format,
    using 'yt_dlp' library.

    """
    try:
        # User's selection query and format type (from the html)
        url = request.GET.get("query")
        format_type = request.GET.get("format", "mp3")

        output_path = os.path.join(settings.MEDIA_ROOT, 'downloads')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_parameters = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format_type,
                'preferredquality': '192',
            }],
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_parameters) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_title = info_dict.get('title', None)

        file_path = os.path.join(output_path, f"{file_title}.{format_type}")

        if os.path.exists(file_path):
            def file_iterator(file_path):
                with open(file_path, 'rb') as file:
                    yield from file
                # Delete the file from the system after the user has downloaded it
                os.remove(file_path)
            response = FileResponse(file_iterator(file_path), as_attachment=True, filename=f"{file_title}.{format_type}")
            response['Content-Disposition'] = f'attachment; filename="{file_title}.{format_type}"'
            return response
        else:
            return HttpResponse("File not found", status=404)

    except Exception as exception:
        print(f"[ {datetime.datetime.now()} ] {exception}")
        return render(request, "error.html")

def convert_url_to_wav(request):
    """

    This function converts a url containing a video to a wav format,
    using 'yt_dlp' library.

    """
    try:
        # User's selection query and format type (from the html)
        url = request.GET.get("query")
        format_type = request.GET.get("format", "wav")

        output_path = os.path.join(settings.MEDIA_ROOT, 'downloads')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_parameters = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format_type,
                'preferredquality': '192',
            }],
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_parameters) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_title = info_dict.get('title', None)

        file_path = os.path.join(output_path, f"{file_title}.{format_type}")

        if os.path.exists(file_path):
            def file_iterator(file_path):
                with open(file_path, 'rb') as file:
                    yield from file
                # Delete the file from the system after the user has downloaded it
                os.remove(file_path)

            response = FileResponse(file_iterator(file_path), as_attachment=True,
                                    filename=f"{file_title}.{format_type}")
            response['Content-Disposition'] = f'attachment; filename="{file_title}.{format_type}"'
            return response
        else:
            return HttpResponse("File not found", status=404)

    except Exception as exception:
        print(f"[ {datetime.datetime.now()} ] {exception}")
        return render(request, "error.html")

def convert_url_to_mp4(request):
    """

    This function converts a url containing a video to a mp4 format,
    using 'yt_dlp' library.
    For mp4 format's best quality and resolution it extracts video and audio
    separately and then combines them into one video.

    """
    try:
        # User's selection query and format type (from the html)
        url = request.GET.get("query")
        format_type = request.GET.get("format", "mp4")

        output_path = os.path.join(settings.MEDIA_ROOT, 'downloads')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_parameters = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': f'{format_type}',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': format_type,
            }],
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_parameters) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_title = info_dict.get('title', None)

        file_path = os.path.join(output_path, f"{file_title}.{format_type}")

        if os.path.exists(file_path):
            def file_iterator(file_path):
                with open(file_path, 'rb') as file:
                    yield from file
                # Delete the file from the system after the user has downloaded it
                os.remove(file_path)

            response = FileResponse(file_iterator(file_path), as_attachment=True,
                                    filename=f"{file_title}.{format_type}")
            response['Content-Disposition'] = f'attachment; filename="{file_title}.{format_type}"'
            return response
        else:
            return HttpResponse("File not found", status=404)

    except Exception as exception:
        print(f"[ {datetime.datetime.now()} ] {exception}")
        return render(request, "error.html")

def convert_url_to_webm(request):
    """

    This function converts a url containing a video to a webm format,
    using 'yt_dlp' library.
    For webm format's best quality and resolution it extracts video and audio
    separately and then combines them into one video.

    """
    try:
        # User's selection query and format type (from the html)
        url = request.GET.get("query")
        format_type = request.GET.get("format", "webm")

        output_path = os.path.join(settings.MEDIA_ROOT, 'downloads')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_parameters = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': f'{format_type}',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': format_type,
            }],
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_parameters) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_title = info_dict.get('title', None)

        file_path = os.path.join(output_path, f"{file_title}.{format_type}")

        if os.path.exists(file_path):
            def file_iterator(file_path):
                with open(file_path, 'rb') as file:
                    yield from file
                # Delete the file from the system after the user has downloaded it
                os.remove(file_path)

            response = FileResponse(file_iterator(file_path), as_attachment=True,
                                    filename=f"{file_title}.{format_type}")
            response['Content-Disposition'] = f'attachment; filename="{file_title}.{format_type}"'
            return response
        else:
            return HttpResponse("File not found", status=404)

    except Exception as exception:
        print(f"[ {datetime.datetime.now()} ] {exception}")
        return render(request, "error.html")

def convert_url_to_mov(request):
    """

    This function converts a url containing a video to a mov format,
    using 'yt_dlp' library.
    For mov format's best quality and resolution it extracts video and audio
    separately and then combines them into one video.

    """
    try:
        # User's selection query and format type (from the html)
        url = request.GET.get("query")
        format_type = request.GET.get("format", "mov")

        output_path = os.path.join(settings.MEDIA_ROOT, 'downloads')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_parameters = {
            'format': 'bestvideo[ext=mov]+bestaudio[ext=mov]/best[ext=mov]/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': f'{format_type}',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': format_type,
            }],
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_parameters) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_title = info_dict.get('title', None)

        file_path = os.path.join(output_path, f"{file_title}.{format_type}")

        if os.path.exists(file_path):
            def file_iterator(file_path):
                with open(file_path, 'rb') as file:
                    yield from file
                # Delete the file from the system after the user has downloaded it
                os.remove(file_path)

            response = FileResponse(file_iterator(file_path), as_attachment=True,
                                    filename=f"{file_title}.{format_type}")
            response['Content-Disposition'] = f'attachment; filename="{file_title}.{format_type}"'
            return response
        else:
            return HttpResponse("File not found", status=404)

    except Exception as exception:
        print(f"[ {datetime.datetime.now()} ] {exception}")
        return render(request, "error.html")