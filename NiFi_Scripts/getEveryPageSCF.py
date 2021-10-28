import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json
import urllib2

class ModJson(StreamCallback):
	def __init__(self):
		pass

	def process(self, inputStream, outputStream):
		#TASK GOES HERE


		
		try:
			

			text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
			
			asjson = json.loads(text)
			
			if asjson['metadata']['pagination']['page']<= asjson['metadata']['pagination']['pages']:
				url = asjson['metadata']['pagination']['next_page_url']
				rawreply = urllib2.urlopen(url).read()
				reply = json.loads(rawreply)

				outputStream.write(bytearray(json.dumps(reply,indent=4).encode('utf-8')))

		except:
			global errorOccurred
			errorOccurred = True
			outputStream.write(bytearray(json.dumps(asjson,indent=4).encode('utf-8')))



#ERROR CATCHING
errorOccurred=False
flowFile = session.get()
if(flowFile!=None):
	flowFile = session.write(flowFile, ModJson())
	#flowFile = session.putAttribute(flowFile)

	if(errorOccurred):
		session.transfer(flowFile, REL_FAILURE)
	else:
		session.transfer(flowFile, REL_SUCCESS)
				
