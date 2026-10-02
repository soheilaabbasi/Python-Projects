![alt text](../images/banner.png)

# Mastering Email Automation with Python

In today's digital age, email remains a cornerstone of communication, both personal and professional. As developers, the ability to programmatically send, receive, and process emails opens up a world of possibilities for automation, data analysis, and building powerful applications. Python, with its rich ecosystem of libraries and straightforward syntax, is an excellent choice for working with emails.

Python offers several advantages when it comes to email manipulation:

1. __Rich Standard Library:__ Python's built-in smtplib and email modules provide robust functionality for sending emails and creating email content.

2. __Extensive Third-Party Libraries:__ Libraries like imaplib for IMAP protocol handling, and higher-level wrappers like yagmail for Gmail, extend Python's email capabilities.

3. __Cross-Platform Compatibility:__ Python's email handling works consistently across different operating systems.

4. __Integration Capabilities:__ Easy integration with web frameworks, data analysis tools, and other Python libraries for comprehensive solutions.

Throughout this lecture, we'll cover:

    1. Setting up your Python environment for email handling
    2. Sending simple text emails
    3. Creating and sending HTML emails with attachments
    4. Working with email templates
    5. Handling multiple recipients (To, Cc, Bcc)
    6. Connecting to IMAP servers to read emails
    7. Processing and analyzing email content
    8. Best practices and security considerations

Let's begin with a basic example of sending an email using Python's `smtplib`:

```
import smtplib
from email.mime.text import MIMEText

def send_email(sender, recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, 'your_password_here')
        server.send_message(msg)

# Usage
send_email('sender@example.com', 'recipient@example.com', 'Hello from Python', 'This is a test email sent from Python!')
```

This script demonstrates the basic steps involved in sending an email:

    1. Creating an email message
    2. Connecting to an SMTP server
    3. Authenticating
    4. Sending the message

💡 __Note:__ This example uses Gmail's SMTP server. You'll need to adjust the settings for other email providers, and for Gmail, you might need to use an "App Password" instead of your regular password due to security settings.

Imagine the possibilities:

    - Sending personalized newsletters to thousands of subscribers
    - Automatically responding to customer inquiries
    - Monitoring an inbox for specific types of messages and taking action
    - Analyzing email patterns in a large dataset

As we progress through this lecture, you'll gain the skills to implement these and many more email-related tasks efficiently using Python.

🔑 __Key Concept:__ Python's email handling capabilities extend far beyond just sending and receiving messages. They provide a foundation for building sophisticated email-based applications and automation systems.

In the next sections, we'll dive deeper into the specifics of email handling in Python, exploring more advanced features and best practices. Get ready to unlock the full potential of email automation with Python!

## Python's smtplib Library: An Overview

__Table of contents__

- Python's smtplib Library: An Overview
    - What is smtplib?
    - Key Features of smtplib
    - Basic Usage of smtplib
    - Key Methods in smtplib.SMTP
    - Advanced Features
    - Best Practices
- Composing Simple Text Emails
    - Basic Structure of a Text Email
    - Using email.mime.text.MIMEText
    - Formatting Text in the Email Body
    - Handling Special Characters
    - Best Practices for Text Emails
    - Practical Example: Automated Report Email
- Creating HTML Emails
    - Why Use HTML Emails?
    - Basic Structure of an HTML Email
    - Creating an HTML Email with Python
    - Best Practices for HTML Emails
    - Adding Images to HTML Emails
    - Creating Responsive HTML Emails
    - Using Email Templates
- Handling Email Attachments
    - Why Use Email Attachments?
    - Adding Attachments to Emails
    - Handling Multiple Attachments
    - Best Practices for Email Attachments
    - Handling Different File Types
    - Reading Attachments from Received Emails
- Sending Emails to Multiple Recipients
    - Types of Multiple Recipients
    - Basic Approach to Sending to Multiple Recipients
    - Using Cc and Bcc
    - Best Practices for Sending to Multiple Recipients
    - Personalization for Multiple Recipients
    - Handling Bounced Emails
- Advanced Topics: Email Templates and Personalization
    - Why Use Email Templates and Personalization?
    - Using Jinja2 for Email Templates
    - Creating Reusable Template Files
    - Advanced Personalization Techniques
    - Handling Complex Data Structures
    - Best Practices for Email Templates and Personalization
    - Integrating with Email Sending
- Final Summary: Mastering Email Automation with Python

The smtplib library is a core component of Python's email handling capabilities. It implements the Simple Mail Transfer Protocol (SMTP), allowing you to send emails from your Python scripts. Understanding this library is crucial for anyone looking to automate email sending or build email-related applications in Python.

## What is smtplib?
`smtplib` is part of Python's standard library, which means it's available in every Python installation without the need for additional installations. This library provides an implementation of the SMTP protocol, enabling communication with mail servers to send emails.

## Key Features of smtplib

__1. SMTP and ESMTP support:__ Handles both basic SMTP and Extended SMTP protocols.
__2. TLS/SSL encryption:__ Supports secure connections to mail servers.
__3. Authentication:__ Allows for username/password authentication with mail servers.
__4. Multiple recipients:__ Can send emails to multiple recipients in one go.
__5. Error handling:__ Provides detailed error messages for troubleshooting.


## Basic Usage of smtplib

Let's break down the basic steps to send an email using `smtplib`:

```
import smtplib
from email.mime.text import MIMEText

# Create the email content
msg = MIMEText("This is the email body")
msg['Subject'] = "Email Subject"
msg['From'] = "sender@example.com"
msg['To'] = "recipient@example.com"

# Connect to the SMTP server
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "sender@example.com"
password = "your_password_here"

try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()
```

## Key Methods in smtplib.SMTP

- SMTP(host, port): Creates an SMTP object to connect to the specified server.
- starttls(): Puts the connection to the SMTP server into TLS mode.
- login(user, password): Logs in to the server using the provided credentials.
- send_message(msg): Sends the email message.
- quit(): Terminates the SMTP session and closes the connection.


## Advanced Features

__1. Handling Attachments__

To send attachments, you'll need to use `MIMEMultipart` and `MIMEBase` from the `email.mime` module:  

```
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
# ... set up the basic email headers ...

# Add attachment
filename = "document.pdf"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")

msg.attach(part)
```

__2. Sending to Multiple Recipients__

You can send to multiple recipients by separating email addresses with commas in the 'To' field:

`msg['To'] = "recipient1@example.com, recipient2@example.com"`

__3. Using CC and BCC__

```
msg['Cc'] = "cc_recipient@example.com"
msg['Bcc'] = "bcc_recipient@example.com"
```

## Composing Simple Text Emails

While modern emails often contain rich HTML content and attachments, there's still a place for simple, straightforward text emails. They're quick to compose, universally compatible, and perfect for many automated tasks. Let's explore how to create and send simple text emails using Python.

### Basic Structure of a Text Email
A simple text email consists of a few key components:

1. Sender's email address
2. Recipient's email address
3. Subject line
4. Email body (plain text)

### Using email.mime.text.MIMEText

Python's `email.mime.text` module provides the `MIMEText` class, which is perfect for creating simple text emails. Here's how to use it:

```
from email.mime.text import MIMEText
import smtplib

def send_simple_email(sender, recipient, subject, body):
    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    password = "your_password"

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
send_simple_email(
    "sender@example.com",
    "recipient@example.com",
    "Hello from Python",
    "This is a simple text email sent from Python."
)
```

To send an email to multiple recipients, you can separate email addresses with commas:
`msg['To'] = "recipient1@example.com, recipient2@example.com"`

Alternatively, you can use the `COMMASPACE` constant from the `email.utils` module:

```
from email.utils import COMMASPACE

recipients = ["recipient1@example.com", "recipient2@example.com"]
msg['To'] = COMMASPACE.join(recipients)
To add CC (Carbon Copy) and BCC (Blind Carbon Copy) recipients:

msg['Cc'] = "cc_recipient@example.com"
msg['Bcc'] = "bcc_recipient@example.com"
```

Remember that BCC recipients are not visible to other recipients.

### Formatting Text in the Email Body

While we're working with plain text emails, you can still use some basic formatting to improve readability:

```
body = """
Dear Recipient,

I hope this email finds you well.

Here are a few key points:
1. First item
2. Second item
3. Third item

Best regards,
Sender
"""
```

msg = MIMEText(body)

### Handling Special Characters

If your email contains non-ASCII characters, you should specify the character encoding:
```
body = "This contains special characters: áéíóú"
msg = MIMEText(body, _charset="utf-8")
```

### Best Practices for Text Emails

__1. Keep it concise:__ Text emails are best when they're short and to the point.
__2. Use line breaks wisely:__ Structure your content with appropriate line breaks for readability.
__3. Avoid large blocks of text:__ Break up your content into smaller paragraphs.
__4. Use simple formatting:__ Utilize asterisks, dashes, or numbers for lists and emphasis.
__5. Include a signature:__ End your email with a clear signature for identification.

### Practical Example: Automated Report Email

Here's an example of how you might use a simple text email to send an automated report:

```
def send_daily_report(recipient, sales_data):
    subject = f"Daily Sales Report - {datetime.date.today()}"
    body = f"""
    Daily Sales Report
    Date: {datetime.date.today()}

    Total Sales: ${sales_data['total']}
    Number of Transactions: {sales_data['transactions']}
    Top Selling Item: {sales_data['top_item']}

    For more details, please check the attached report.

    Best regards,
    Sales Automation Team
    """

    send_simple_email("reports@company.com", recipient, subject, body)

# Usage
sales_data = {
    'total': 15000,
    'transactions': 143,
    'top_item': 'Widget X'
}
send_daily_report("manager@company.com", sales_data)
```

🔑 __Key Takeaway:__ Simple text emails are powerful tools for automated communication. They're quick to compose, widely compatible, and perfect for conveying straightforward information.

By mastering the creation and sending of simple text emails, you've laid the groundwork for more advanced email operations in Python. In the next sections, we'll explore how to enhance your emails with HTML formatting and attachments.


## Creating HTML Emails

While plain text emails have their place, HTML emails offer richer formatting options, allowing for more visually appealing and interactive content. Let's explore how to create and send HTML emails using Python.

### Why Use HTML Emails?

HTML emails provide several advantages:

    - Enhanced visual appeal with formatting, colors, and layout
    - Ability to include images and links
    - Support for responsive design for better mobile viewing
    - Improved tracking capabilities (e.g., open rates, click-through rates)


### Basic Structure of an HTML Email

An HTML email typically consists of:

    1. HTML content (the email body)
    2. Optional plain text alternative (for email clients that don't support HTML)
    3. Email headers (From, To, Subject, etc.)


### Creating an HTML Email with Python

To create an HTML email, we'll use the `email.mime.multipart.MIMEMultipart` and `email.mime.text.MIMEText` classes:

```
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_html_email(sender, recipient, subject, html_content, text_content):
    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Record the MIME types of both parts - text/plain and text/html
    part1 = MIMEText(text_content, 'plain')
    part2 = MIMEText(html_content, 'html')

    # Attach parts into message container
    # According to RFC 2046, the last part of a multipart message is best and preferred
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(sender, 'your_password')
        s.send_message(msg)
        print("Email sent successfully!")

# Usage
html_content = """
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>This is an <b>HTML</b> email sent from <i>Python</i>.</p>
    <p>Here's a list:
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
    </p>
  </body>
</html>
"""

text_content = """
Hello, World!
This is a plain text version of the HTML email sent from Python.
Here's a list:
- Item 1
- Item 2
- Item 3
"""

send_html_email(
    "sender@example.com",
    "recipient@example.com",
    "HTML Email Test",
    html_content,
    text_content
)
```

### Best Practices for HTML Emails

 __1. Always include a plain text alternative:__ Some email clients or users prefer plain text, and it helps with deliverability.

__2. Use inline CSS:__ Many email clients strip out `<style>` tags, so use inline styles for consistent rendering.

__3. Keep it simple:__ Complex layouts can break in some email clients. Stick to simple, table-based layouts for best compatibility.

__4. Test across multiple clients:__ Email rendering can vary widely between clients. Test your emails in various popular email clients.

__5. Optimize images:__ Use appropriate file formats and sizes to ensure quick loading, especially on mobile devices.

__6. Be mindful of spam filters:__ Avoid excessive use of images, certain words, or all-caps that might trigger spam filters.

### Adding Images to HTML Emails

To include images in your HTML email, you can either link to external images or embed them directly in the email using base64 encoding. Here's an example of linking to an external image:

```
html_content = """
<html>
  <body>
    <h1>Check out this image!</h1>
    <img src="https://example.com/image.jpg" alt="An example image" style="width:100%; max-width:600px;">
  </body>
</html>
"""
```

💡 __Pro Tip:__ When using external images, be aware that some email clients block external images by default for security reasons.

### Creating Responsive HTML Emails

To ensure your emails look good on both desktop and mobile devices, consider using responsive design techniques:

```
<html>
  <head>
    <style>
      @media only screen and (max-width: 600px) {
        .container {
          width: 100% !important;
        }
      }
    </style>
  </head>
  <body>
    <table class="container" width="600" style="max-width: 600px; margin: auto;">
      <tr>
        <td>
          <h1>Responsive Email</h1>
          <p>This email will adjust to screen size.</p>
        </td>
      </tr>
    </table>
  </body>
</html>
```

### Using Email Templates

For more complex HTML emails, consider using a templating engine like Jinja2:

```
from jinja2 import Template

template_string = """
<html>
  <body>
    <h1>Hello, {{ name }}!</h1>
    <p>Your account balance is ${{ balance }}.</p>
  </body>
</html>
"""

template = Template(template_string)
html_content = template.render(name="John Doe", balance=1000)
```

🔑 __Key Takeaway:__ HTML emails offer powerful formatting and design options, but require careful consideration of email client compatibility and best practices for optimal delivery and rendering.

By mastering HTML email creation in Python, you can create more engaging and visually appealing emails for your recipients. Whether you're sending newsletters, promotional content, or rich informational emails, these techniques will help you craft effective HTML emails programmatically.


## Handling Email Attachments

Attaching files to emails is a common requirement in many applications, from sending reports to sharing documents. Python provides robust capabilities for handling email attachments, allowing you to send various file types with ease.

### Why Use Email Attachments?

Email attachments allow you to:

- Share documents, images, or other files directly within an email
- Send larger amounts of data than what can be comfortably included in the email body
- Maintain the original format and integrity of files


### Adding Attachments to Emails

To add attachments to an email, we'll use the `email.mime.multipart.MIMEMultipart` and `email.mime.base.MIMEBase` classes, along with the `email.encoders` module.

Here's a basic example of how to send an email with an attachment:

```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender, recipient, subject, body, file_path):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    # Open the file in bynary
    binary_file = open(file_path, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=os.path.basename(file_path))
    payload.set_payload((binary_file).read())

    # Encode the payload using Base64
    encoders.encode_base64(payload)

    # Add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=os.path.basename(file_path))
    msg.attach(payload)

    # Create SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(sender, 'your_password')
        text = msg.as_string()
        session.sendmail(sender, recipient, text)
        print('Email sent successfully')

# Usage
send_email_with_attachment(
    'sender@example.com',
    'recipient@example.com',
    'Email with Attachment',
    'Please find the attached file.',
    '/path/to/your/file.pdf'
)
```

### Handling Multiple Attachments

To send multiple attachments, you can simply repeat the attachment process for each file:

```
def add_attachment(msg, file_path):
    with open(file_path, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
    msg.attach(part)

def send_email_with_multiple_attachments(sender, recipient, subject, body, file_paths):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for file_path in file_paths:
        add_attachment(msg, file_path)

    # Send the email (SMTP setup and sending code here)
```


### Best Practices for Email Attachments

__1. File Size Limits:__ Be aware of email size limits. Many email providers have a maximum attachment size (often around 25MB).

__2. File Types:__ Some file types (like executables) may be blocked by email servers. Stick to common document and media formats when possible.

__3.Compression:__ For large files, consider compressing them before attaching to reduce the email size.

__4. Naming Conventions:__ Use clear, descriptive names for your attachments, avoiding special characters.

__5. Security:__ Be cautious about the content you're sending. Avoid sending sensitive information in unencrypted attachments.

### Handling Different File Types

Different file types may require different MIME types. Here are some common ones:

    - PDF: application/pdf
    - Images (JPEG): image/jpeg
    - Word Document: application/msword
    - Excel Spreadsheet: application/vnd.ms-excel

You can specify the MIME type when creating the `MIMEBase` object:

`part = MIMEBase('application', 'pdf')  `


### Reading Attachments from Received Emails

When you're on the receiving end, you might need to extract attachments from emails. Here's a basic example using the `imaplib` library:

```
import imaplib
import email

def get_attachments(email_message):
    attachments = []
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join('/path/to/attachment/dir', fileName)
            with open(filePath, 'wb') as f:
                f.write(part.get_payload(decode=True))
            attachments.append(filePath)
    return attachments

# Connect to an IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email@gmail.com', 'your_password')
mail.select('inbox')

# Search for specific emails (e.g., all emails)
_, search_data = mail.search(None, 'ALL')

for num in search_data[0].split():
    _, data = mail.fetch(num, '(RFC822)')
    email_body = data[0][1]
    email_message = email.message_from_bytes(email_body)
    
    attachments = get_attachments(email_message)
    print(f"Attachments saved: {attachments}")
```

🔑 __Key Takeaway:__ Handling email attachments in Python involves working with MIME types and encodings. Whether you're sending or receiving attachments, understanding these concepts is crucial for effective email automation.

By mastering the handling of email attachments, you can greatly expand the capabilities of your email-based Python applications, enabling more complex and data-rich communications.

## Sending Emails to Multiple Recipients

When it comes to email automation, the ability to send emails to multiple recipients is crucial. Whether you're distributing newsletters, sending team updates, or managing a mailing list, understanding how to efficiently handle multiple recipients in Python is essential.

### Types of Multiple Recipients

In email, there are three types of recipients:

__1. To:__ The primary recipients of the email.
__2. Cc (Carbon Copy):__ Secondary recipients whose names are visible to all other recipients.
__3. Bcc (Blind Carbon Copy):__ Recipients whose names are not visible to other recipients.

### Basic Approach to Sending to Multiple Recipients

Here's a simple way to send an email to multiple recipients using Python's `smtplib`:

```
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_to_multiple_recipients(sender, recipients, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)  # Join all recipients with commas
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    password = "your_password_here"

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
sender = "your_email@gmail.com"
recipients = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
subject = "Group Announcement"
body = "This is a test email sent to multiple recipients."

send_email_to_multiple_recipients(sender, recipients, subject, body)
```

### Using Cc and Bcc

To include Cc and Bcc recipients, you can modify the above function:

```
def send_email_with_cc_bcc(sender, to_recipients, cc_recipients, bcc_recipients, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(to_recipients)
    msg['Cc'] = ', '.join(cc_recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Combine all recipients for sending
    all_recipients = to_recipients + cc_recipients + bcc_recipients

    # SMTP setup and sending (as in the previous example)
    # ...

# Usage
sender = "your_email@gmail.com"
to_recipients = ["primary1@example.com", "primary2@example.com"]
cc_recipients = ["cc1@example.com", "cc2@example.com"]
bcc_recipients = ["bcc1@example.com", "bcc2@example.com"]
subject = "Meeting Minutes"
body = "Please find attached the minutes from our recent meeting."

send_email_with_cc_bcc(sender, to_recipients, cc_recipients, bcc_recipients, subject, body)
```

### Best Practices for Sending to Multiple Recipients

1. __Use BCC for Large Lists:__ When sending to a large number of recipients, use BCC to protect their privacy and prevent reply-all chaos.

2. __Respect Anti-Spam Laws:__ Ensure you have permission to email all recipients and include an unsubscribe option in mass emails.

3. __Personalization:__ Consider personalizing emails when possible, even when sending to multiple recipients.

4. __Batch Sending:__ For very large lists, consider sending in batches to avoid overwhelming your SMTP server or triggering spam filters.


### Personalization for Multiple Recipients

Here's an example of how you might personalize emails for multiple recipients:

```
from jinja2 import Template

def send_personalized_emails(sender, recipients, subject_template, body_template):
    subject_tmpl = Template(subject_template)
    body_tmpl = Template(body_template)

    for recipient in recipients:
        personalized_subject = subject_tmpl.render(name=recipient['name'])
        personalized_body = body_tmpl.render(name=recipient['name'], info=recipient['info'])

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient['email']
        msg['Subject'] = personalized_subject
        msg.attach(MIMEText(personalized_body, 'plain'))

        # SMTP setup and sending for each personalized email
        # ...

# Usage
recipients = [
    {"name": "Alice", "email": "alice@example.com", "info": "Team Lead"},
    {"name": "Bob", "email": "bob@example.com", "info": "Developer"},
    {"name": "Charlie", "email": "charlie@example.com", "info": "Designer"}
]

subject_template = "Hello {{ name }}, here's your update"
body_template = """
Dear {{ name }},

This is your personalized update. As our {{ info }}, we wanted to inform you about...

Best regards,
The Management Team
"""

send_personalized_emails("sender@example.com", recipients, subject_template, body_template)
```

### Handling Bounced Emails

When sending to multiple recipients, it's important to handle bounced emails:

```
def send_with_bounce_handling(sender, recipients, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender, "your_password")
            
            failed_recipients = {}
            for recipient in recipients:
                msg['To'] = recipient
                try:
                    server.send_message(msg)
                    print(f"Email sent to {recipient}")
                except smtplib.SMTPException as e:
                    failed_recipients[recipient] = str(e)
            
            if failed_recipients:
                print("Failed to send to some recipients:")
                for recipient, error in failed_recipients.items():
                    print(f"{recipient}: {error}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

🔑 __Key Takeaway:__ Sending emails to multiple recipients involves more than just adding multiple addresses. Consider privacy, personalization, and proper handling of different recipient types (To, Cc, Bcc) for effective email communication.

By mastering these techniques, you can create powerful email automation systems capable of handling complex mailing scenarios, from personalized bulk emails to carefully managed group communications.

## Advanced Topics: Email Templates and Personalization

As you advance in your email automation journey, you'll likely encounter scenarios that require more sophisticated email content creation. This is where email templates and personalization come into play, allowing you to create dynamic, tailored emails at scale.

### Why Use Email Templates and Personalization?

1. __Consistency:__ Maintain a consistent brand voice and structure across all communications.
2. __Efficiency:__ Save time by reusing templates instead of writing emails from scratch.
3. __Personalization:__ Increase engagement by tailoring content to individual recipients.
4. __Scalability:__ Easily manage and update email content for large-scale sending.


### Using Jinja2 for Email Templates

Jinja2 is a powerful and flexible templating engine for Python. It's particularly well-suited for creating email templates. Here's how you can use it:

First, install Jinja2:

`pip install Jinja2`

Now, let's create a simple email template:

```
from jinja2 import Template

html_template = """
<html>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>We noticed you've been using our {{ product }} for {{ days }} days.</p>
    {% if days > 30 %}
    <p>As a valued long-term user, we'd like to offer you a special discount!</p>
    {% else %}
    <p>We hope you're enjoying it so far!</p>
    {% endif %}
    <p>Best regards,<br>The {{ team }} Team</p>
</body>
</html>
"""

def generate_email(template_string, **kwargs):
    template = Template(template_string)
    return template.render(**kwargs)

# Usage
email_content = generate_email(html_template, 
                               name="Alice", 
                               product="SuperApp", 
                               days=45, 
                               team="Customer Success")

print(email_content)
```

### Creating Reusable Template Files

For more complex templates, it's better to store them in separate files:

```
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

def generate_email_from_file(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)

# Usage
email_content = generate_email_from_file('welcome_email.html', 
                                         name="Bob", 
                                         product="MegaTool")
```

In this case, you'd have a file named `welcome_email.html` in a `templates` directory.

### Advanced Personalization Techniques

1. __Dynamic Content Blocks__

You can use Jinja2's `{% if %}` statements to include or exclude entire sections based on user data:

```
{% if user.subscription_tier == 'premium' %}
<section class="premium-content">
    <h2>Exclusive Premium Content</h2>
    <p>Here's some special content just for our premium subscribers!</p>
</section>
{% endif %}
```

2. __Loops for Dynamic Lists__

Use loops to generate dynamic content, like product recommendations:

```
<h2>Recommended for You</h2>
<ul>
{% for product in recommended_products %}
    <li>{{ product.name }} - ${{ product.price }}</li>
{% endfor %}
</ul>
```

3. __Filters for Data Formatting__

Jinja2 filters can help format data in your templates:

<p>Your subscription will renew on {{ renewal_date|date_format('%B %d, %Y') }}.</p>
You'd need to define the `date_format` filter in your Python code.


### Handling Complex Data Structures

Sometimes you'll need to work with more complex data structures in your templates. Jinja2 can handle nested dictionaries and lists with ease:

```
user_data = {
    'name': 'Charlie',
    'purchases': [
        {'item': 'Widget A', 'price': 19.99},
        {'item': 'Gadget B', 'price': 29.99}
    ],
    'total_spent': 49.98
}

template_string = """
<h1>Thank you for your purchase, {{ name }}!</h1>
<h2>Your Items:</h2>
<ul>
{% for purchase in purchases %}
    <li>{{ purchase.item }} - ${{ purchase.price }}</li>
{% endfor %}
</ul>
<p>Total: ${{ total_spent }}</p>
"""

email_content = generate_email(template_string, **user_data)
```

### Best Practices for Email Templates and Personalization

1. __Test Thoroughly:__ Always test your templates with various data inputs to ensure they render correctly in all scenarios.

2. __Use Fallback Values:__ Provide default values for optional template variables to prevent errors:

`<p>Hello, {{ name|default('Valued Customer') }}!</p>`

3. __Keep It Simple:__ While powerful, overly complex templates can be hard to maintain. Strike a balance between flexibility and simplicity.

4. __Modular Design:__ Break your templates into reusable components. Jinja2 supports template inheritance and includes, which can help organize complex email designs.

5. __Responsive Design:__ Ensure your HTML templates are responsive for proper rendering on various devices and email clients.

6. __Personalization Beyond Just Names:__ Consider personalizing based on user behavior, preferences, or other relevant data points.

7. __A/B Testing:__ Use template variations to A/B test different email designs or content strategies.

### Integrating with Email Sending

To use these templates in your email sending function:

```
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_personalized_email(sender, recipient, subject, template_name, **template_data):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Generate HTML content
    html_content = generate_email_from_file(template_name, **template_data)
    
    # Attach parts
    msg.attach(MIMEText(html_content, 'html'))

    # SMTP sending code here
    # ...

# Usage
send_personalized_email('sender@example.com', 
                        'recipient@example.com', 
                        'Your Weekly Update', 
                        'weekly_update.html', 
                        name='David', 
                        points=250, 
                        level='Gold')
```

🔑 __Key Takeaway:__ Email templates and personalization are powerful tools for creating engaging, dynamic email content at scale. By leveraging templating engines like Jinja2, you can create flexible, maintainable email templates that adapt to your users' individual characteristics and behaviors.

Mastering these techniques allows you to create sophisticated email automation systems that can handle complex, personalized communication needs while maintaining efficiency and scalability.

## Final Summary: Mastering Email Automation with Python

Throughout this lecture, we've explored the multifaceted world of email automation using Python. Let's recap the key points and reflect on the power and versatility of email handling in Python:

1. __Foundation of Email Handling:__ We began with an introduction to email handling in Python, understanding the basic components and libraries involved, particularly smtplib for sending emails.

2. __Composing Emails:__ We learned how to compose both simple text emails and more complex HTML emails, giving us the flexibility to create various types of email content.

3. __Attachments:__ The ability to handle email attachments opened up possibilities for sharing documents, reports, and other files programmatically.

4. __Multiple Recipients:__ We explored techniques for sending emails to multiple recipients, including the use of CC and BCC, essential for managing group communications and mailing lists.

5. __Templates and Personalization:__ Advanced topics like email templates and personalization demonstrated how to create dynamic, tailored email content at scale, significantly enhancing the effectiveness of email communications.

Python's rich ecosystem of libraries and its straightforward syntax make it an excellent choice for email automation tasks. From simple scripts to complex email marketing systems, Python provides the tools and flexibility to handle a wide range of email-related challenges.

__Best practices for email automation include:__

- Always prioritize security, using encryption and proper authentication methods.
- Respect email etiquette and anti-spam laws when sending bulk emails.
- Test your email scripts thoroughly, especially when using templates or personalization.
- Keep your code modular and well-documented for easy maintenance and scalability.
- Stay updated with the latest email standards and best practices to ensure deliverability.

As email continues to be a critical communication tool, the skills you've learned in this lecture will prove invaluable. Whether you're building automated notification systems, managing customer communications, or developing sophisticated email marketing campaigns, the foundations laid here will serve as a solid starting point.

To further enhance your email automation skills, consider exploring:

- Integration with web frameworks for building email-based web applications
- Advanced email analytics and tracking
- Machine learning for email content optimization and spam detection
- Compliance with international email regulations (like GDPR)


🔑 __Final Thought:__ Email automation with Python is a powerful skill that bridges the gap between programming and effective communication. By mastering these techniques, you're well-equipped to create efficient, scalable, and sophisticated email systems that can significantly impact how organizations and individuals manage their communications.

Remember, the world of email technology is ever-evolving, so keep learning and adapting your skills to stay at the forefront of email automation capabilities.

