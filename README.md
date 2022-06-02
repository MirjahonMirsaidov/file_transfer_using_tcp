<div id="top"></div>



<!-- ABOUT THE PROJECT -->
## About The Project

Transfering large file using tcp in Python. 


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Socket library](https://docs.python.org/3/library/socket.html)

<p align="right">(<a href="#top">back to top</a>)</p>



### Installation


1. Clone the repo
   ```sh
   git clone github.com/MirjahonMirsaidov/file_transfer_using_tcp.git
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Run
There 2 versions of the server. First one is server.py, use this to accept only one connection at a time. Second one is multithreaded_server.py, it uses threading library to support more than one transfer. Run one the files above to run server and you can make requrest. To test you can use client.py to transfer files. Before running client.py make sure you ran server and port 5566 is open. If you did steps above correct you will results like this:

![alt text](https://user-images.githubusercontent.com/60573267/171596484-91b49b36-f785-4c2a-a568-c35ab04f2885.png)

![alt text](https://user-images.githubusercontent.com/60573267/171596732-b8d72b54-11f3-4049-a8f1-d0d786e925a8.png)
<p align="right">(<a href="#top">back to top</a>)</p>

