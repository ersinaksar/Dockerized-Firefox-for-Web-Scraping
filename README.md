<h1 align="center" id="title">Dockerized Firefox for Web Scraping</h1>

*Read this in other languages: [English](README.md), [Turkish](README.tr.md).*

<p id="description"> A repository containing a Dockerfile and sample Python code to run Firefox in a Docker container for web scraping. </p>


<p id="description">This is a Dockerized Python script that uses Selenium and Firefox to scrape the page source of a given URL. The script is run in headless mode using Xvfb.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Scrapes the page source of a given URL using Firefox and Selenium.
*   Runs in headless mode using Xvfb.

<h2>🛠️ Installation Steps:</h2>

<p>1. Install Docker on your system.</p>

<p>2. Clone the repository.</p>

<p>3. Build the Docker image using the command</p>

```
sudo docker build -t my-firefox .
```

<p>4. Run the Docker container using the command</p>

```
sudo docker run --rm -e DISPLAY=:99 my-firefox
```

<p>5. The page source of the URL will be printed to the console.</p>

<h2>🍰 Contribution Guidelines:</h2>

Contributions to the project are welcome. If you find a bug or have a suggestion for a new feature please open an issue or a pull request.

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Docker
*   Selenium
*   Firefox
*   Xvfb

<h2>💖Like my work?</h2>

If you have any questions or need help with the project please feel free to open an issue on GitHub.

- :beer: support me **[Patreon]**
- :coffee: support me **[buymeacoffee]** 




[buymeacoffee]: https://www.buymeacoffee.com/in/ersinaksar "buymeacoffee"
[Patreon]: https://www.buymeacoffee.com/ersinaksar "Patreon"
