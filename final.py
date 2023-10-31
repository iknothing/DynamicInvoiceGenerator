import  pdfkit
from jinja2 import  Template
from num2words import num2words

# steps to run:
# create virtual Environment using command: virtualenv env
# activate virtual environment using command: env\Scripts\activate
# pip install pdfkit
# pip install jinja2
# pip install num2words
# install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html or  Sudo apt install wkhtmltopdf

html="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Invoice</title>
    <style>
        *{
            border: 0;
            box-sizing: content-box;
            color: inherit;
            font-family: inherit;
            font-family: 'Merriweather', serif !important;
            font-style: inherit;
            font-weight: inherit;
            line-height: inherit;
            list-style: none;
            margin: 0;
            padding: 0;
            text-decoration: none;
            vertical-align: top;
            font-size: 15px;
        }
        .marathi{
            font-family: 'Palanquin', sans-serif !important;
        }
        .marathi.info p {
            margin-top: 0;
            font-weight: 600;
            margin-bottom: 0;
            font-family: 'Palanquin', sans-serif !important;
            font-size: 11px;
            color: #181818;
            line-height: 1.5;
        }
        p.text-center.mah_in {
            position: absolute;
            font-size: 12px;
            top: 5px;
            left: 47%;
            font-family: 'Palanquin', sans-serif !important;
        }
        td{word-break: break-all;}    
        .marathi.info {
            margin-top: 20px;
        }
        .red{
            color:#f44336!important;
        }
        
        /* content editable */
        
        *[contenteditable] { border-radius: 0.25em; min-width: 1em; outline: 0; }
        
        *[contenteditable] { cursor: pointer; }
        
        *[contenteditable]:hover, *[contenteditable]:focus, td:hover *[contenteditable], td:focus *[contenteditable], img.hover {  }
        
        span[contenteditable] { display: inline-block; }
        
        /* heading */
        
        h1 { font: bold 100% sans-serif; letter-spacing: 0.5em; text-align: center; text-transform: uppercase; }
        
        /* table */
        
        table { font-size: 75%; table-layout: auto; width: 100%; }
        table { border-collapse: separate; border-spacing: 2px; }
        th, td { border-width: 1px; padding: 0.5em; position: relative; text-align: left; }
        th, td { border-radius: 0.25em; border-style: solid; }
        th {border-color: black; }
        td { border-color: black; }
        
        /* page */
        
        /* html { font: 16px/1 'Open Sans', sans-serif; overflow: auto; padding: 0.5in; }
        html { background: #999; cursor: default; }
        
        body { box-sizing: border-box; min-height: 11in; margin: 0 auto; padding: 0 0.5in; width: 8.5in; }
        body { background: #FFF; border-radius: 1px; box-shadow: 0 0 1in -0.25in rgba(0, 0, 0, 0.5); }
         */
        /* header */
        
        header { margin: 0 0 1em; }
        header:after { clear: both; content: ""; display: table; }
        
        header h1 { background: #000; border-radius: 0.25em; color: #FFF; margin: 0 0 1em; padding: 0.5em 0; }
        header address { float: left; font-size: 75%; font-style: normal; line-height: 1.25; margin: 0 1em 1em 0; }
        header address p { margin: 0 0 0.25em; }
        header span, header img { display: block; }
        header span { max-height: 100%; max-width: 100%; position: relative; }
        header img { max-height: 100%; max-width: 100%; margin: 0 auto;}
        header input { cursor: pointer; -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)"; height: 100%; left: 0; opacity: 0; position: absolute; top: 0; width: 100%; }
        
        /* article */
        
        article, article address, table.meta, table.inventory { margin: 0 0 0em; }
        article:after { clear: both; content: ""; display: table; }
        article h1 { clip: rect(0 0 0 0); position: absolute; }
        
        article address { float: left; font-size: 125%; font-weight: bold; }
        
        /* table meta & balance */
        
        table.meta, table.balance { float: right; width: auto; }

        
        /* table meta */
        
        table.meta th { width: 40%; }
        table.meta td { width: 60%; }
        
        /* table items */
        
        table.inventory { clear: both; width: 100%; }
        table.inventory th { font-weight: 400; text-align: center; }

        table.inventory td:nth-child(1) { width: 35%; } 
        table.inventory td:nth-child(2) { width: 10%; }
        table.inventory td:nth-child(3) { text-align: right; width: 12%; }
        table.inventory td:nth-child(4) { text-align: right; width: 12%; } /* Adjust the width of the Quantity column */
        table.inventory td:nth-child(5) { text-align: right; width: 12%; } /* Adjust the width of the Price column */
        table.inventory td:nth-child(6) { text-align: right; width: 12%; }
        
        /* table balance */
        
        table.balance th, table.balance td { width: 50%; }
        table.balance td { text-align: right; }

        table.balance-master th, table.balance-master td { border: 1px solid black; width: 50%; }
        /* aside */
        
        aside h1 { border: none; border-width: 0 0 1px; margin: 0 0 1em; }
        aside h1 { border-color: #999; border-bottom-style: solid; }
        .left_info {
            width: 60%;
            display: inline-block;
        }
        .min_height {
            min-height: 283px;
        }
        /* javascript */
        
        .add, .cut
        {
            border-width: 1px;
            display: block;
            font-size: .8rem;
            padding: 0.25em 0.5em;  
            float: left;
            text-align: center;
            width: 0.6em;
        }
        .signature{margin-top: 40px;
        float: right;
        bottom: 10px;
        right: 20px;
        }
        
        }
        .add, .cut, .mah_btn
        {
            background-position: 0% 0%;
            box-shadow: 0 1px 2px rgba(0,0,0,0.2);
            border-radius: 0.5em;
            border-color: #0076A3;
            color: #FFF;
            cursor: pointer;
            font-weight: bold;
            background-image: -webkit-linear-gradient(#00ADEE 5%, #0078A5 100%);
            background-color: #9AF;
            background-repeat: repeat;
            background-attachment: scroll;
        }
        
        .add { margin: -2.5em 0 0; }
        
        .add:hover { background: #00ADEE; }
        
        .cut { opacity: 0; position: absolute; top: 0; left: -1.5em; }
        .cut { -webkit-transition: opacity 100ms ease-in; }
        
        tr:hover .cut { opacity: 1; }
        
        @media print {
            * { -webkit-print-color-adjust: exact; }
            html { background: none; padding: 0; }
            
            .add, .cut { display: none; }
                .input.clientDetails{
                border-bottom: none;
            }
        
        }
        @page { margin: 0; }
        
        body{
            margin-top: 0px;
            
            position: relative;
        }
        header img {
            width: 816px;
            margin-left: -48px;
            max-width: 816px !important;
        }
        div.container a.navbar-brand{
            color: white;
        }
        img.stamp{
            margin-left:5px;
            height:50px;
            background: rgba(0, 0, 0, 0);
            box-shadow: 0 0 0 0 rgba(0, 0, 0, 0);
        }
        .bold{
            font-weight:400;
        }
        .left_btn button.mah_btn {
            font-size: 14px;
            font-weight: 400;
            padding: 8px 19px;
            border-radius: 3px;
        }
        .left_btn {
            width: 50%;
            float: left;
        }

        
        
        .nodisplay{
            display: none;
        }

        .display {
            display: block;
        }
        .clientDetails {
            width: 400px;
            border-bottom: 1px solid #ccc;
            margin-bottom: 3px;
            font-size: 15px;
            word-wrap: break-word;
        }
        .bankDetails{
            width: 300px;
            border-bottom: 1px solid #ccc;
            margin-bottom: 3px;
            font-size: 15px;
        }
        
        .add:hover,.cut:hover { text-decoration: none; }
        
        /* content editable */
        
        *[contenteditable] { border-radius: 0.25em; min-width: 1em; outline: 0; }
        
        *[contenteditable] { cursor: pointer; }
        
        *[contenteditable]:hover, *[contenteditable]:focus, td:hover *[contenteditable], td:focus *[contenteditable], img.hover { background: #fcf3a9; box-shadow: 0 0 1em 0.5em #DEF; }
        
        span[contenteditable] { display: inline-block; }</style>
        
</head>
<body>
    <form>
        <header>
            <span>
            </span>
        </header>
        <article class="invoicebody">
            <div class="container">
            <table style="width: 100%;">
                <tr>
                    <td style="width: 50%;">
                        <div class="row"></div>
                                    <table  id="top_data_table">
                            <tbody>
                                <tr>
                                    <th class="bold"><span class="date" id="Date"> Invoice Date</span></th>
                                    <td><span contenteditable=""><input type="text" id="Date" value="{{ data.BillDate }}"></span></td>
                                </tr>
                            </tbody>
                        </table>
                        </div>
                    </td>
                    <td style="width: 50%;">
                        <table  id="top_data_table">
                            <tbody>
                                <table  id="top_data_table">
                                <tr>
                                    <th class="bold"><span class="invoiceno" id="invoiceno"> Invoice Number</span></th>
                                    <td><span contenteditable=""><input type="text" id="invoice number" value="{{ data.BillNo }}"></span></td>
                                </tr>
                            </tbody>
                        </table>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </table>
            

            <div class="container" style="display: block;">
            <table style="width: 100%;">
                <tr>
                    <td style="width: 50%;">
                        <div class="row"></div>
                                <h2 class="text-center mah_in">BILL From:</h2>
                                    <div class="left_info">
                                        <input type="text" class="clientDetails" id="CompanyName" placeholder="Company Name" value="{{ data.CompanyName }}"><br>
                                        <textarea class="clientDetails" id="CompanyAddress" placeholder="Address">{{ data.CompanyAddress }}</textarea><br>
                                        <input type="text" class="clientDetails" id="CompanyGstNo" placeholder="GstNO" value="GST No:{{ data.CompanyGstNo }}"><br>
                                        <input type="text" class="clientDetails" id="CompanyGstNo" placeholder="PanNo" value="PAN No:{{ data.CompanyPanNo }}"><br>
                                        <input type="text" class="clientDetails" id="HSN" placeholder="HSN" value="HSN:{{ data.CompanyHSN }}"><br>
                                    </div>
                        </div>
                    </td>
                    <td style="width: 50%;">
                        <table  id="top_data_table">
                            <tbody>
                                <tr>
                                    <th class="bold"><span class="claim" id="claim_no">Claim No</span></th>
                                    <td><span contenteditable=""><input type="text" id="ClaimNo" value="{{ data.ClaimNo }}"></span></td>
                                </tr>
                                <tr>
                                    <th class="bold"><span class="claim" id="claim_type">Claim Type</span></th>
                                    <td><span contenteditable=""><input type="text" id="ClaimType" value="{{ data.ClaimType }}"></span></td>
                                </tr>
                                <tr>
                                    <th class="bold"><span class="policy" id="policy_no">Policy No</span></th>
                                    <td><span contenteditable=""><input type="text" id="PolicyNo" value="{{ data.PolicyNo }}"></span></td>
                                </tr>
                                
                                <tr>
                                    <th class="bold"><span class="insured" id="insured_name">Insured Name</span></th>
                                    <td><span contenteditable=""><input type="text" id="InsuredName" value="{{ data.InsuredName }}"></span></td>
                                </tr>
                                <tr>
                                    <th class="bold"><span class="insured" id="insured_location">Insured Location</span></th>
                                    <td><span contenteditable=""><input type="text" id="InsuredLocation" value="{{ data.InsuredLocation }}"></span></td>
                                </tr>
                    
                            </tbody>
                        </table>
                    </td>
                </tr>
            </table>
         </div>
            <table style="width: 100%;">
                <tr>
                    <td style="width: 50%;">
                        <div class="row">
                            <h2 class="text-center mah_in">BILL To:</h2>
                                 <div class="left_info">
                                        <input type="text" class="clientDetails" id="ClientName" placeholder="Company Name" value="{{ data.ClientName }}"><br>
                                        <div class="clientDetails" id="ClientAddress">{{ data.ClientAddress }}</div><br>
                                        <input type="text" class="clientDetails" id="ClientGstNo" placeholder="GST No" value="GST No: {{ data.ClientGstNo }}"><br>
                                        <input type="text" class="clientDetails" id="ClientPanNo" placeholder="ClientPanNo" value="Pan No:{{ data.ClientPanNo }}"><br>
                                    </div>
                                </div>
                        </div>
                    </td>
                    <td style="width: 50%;">
                        <h2 class="text-center mah_in">SHIP To:</h2>
                    <div class="left_info">
                        <input type="text" class="clientDetails" id="ship_company_name" placeholder="Company Name" value="{{ data.ship_company_name }}"><br>
                        <input type="text" class="clientDetails" id="ship_customer_name" placeholder="Address" value="{{ data.ship_address }}"><br>
                        <input type="text" class="clientDetails" id="ship_occupation" placeholder="Contact Person" value="{{ data.ship_contact_person }}"><br>
                        <input type="text" class="clientDetails" id="ship_afm" placeholder="Contact No" value="{{ data.ship_contact_no }}"><br>
                        <input type="text" class="clientDetails" id="ship_doy" placeholder="Email" value="{{ data.ship_email }}">
                    </div>
                    </td>
                </tr>
            </table>
        <table class="inventory" id="inventory">
            <thead>
                <tr>
                    <th class="bold">
                        <span class="Particular" id="Particular">Particular</span>
                    </th>
                    <th class="bold">
                        <span class="rate" id="rate">Unit Price</span>
                    </th>
                    {% if "SGST+CGST" in data.Items|map(attribute='TaxName') %}
                        <th colspan="2" class="bold">
                            <span class="description" id="description">CGST</span>
                        </th>
                        <th colspan="2" class="bold">
                            <span class="description" id="description">SGST</span>
                        </th>
                    {% else %}
                        <th colspan="2" class="bold">
                            <span class="description" id="description">IGST</span>
                        </th>
                    {% endif %}
                    <th class="bold">
                        <span class="price" id="price">Total Price</span>
                    </th>
                </tr>
            </thead>
            
            <tbody>
                {% for item in data.Items %}
                    <tr>
                        <td>
                            <a class="cut" title="Remove Item">-</a>
                            <span contenteditable>{{ item.ServiceName }}</span>
                        </td>
                        <td>
                            <span data-prefix>&#8377;</span>
                            <span contenteditable>{{ item.Rate }}</span>
                        </td>
                        {% if "SGST+CGST" in item.TaxName %}
                            <td>
                                <span contenteditable>{{ (item.TaxPer)/2 }}%</span>
                            </td>
                            <td>
                                <span data-prefix>&#8377;</span><span contenteditable>{{ (item.TaxValue)/2 }}</span>
                            </td>
                            <td>
                                <span contenteditable>{{ (item.TaxPer)/2 }}%</span>
                            </td>
                            <td>
                                <span data-prefix>&#8377;</span><span contenteditable>{{ (item.TaxValue)/2 }}</span>
                            </td>
                        {% else %}
                            <td>
                                <span contenteditable>{{ item.TaxPer }}%</span>
                            </td>
                            <td>
                                <span data-prefix>&#8377;</span><span contenteditable>{{ item.TaxValue }}</span>
                            </td>
                        {% endif %}
                        <td>
                            <span data-prefix>&#8377;</span><span>{{ item.Rate+item.TaxValue }}</span>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
            </table>
            <div class="container">
            <table class="balance-master">
                <tr>
                    <td style="width: 50%;">
                        <div class="row">
                            <h2 class="text-center mah_in">Company Bank Details:</h2>
                                 <div class="left_info">
                                       <input type="text" class="bankDetails" id="bank_name" placeholder="Bank Name" value="{{ data.bank_name }}"><br>
                                        <input type="text" class="bankDetails" id="bank_address" placeholder="Bank Address" value="{{ data.bank_address }}"><br>
                                        <input type="text" class="bankDetails" id="bank_account_no" placeholder="Account No" value="{{ data.bank_account_no }}"><br>
                                        <input type="text" class="bankDetails" id="bank_ifsc" placeholder="IFSC Code" value="{{ data.bank_ifsc }}"><br>
                                    </div>
                                </div>
                        </div>
                    </td>
                    <td style="width: 50%;">
                    <table class="balance" id="balance">
                        <tbody>
                            <tr>
                                <th class="bold">
                                    <span class="subtotal" id="subtotal">Total</span>
                                </th>
                                <td>
                                    <span>&#8377;</span><span>{{ data.subtotal }}</span>
                                </td>
                            </tr>
                            <tr>
                                <th class="bold">
                                    <span class="tax" id="tax" contenteditable="">GST</span>
                                    <span contenteditable="">{{ data.TaxPer }}</span>
                                </th>
                                <td>
                                    <span>&#8377;</span><span>{{ data.sub }}</span>
                                </td>
                            </tr>
                            <tr>
                                <th class="bold">
                                    <span class="total" id="total">Grand Total</span>
                                </th>
                                <td>
                                    <span>&#8377; </span><span>{{ data.total_amount }}</span>
                                </td>
                            </tr>
                            <tr>
                                <th class="bold">
                                    <span class="total" id="total">Amount in Words</span>
                                    </th>
                                <td>
                                    <span>{{ data.amount_in_words }}</span>
                                </td>
                        </tbody>
                    </table>
                    </td>
                </tr>
            </table>
       </div>
            <div class="signature">
            <br>
            <p class="text-center">Authorised Signature</p>
            <p class="text-center">Accounts Department</p>
            </div>
        </article>
    </form>
</body>
</html>
 """


data = {
    "PrintType": "PDF",
    "CompanyName": "ABC Corporation",
    "CompanyAddress": "123 Main St",
    "CompanyGstNo": "27AAICM5811C1ZP",
    "CompanyBankName": "",
    "CompanyAccNo": "",
    "CompanyIFSC": "",
    "CompanyBranch": "",
    "BillNo": "123",
    "BillDate": "01-01-2022",
    "ClientName": "XYZ Inc.",
    "ClientAddress": "456 Oak St",
    "ClientGstNo": "27AAOCA9055C1ZJ",
    "ClientPanNo": "ABCDE1234F",
    "ClaimNo": "456789",
    "PolicyNo": "123456",
    "InsuredName": "Jane Doe",
    "InsuredLocation": "Anytown",
    "Amount": "",
    "Items": [
        {"ServiceName": "Consulting", "Rate": 200, "TaxValue": 10.0, "TaxName": "IGST", "TaxPer": 0.0},
        {"ServiceName": "Software Development", "Rate": 500, "TaxValue": 18.0, "TaxName": "IGST", "TaxPer": 0.0}
    ]
}

subtotal=0
taxtotal=0
total_amount=0

for item in data["Items"]:
    subtotal=subtotal+item["Rate"]
    taxtotal=taxtotal+item["TaxValue"]
    total_amount=total_amount+item["Rate"]+item["TaxValue"]

data["subtotal"]=subtotal
data["sub"]=taxtotal
data["total_amount"]=total_amount
data["amount_in_words"]=num2words(total_amount,lang='en_IN').title()+" Only"

template = Template(html)
html = template.render(data=data)


# Create a PDF from the HTML and save it to a file
# weasyprint.HTML(string=html).write_pdf('invoice.pdf',stylesheets=["style.css"])

pdfkit.from_string(html, "invoice.pdf", options={"enable-local-file-access": None,"page-size": "A4",
    "margin-top": "40mm",
    "margin-right": "10mm",
    "margin-bottom": "10mm",
    "margin-left": "10mm"},configuration=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))