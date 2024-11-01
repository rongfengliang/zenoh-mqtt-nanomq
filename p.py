import	time
import	zenoh
conf	= zenoh.Config.from_json5("""
							   {"id":"333333","mode":	"client","connect":{"endpoints":["tcp/127.0.0.1:7447"]}}
							   """)
session	= zenoh.open(conf)
key_expr = "demo/example/demo"
pub = session.declare_publisher(key_expr)
while True:
	time.sleep(1.0)
	val	= "Hello!" + str(time.time())
	pub.put(val)