<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/brnom/stock-management">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h1 align="center">Stock Management</h1>

  <!-- <p align="center">
    project_description
    <br />
    <a href="https://github.com/brnom/stock-management"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/brnom/stock-management">View Demo</a>
    ·
    <a href="https://github.com/brnom/stock-management/issues">Report Bug</a>
    ·
    <a href="https://github.com/brnom/stock-management/issues">Request Feature</a>
  </p> -->
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Project that implements a distributed solution to monitor product stock levels at stores and distribution centers

<img src="images/about-project.png" alt="Project Architecture">

Start with stock levels different from zero for all stores and products. Mock product sales by random clients at stores. Every sale debits the current stock level of a given product (represent levels by colors). When a sale provokes a Red level, dispatch a buy order (message on request-topic) to the distribution center (DC). Apply same logic to the DC, where it requires products from fabrics.
When a buy order is done, both DC and stores are added a credit. Fabrics don't need stock management. DC stock level is equal the number of stores \* their max stock level.

### Built With

- [Python](https://www.python.org)
- [Docker](https://www.docker.com)
- [HiveMQ](https://www.hivemq.com)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/) installed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/brnom/stock-management.git
   ```
2. Build and execute docker containers
   ```sh
   docker compose up --build -d
   ```

<!-- USAGE EXAMPLES -->

<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- CONTACT -->

## Contact

Bruno Mengaldo - [@brunomengaldo](https://twitter.com/brunomengaldo) - brunomengaldo@gmail.com

Project Link: [https://github.com/brnom/stock-management](https://github.com/brnom/stock-management)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

<!-- BEST README TEMPLATE -->
<!-- WAIT FOR IT -->

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [wait-for-it](https://github.com/vishnubob/wait-for-it)
- [mqtt-pwn](https://github.com/akamai-threat-research/mqtt-pwn)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/brnom/stock-management.svg?style=for-the-badge
[contributors-url]: https://github.com/brnom/stock-management/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/brnom/stock-management.svg?style=for-the-badge
[forks-url]: https://github.com/brnom/stock-management/network/members
[stars-shield]: https://img.shields.io/github/stars/brnom/stock-management.svg?style=for-the-badge
[stars-url]: https://github.com/brnom/stock-management/stargazers
[issues-shield]: https://img.shields.io/github/issues/brnom/stock-management.svg?style=for-the-badge
[issues-url]: https://github.com/brnom/stock-management/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/brunomengaldo
