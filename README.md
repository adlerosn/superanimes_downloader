# SuperAnimes Downloader
A Python3 script that fetches the video link from superanimes website and downloads it.

##Requisites
Most Linux distros satisfy the requirements.

You will need these programs in your PATH in order to run this program properly:

 * bash
 * python3
 * wget

##Purpose

Download episodes from SuperAnimes.

##How to download an anime
You'll need writing an `animeInfo.txt` file for each anime you want to download.

Let's take "Wolf's Rain" as example:

The anime page is `http://www.superanimes.com/wolfs-rain`, so we write:<br/>
`Page: http://www.superanimes.com/wolfs-rain`<br/>

Most sufixes for SuperAnimes are the same:<br/>
`site_prefix: /episodio-`<br/>

Supposing the download will start from the episode one:<br/>
`ep_first: 1`<br/>

And will end at the 30th:<br/>
`ep_last_: 30`<br/>

The downloaded files will have this "shape":<br/>
`out_file: wolfs-rain-episodio-`<br/>

This is how they used the formatter:<br/>
`ep_num_style: %d`<br/>

The file extension:<br/>
`file_ext: .mp4`<br/>

And the anime name for the temporary files:<br/>
`aniname: wolfs-rain`<br/>

So, it's just a matter of customization of a file.

<br/>
<b>Finally</b>, we have:

`Page: http://www.superanimes.com/wolfs-rain`<br/>
`site_prefix: /episodio-`<br/>
`ep_first: 1`<br/>
`ep_last_: 30`<br/>
`out_file: wolfs-rain-episodio-`<br/>
`ep_num_style: %d`<br/>
`file_ext: .mp4`<br/>
`aniname: wolfs-rain`<br/>

But this one is also valid (and confusing):<br/>
`: http://www.superanimes.com/wolfs-rain`<br/>
`: /episodio-`<br/>
`: 1`<br/>
`: 30`<br/>
`: wolfs-rain-episodio-`<br/>
`: %d`<br/>
`: .mp4`<br/>
`: wolfs-rain`<br/>


###Model for writing an `animeInfo.txt` file:
`Page: `<br/>
`site_prefix: /episodio-`<br/>
`ep_first: 1`<br/>
`ep_last_: `<br/>
`out_file: `<br/>
`ep_num_style: %d`<br/>
`file_ext: .mp4`<br/>
`aniname: `


##How to run
After setting up properly the `animeInfo.txt` file, you'll need the links.

Type the command below in a terminal to grab the video links:<br/>
`python3 simpleAnimeFetch_LinkGrabber.py`<br/>
If it reaches any error, just repeat (or your `animeInfo.txt` may be incorrect, or this script outdated).

Now that you have the video links, just enter with the command below in a terminal:<br/>
`python3 simpleAnimeFetch_Downloader.py`<br/>

If nothing wrong happens, all videos may be in a folder named `Downloads`.