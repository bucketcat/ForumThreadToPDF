# ForumThreadToPDF
A python script that functions as a webscraper, minus having to load the webpage which avoids accidental DoS and subsequent rate limitations, with the intent of saving large forum threads as PDF locally. Limited to forums that use sequential and nonencrypted URL's for page numbering. It downloads threads individual pages, in chunks of 3. It's somewhat slow, but robust and avoids flooding the target site with network requests.

To merge the PDFs to one large PDF, use one of the many open source PDF mergers available.


### Project Dependencies
* Python 3
* PDFkit (https://github.com/foliojs/pdfkit/blob/master/LICENSE)
* whktmltopdf (https://github.com/wkhtmltopdf/wkhtmltopdf/blob/master/LICENSE)

### Follow the install instructions of wkhtmltopdf. If you're on an Windows environment and can't get it to work after adding it to path, look at the comments in the script. I had the same issue and spent way, way too long trying to get it to work. For MAC and Linux, specific installations of dependencies. PDFkit should be installable through your IDE's package manager, while whktmltopdf might have to be installed manually on Windows.


