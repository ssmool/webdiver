## ⛵ Web Diver - WebScrawling
![Python Webdiver Webscrawling Logo](./assets/webdivervas.gif)

**Version:** 1.0 Beta

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
pip install webdiver_v1
pip install requests beautifulsoup4 pandas
```

⚙️ Basic Functionality

### sql_setup(db_name: str)
Creates and configures a .db file to keep records of searches performed by Web Diver.

Example:

```bash
sql_setup("webdiver_archive.db")
```

### set_task_uri(url: str)
Sets the URL that will be used in the web content reading and search task.

Example:

```bash
set_task_uri("https://example.com")
```

### www_diver()
Reads the URL defined with set_task_uri() and stores the extracted information in the SQLite database.

Example:

```bash
www_diver()
```

### set_task(uri: str, hour: int, minute: int)

chedules a new web crawling task for a specific time, setting the URL, hour, and minute for automatic execution.

Example:

```bash
set_task("https://example.com/news", 14, 30)
```

💡 Usage Examples

```bash
from webdiver import set_task_uri, www_diver, sql_setup, set_task
sql_setup("mydata.db")
set_task_uri("https://example.com")
www_diver()
```

```bash
## Task Scheduling
set_task("https://example.com", 12, 45)
```

🗃️ Database
The captured data is automatically stored in an SQLite database with information such as:

URL accessed

Simplified HTML content

Collection timestamp

👨‍💻 Developed by
#asytrick
Project available at: github.com/ssmool/webdiver

##🤝 Contributions

Contributions are welcome! Feel free to open issues, submit pull requests, or reach out by email.

##📫 Contact

- Author: **#asytrick**  
- Repository: [github.com/webdiver](https://github.com/ssmool/webdiver)  
- Email: **eusmool@gmail.com**
