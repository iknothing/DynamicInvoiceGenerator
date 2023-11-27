## Dynamic Invoice Generator

This script generates an invoice using custom JSON data. You can customize the invoice data as per your liking in the file named `data.json`. The invoice is generated using HTML, so you can edit it accordingly.

**Steps to run:**

1. Create a virtual environment using the command:

    `virtualenv env`

2. Activate the virtual environment using the command:

    `env\Scripts\activate`

3. Install the required Python packages using the following commands:

    `pip install pdfkit`
    `pip install jinja2`
    `pip install num2words`

4. Install the `wkhtmltopdf` package. You can download it from [here](https://wkhtmltopdf.org/downloads.html) or install it using the following command:

    `Sudo apt install wkhtmltopdf`

5. Create a JSON file named `data.json` and enter your invoice data. You can customize the invoice data as per your liking.

6. Run the following command to generate the invoice:

    `python final.py`

This will generate a PDF invoice file named `invoice.pdf`. You can open this file in a PDF reader to view the invoice.
