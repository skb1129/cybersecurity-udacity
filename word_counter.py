from http.server import HTTPServer, BaseHTTPRequestHandler

# All of the web server template code is already written for you.  
# It will use port 8000 to listen for a GET response
# that will pass in an input, in this case a string for a sentence 
# in the form of a pathname, and the answer will be written
# into an html file that will be checked later in the lab. 

# Your task is completing the function WordCount, so that it
# returns the correct number of words given in an input sentence.

def WordCount(sentence):
    string = sentence.replace('%20', ' ').strip()
    words = string.split(' ')
    words = [word for word in words if word != '']
    return len(words)

class Function(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)

        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        x = self.path[1:]
        answer = WordCount(x)

        self.wfile.write(str(answer).encode())

if __name__ == '__main__':
    # Debug Test Check results
    print("Test 1: "+str(2 == WordCount("A sentence.")))
    print("Test 2: "+str(3 == WordCount("Too  many   spaces!")))
    print("Test 3: "+str(4 == WordCount("Cyber, web, and security? ")))
    print("Test 4: "+str(3 == WordCount("Does%20this%20count?")))
    web_server = True
    if web_server:
        server_address = ('', 8000) # Serve on all addresses, port 8000
        httpd = HTTPServer(server_address, Function)
        httpd.serve_forever()
