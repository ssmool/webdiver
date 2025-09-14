## ⛵ Web Diver - WebScrawling
![Python Webdiver Webscrawling Logo](./assets/webdivervas.gif)

**Version:** 2.0 Alpha

**Status:** Under Development  

**Author:** #asytrick

**Website:** [github.com/wendiver](https://github.com/ssmool/webdiver)  

**Contact:** eusmool@gmail.com  

## ⛵ Web Diver

Web Diver is a simple and powerful web crawling and search automation tool for the World Wide Web, developed in Python. Web Diver's main purpose is to read and archive content from specific URLs, saving the data in a structured format in a local SQLite database.

---

## 🚀 Installation

First of all, make sure you're using Python 3.6+ and have pip updated.

### Install via pip:
```bash
#pip install webdiver-2.0 - under release 2.0 Alpha Version
```

⚙️ Basic Functionality

### www_diver_add_taski(url: str)
Sets the URL that will be used in the web content reading and search task.

Example:

```bash
www_diver_add_task('https://electronics.howstuffworks.com/tv.htm')
```

### www_diver_start(db: str, type: str)
Reads the URL defined with www_diver_add_task('db.sqlite','_text') and stores the extracted information in the SQLite database.

Example:

```bash
_type = ['_text','_html','_filter']
www_diver_start('db.sqlite',_type[0])
```

### set_task(uri: str, hour: int, minute: int) - *COMMING SOON - UNDER PREVIEW REVIEW

Schedules a new web crawling task for a specific time, setting the URL, hour, and minute for automatic execution.

Example:

```bash
#set_task("https://example.com/news", 14, 30)
```

💡 Usage Examples

```bash
from webdiver.web_diver import *
www_diver_add_task('https://electronics.howstuffworks.com/tv.htm')
www_diver_start('db.sqlite','_text')
```

```bash
## Task Scheduling - *COMMING SOON - UNDER PREVIEW REVIEW
#set_task("https://example.com", 12, 45)
```

🗃️ Database
The captured data is automatically stored in an SQLite database with information such as:

URL accessed

Simplified HTML content

Collection timestamp

👨‍💻 Developed by
#asytrick
Project available at: github.com/ssmool/webdiver

**🤝 Contributions**

Contributions are welcome! Feel free to open issues, submit pull requests, or reach out by email.

**📫 Contact**

- Author: **#asytrick**  
- Repository: [github.com/webdiver](https://github.com/ssmool/webdiver)  
- Email: **eusmool@gmail.com**

## 📦 CineOS Barsotti @buskplay - RAG PARTS:

Webdiver is a part of the CineOS Barsotti @buskplay - Unix Like project and aligned with global goals for decentralized AI-assisted creative ORM Development, Generative Software Assembly, Researchs, Works Suits and so much more pourposes for SW Deploy and support for(AI Orquestrators by LLMs and GEN-AI and OS Support Documentation) by generative creativity.
