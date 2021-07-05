#!C:\Users\AshishKumar\anaconda3\python.exe
import cgi


print("content-type: text/html")
print()
form = cgi.FieldStorage()
cmd = form.getvalue("var")

if cmd == "KLO1CC5919":
	print('''<pre>
	<h2><strong>      Car Number: KLO1CC5919      <strong></h2>
	<h2>              Car Model: BMW                      </h2>
	<h2>              hRegistration Name: Ajith           </h2>
	<h2>              Registration Date: 17/1/2013        </h2>
	<h2>              Fuel Type: CNG                      </h2>
	<h2>              Location: Delhi, India              </h2>
	<h2>              Vehicle Class: SUV                  </h2>
	<h2>              Insurance Upto: 19/12/2022          </h2>
	</pre>''')
elif cmd == "Apz8 DD 2438":
	print('''<pre>
    <h2><strong>      Car Number: Apz8 DD 2438      <strong></h2>
	<h2>              Car Model: BMW                      </h2>
	<h2>              hRegistration Name: Ramesh          </h2>
	<h2>              Registration Date: 17/1/2016        </h2>
	<h2>              Fuel Type: CNG                      </h2>
	<h2>              Location: Delhi, India              </h2>
	<h2>              Vehicle Class: SUV                  </h2>
	<h2>              Insurance Upto: 19/12/2026          </h2>
	</pre>''')

elif cmd == "AP294S 8467":
	print('''<pre>
    <h2><strong>      Car Number: AP294S 8467    <strong></h2>
	<h2>              Car Model: BMW                      </h2>
	<h2>              hRegistration Name: Shudha          </h2>
	<h2>              Registration Date: 17/1/2016        </h2>
	<h2>              Fuel Type: CNG                      </h2>
	<h2>              Location: TamilNadu, India          </h2>
	<h2>              Vehicle Class: SUV                  </h2>
	<h2>              Insurance Upto: 19/12/2025          </h2>   
	</pre>''')
else:
    print("<h1>No record Found</h1>")