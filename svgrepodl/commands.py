import sys
import click
from .Url import Url
from .utils import downloader
from os.path import expanduser


def getUserDocumentPath():
	"""Locate Personal User document folder
	Returns:
		[string] -- Return destanation download path
	"""
	return expanduser("~") + "/Documents/icons/"

@click.command()
@click.option('--path', '-p', default=getUserDocumentPath(), help="Change download destination path.")
@click.argument('url')
def cli(path, url):
	"""Run downloader to get SVGREPO pack
	
	Decorators:
		click.command
		click.option
		click.argument
	Arguments:
		path {[string]} -- Destination download path
		url {[string]} -- URL of SVGREPO Collection
	"""
	urlHelpers = Url(url) 
	if not urlHelpers.checker():
		click.echo('😱 Oups URL provided not match !')
		click.echo('💡 Your URL should look like this : https://svgrepo/collection/[id]')
		sys.exit()

	if(urlHelpers.httpGetResponse() != 404):
		dest = path + urlHelpers.collectionName();
		click.echo('📣 Download will start for %s pack !' % urlHelpers.collectionName())
		downloader(url, dest)
	else:
		click.echo("😱 Cannot get this URL!")
		sys.exit()