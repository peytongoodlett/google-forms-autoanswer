import mechanize, sys


link = 'https://docs.google.com/forms/d/e/1FAIpQLSfomL63-Gh5sQma6EhAo2Ke05ZGdxTE8qMTNqvD1xdGW_MrqQ/viewform'
rsp = ['Option 1']


def vota(i):
	br = mechanize.Browser()
	br.open(link)
	br.set_handle_robots(False)
	br.form = list(br.forms())[0]

    
	for control in br.form.controls:
		if 'en' in control.name:
		    control.readonly = False
		    control.disabled = False

		    br[control.name] = rsp[i]
		    i+=1
		    # print control
		    # print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
	
	br.submit()
	br.close()

def main():
	i=0
	vota(i)



main()
