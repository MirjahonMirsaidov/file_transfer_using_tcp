<div id="top"></div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Transfering large file using tcp in Python. 


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [Socket library](https://docs.python.org/3/library/socket.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

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

