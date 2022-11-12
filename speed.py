import speedtest as s
st=s.Speedtest()

download=st.download() # we can check the speed using python very easily which is very 
                       # difficult to do in other language

upload=st.upload()

#convert them to mbps

download=download/1000000
upload=upload/1000000

print("My download speed is :", round(download,3),'mbps')
print("My upload speed is :", round(upload,3),'mbps')

st.get_servers([])
ping=st.results.ping

print("Your ping results is :", ping)

