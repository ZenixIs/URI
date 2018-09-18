# -*- coding: utf-8 -*-
# http.py ::: URI module
# @Helix

from . import errors

class URI:
	def __init__(self, URL):
		self.URL = URL
		self.PARSE = URL  
		self.https = None
		self._port = None
		self._host = None

		if not "http" in self.URL:
			raise errors.BadURLError(self.URL)	

	def parsing(self):
		if "http://" in self.PARSE:
			self._port = 80
			self.PARSE = self.PARSE.replace("http://", "")

		elif "https://" in self.PARSE:
			self.https = True
			self._port = 443
			self.PARSE = self.PARSE.replace("https://", "")

		if "/" in self.PARSE:
			self._host = self.PARSE.split("/")[0]
		else:
			self._host = self.PARSE 

		if ":" in self.PARSE:
			host, port = self.PARSE.split(":")
			self._host = host
			if "/" in port:
				port = int(port.split("/")[0])

			self._port = port
		
	def port(self):
		# returns the port of the website
		self.parsing()
		return self._port

	def host(self):
		# returns the domain
		self.parsing()
		return self._host
	
	def path(self):
		# return only gived paths
		# url = "http://test.com/test/adm"
		# result = "/test/adm"
		if "http://" in self.URL:
			self.URL = self.URL.replace("http://", "")
		
		elif "https://" in self.URL:
			self.https = True
			self.URL = self.URL.replace("https://", "")
		
		path = self.URL.split("/")[1:]
		
		return  "/" + "/".join(path)

        def isPath(self):
            if self.path() == "/":
                return False
            else:
                return True
		
	def prepare(self):
		# Prepare the URL, ready for
		# bruteforcing.
		# "test.com/ext/dirs"
		if "http://" in self.URL:
			self.URL = self.URL.replace("http://", "")

		elif "https://" in self.URL:
			self.https = True
			self.URL = self.URL.replace("https://", "")
		
		if self.URL.endswith("/") == False:
			if self.https == True:
				final = "https://" + self.URL + "/"
			else:
				final = "http://" + self.URL + "/"
		else:
			if self.https == True:
				final = "https://" + self.URL
			else:
				final = "http://" + self.URL

		return final
