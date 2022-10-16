<p align="center">
  <p align="center">
    <a href="https://abhinayy0.github.io/DQRCG/" target="_blank">
          <img src="./dqrcg/client/public/apple-touch-icon.png" alt="DQRCG" height="72">
    </a>
  </p>
  <p align="center">
    Dynamic QR Code Generator
  </p>
</p>

## About the project

DQRCG let's you generate dynamic qr code's for your website urls without any hassle. You can create dynamic urls and change your url any time you want.

### Built With

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Launch the app and go to the server and just start using.

### Prerequisites

Install your dependencies using pip.

- pip
  ```sh
  pip install -r requirements.txt
  ```

### Installation

Setting up the server locally.

1. Clone the repo
   ```sh
   git clone https://github.com/abhinayy0/dqrcg.git
   ```
2. Create a virtualenv.
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Activate the virtual environment if you're using it. Install requirements

   ```sh
   pip install -r requirements.txt
   ```

4. Make sure you're in the same working directory as your run.sh before executing the command.

5. For (Linux/ Mac OS) launch using

   ```sh
   python3 services_manager build
   ```

   ```sh
   python3 services_manager run-server
   ```

   For windows launch using

   ```
   ./run.bat
   ```

6. Now your app should be accessible at

   ```
   http://127.0.0.1:5000
   ```

7. For setting up the frontend got to the [client](./dqrcg/client/) folder. Run
   the npm install command to create the node_modules of react app. More info about
   running react project can be found at this [link](https://github.com/facebook/create-react-app).

8. Adjust the backend api config.BASE_URL in [config.js](./dqrcg/client/src/config.js) to point
   to your flask backend. Your project should now be working.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Below you can see the application home page asking for a url field to generate qr code.
After providing the url you will get your generated qrcode.

![Home Screen](/screenshots/homepage.png?raw=true "Home Screen")
![Genereated Code](/screenshots/generatedqr.png?raw=true "Generated Code")
![Validation Error](/screenshots/error.png?raw=true "Validation Error")

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Abhinay Yadav- [@abhinayy0](https://abhinayy0.github.io/) - abhinayy0@gmail.com

Project Link: [https://github.com/abhinayy0/dqrcg](https://github.com/abhinayy0/dqrcg)

<p align="right">(<a href="#top">back to top</a>)</p>
