from collections import namedtuple
from typing import Dict

from requests_html import HTMLSession

GCode = namedtuple('GCode', ['name', 'description', 'long_description', 'arguments'])


def load_marlin_gcodes():
	session = HTMLSession()
	r = session.get('http://marlinfw.org/meta/gcode/')

	d = {}

	for gcode_row in r.html.find('div.gcode-row'):
		commands, name = gcode_row.find('.meta h1', first=True).text.split(' - ')
		description = gcode_row.find('i.fa')[-1].text

		gcode = GCode(name, description=description, long_description='', arguments=[])
		for com in commands.split(', '):
			d[com] = gcode

	return d


def load_smoothie_gcodes():
	d = load_marlin_gcodes()

	session = HTMLSession()
	r = session.get('http://forum.smoothieware.org/supported-g-codes')

	for row in r.html.find('table.wiki-content-table tr')[1:]:
		tds = row.find('td')
		if len(tds) < 2:
			continue

		a = tds[0].find('a', first=True)
		command = a.text if a else tds[0].text

		desc = tds[1].text
		if command in d:
			d[command] = d[command]._replace(long_description=desc)
		else:
			d[command] = GCode('', '', desc, [])

	return d


SUPPORTED_FLAVOURS = {
	'smoothie': load_smoothie_gcodes,
	'marlin': load_marlin_gcodes
}


def load_gcode_flavour(flavour) -> Dict[str, GCode]:
	try:
		return SUPPORTED_FLAVOURS[flavour]()
	except KeyError:
		raise ValueError('Unsupported GCode flavour')
